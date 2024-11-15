import Head from "next/head";
import Search from "./../components/Search"
import Insert from "./../components/Insert"
import styles from "@/styles/Home.module.css";

const CONTACTS_ENDPOINT = 'http://127.0.0.1:8000/phonebook/contacts'

export default function Home() {
  return (
    <>
      <Head>
        <title>Phonebook</title>
        <meta name="description" content="Phonebook" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.png" />
      </Head>
      <main className={styles.main}>
        <div>
          <h2>Insert phone number</h2>
          <Insert contactsEndpoint={CONTACTS_ENDPOINT}/>
        </div>
        <div>
          <h2>Search phone by name</h2>
          <Search contactsEndpoint={CONTACTS_ENDPOINT}/>
        </div>
      </main>
    </>
  );
}
