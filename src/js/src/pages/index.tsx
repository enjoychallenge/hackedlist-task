import Head from "next/head";
import Search from "./../components/Search"
import Insert from "./../components/Insert"
import styles from "@/styles/Home.module.css";

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
          <Insert/>
        </div>
        <div>
          <h2>Search phone by name</h2>
          <Search/>
        </div>
      </main>
    </>
  );
}
