import styles from '@/styles/Insert.module.css'
import { useRef, useState, MouseEvent } from 'react'

interface InsertProps {
  contactsEndpoint: string
}

interface Error422Item {
  loc: string[]
  msg: string
}

interface ErrorMessages {
  name?: string
  phone?: string
}

export default function Insert(props: InsertProps) {
  const [name, setName] = useState<string>('')
  const [phone, setPhone] = useState<string>('')
  const [result, setResult] = useState<boolean | null>(null)
  const [errorMsgs, setErrorMsgs] = useState<ErrorMessages>({})
  const insertingData = useRef<object | null>(null)

  const handleButtonClick = async (evt: MouseEvent<HTMLElement>) => {
    evt.preventDefault()
    const data = {
      name,
      phone,
    }
    setErrorMsgs({})
    insertingData.current = data
    const resp = await fetch(props.contactsEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    if (resp.ok) {
      const res = await resp.json()
      if (insertingData.current === data) {
        insertingData.current = null
        setResult(res)
      }
    } else {
      const newErrorMsgs: ErrorMessages = {}
      if (resp.status === 422) {
        const res = await resp.json()
        res.detail.forEach((errDetail: Error422Item) => {
          if (
            JSON.stringify(errDetail.loc) === JSON.stringify(['body', 'name'])
          ) {
            newErrorMsgs.name = errDetail.msg
          }
          if (
            JSON.stringify(errDetail.loc) === JSON.stringify(['body', 'phone'])
          ) {
            newErrorMsgs.phone = errDetail.msg
          }
        })
      }
      if (insertingData.current === data) {
        insertingData.current = null
        setResult(false)
        setErrorMsgs(newErrorMsgs)
      }
    }
  }

  let resultJsx = null
  if (result !== null) {
    resultJsx = result ? (
      <div>Data successfully inserted!</div>
    ) : (
      <div className="warn">Data was not inserted!</div>
    )
  }

  return (
    <form className={styles.insert}>
      <div>
        <h3>Name</h3>
        <input
          type="text"
          onChange={(e) => {
            setResult(null)
            setName(e.target.value)
          }}
          value={name}
        />
        {errorMsgs.name ? <div className="warn">{errorMsgs.name}</div> : null}
      </div>
      <div>
        <h3>Phone number</h3>
        <input
          type="text"
          onChange={(e) => {
            setResult(null)
            setPhone(e.target.value)
          }}
          value={phone}
        />
        {errorMsgs.phone ? <div className="warn">{errorMsgs.phone}</div> : null}
      </div>
      {resultJsx}
      <button onClick={handleButtonClick}>Insert</button>
    </form>
  )
}
