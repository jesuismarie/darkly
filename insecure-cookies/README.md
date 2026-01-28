## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

---

## Step 2: Inspect Cookies

1. Open **Developer Tools**
2. Navigate to the **Storage** (or **Application**) tab
3. Open the **Cookies** section

You will find a cookie named:

```
I_am_admin
```

---

## Step 3: Analyze the Cookie Value

Check the value of the cookie:

```
68934a3e9455fa72420237eb05902327
```

---

## Step 4: Identify the Hash Type

Use `hash-identifier` on the hash part:

```
hash-identifier 68934a3e9455fa72420237eb05902327
```

**Result:**
-> MD5

---

## Step 5: Forge an Admin Cookie

1. Take the logical opposite of `false` → `true`
2. Hash `true` using **MD5**

Replace the cookie value with the MD5 hash of `true`.

---

## Step 6: Update Cookie & Refresh

1. Edit the `I_am_admin` cookie value in Developer Tools
2. Refresh the page

---

## Step 7: Get the Flag

After refreshing with the forged admin cookie, the application grants admin access and displays the flag.
