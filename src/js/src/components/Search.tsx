import styles from '@/styles/Search.module.css'
import { useEffect, useRef, useState } from 'react'

interface FoundPhonesProps {
  foundPhones: string[]
}

const FoundPhones = (props: FoundPhonesProps) => {
  if (props.foundPhones.length > 0) {
    return (
      <>
        <h3>Found phone numbers</h3>
        <ul>
          {props.foundPhones.map((foundPhone, idx) => {
            return <li key={idx}>{foundPhone}</li>
          })}
        </ul>
      </>
    )
  } else {
    return <div className="warn">No phone numbers found!</div>
  }
}

interface SearchProps {
  contactsEndpoint: string
}

export default function Search(props: SearchProps) {
  const [searchText, setSearchText] = useState<string>('')
  const requestingText = useRef<string | null>(null)
  const [foundPhones, setFoundPhones] = useState<string[]>([])

  useEffect(() => {
    if (searchText.length > 0) {
      const urlParams = new URLSearchParams({
        prefix: searchText,
      }).toString()

      requestingText.current = searchText
      fetch(`${props.contactsEndpoint}?${urlParams}`).then(async (response) => {
        if (requestingText.current !== searchText) {
          return
        }
        if (response.ok) {
          const phones = await response.json()
          if (requestingText.current !== searchText) {
            return
          }
          requestingText.current = null
          setFoundPhones(phones)
        } else {
          requestingText.current = null
          setFoundPhones([])
        }
      })
    } else {
      setFoundPhones([])
    }
  }, [searchText, props.contactsEndpoint])

  let results = <>Loading data ...</>
  if (requestingText.current === null) {
    results =
      searchText.length > 0 ? (
        <FoundPhones foundPhones={foundPhones} />
      ) : (
        <>Type at least 1 letter.</>
      )
  }

  return (
    <div className={styles.search}>
      <input
        type="text"
        onChange={(e) => setSearchText(e.target.value)}
        value={searchText}
      />
      <div>{results}</div>
    </div>
  )
}
