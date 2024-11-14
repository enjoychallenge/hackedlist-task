import Head from "next/head";
import Search from "./../components/Search"
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
          <h2>Search phone by name</h2>
          <Search/>
        </div>
      </main>
    </>
  );
}
