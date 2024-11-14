import styles from "@/styles/Insert.module.css";
import {MutableRefObject, useRef, useState, MouseEvent} from "react";

export default function Insert() {
  const [name, setName] = useState<string>("");
  const [phone, setPhone] = useState<string>("");
  const [result, setResult] = useState<boolean | null>(null);
  const insertingData: MutableRefObject<object | null> = useRef(null);

  const handleButtonClick = async (evt: MouseEvent<HTMLElement>) => {
    evt.preventDefault()
    const data = {
      name,
      phone,
    }
    insertingData.current = data
    const resp = await fetch('http://127.0.0.1:8000/phonebook/contacts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    });
    if(resp.ok) {
      const res = await resp.json()
      if(insertingData.current === data) {
        insertingData.current = null;
        setResult(res)
      }
    } else {
      if(insertingData.current === data) {
        insertingData.current = null;
        setResult(false)
      }
    }
  }

  let resultJsx = null;
  if (result !== null) {
    resultJsx = result ? <div>Data successfully inserted!</div> : <div className="warn">Data was not inserted!</div>
  }

  return (
      <form className={styles.insert}>
        <div>
          <h3>Name</h3>
          <input type="text"
                 onChange={(e) => {
                   setResult(null)
                   setName(e.target.value)
                 }}
                 value={name}
          />
        </div>
        <div>
          <h3>Phone number</h3>
          <input type="text"
                 onChange={(e) => {
                   setResult(null)
                   setPhone(e.target.value)
                 }}
                 value={phone}
          />
        </div>
        {resultJsx}
        <button onClick={handleButtonClick}>Insert</button>
      </form>
  );
}
