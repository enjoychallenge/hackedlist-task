import styles from "@/styles/Search.module.css";
import {useEffect, useRef, useState} from "react";

interface FoundPhonesProps {
  foundPhones: string[];
}

const FoundPhones = (props: FoundPhonesProps) => {
  if(props.foundPhones.length > 0) {
    return <>
      <h3>Found phone numbers</h3>
      <ul>
          {
            props.foundPhones.map((foundPhone, idx) => {
              return <li key={idx}>{foundPhone}</li>
            })
          }
      </ul>
    </>
  } else {
    return <div className="warn">No phone numbers found!</div>
  }
}

export default function Search() {
  const [searchText, setSearchText] = useState<string>("");
  const requestingText = useRef<string | null>(null);
  const [foundPhones, setFoundPhones] = useState<string[]>([]);

  useEffect(() => {
    if (searchText.length > 0) {

      const urlParams = new URLSearchParams({
        prefix: searchText,
      }).toString()

      requestingText.current = searchText
      fetch(`http://127.0.0.1:8000/phonebook/contacts?${urlParams}`)
          .then(async (response) => {
            if(requestingText.current !== searchText) {
              return
            }
            if (response.ok) {
              const phones = await response.json()
              if (requestingText.current !== searchText) {
                return
              }
              requestingText.current = null;
              setFoundPhones(phones)
            } else {
              requestingText.current = null;
              setFoundPhones([])
            }
          })
    } else {
      setFoundPhones([])
    }
  }, [searchText]);

  let results = <>Loading data ...</>
  if (requestingText.current === null) {
     results = searchText.length > 0 ? <FoundPhones foundPhones={foundPhones} /> : <>Type at least 1 letter.</>
  }

  return (
      <div className={styles.search}>
        <input type="text"
               onChange={(e) => setSearchText(e.target.value)}
               value={searchText}
        />
        <div>
          {results}
        </div>
      </div>
  );
}
