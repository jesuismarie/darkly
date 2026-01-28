## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

Scroll to the bottom of the page.

---

## Step 2: Identify Redirect Buttons

At the end of the page, there are **three buttons** that redirect users to external websites (e.g., social media).

Click one of them while intercepting traffic.

---

## Step 3: Intercept the Request with Burp Suite

1. Open **Burp Suite**
2. Enable **Intercept** in the Proxy tab
3. Click one of the redirect buttons

You will capture a request similar to:

```
GET /index.php?page=redirect&site=facebook HTTP/1.1
Host: 192.168.5.17
```

---

## Step 4: Send to Repeater

In Burp:

1. Right-click the intercepted request
2. Select **Send to Repeater**

---

## Step 5: Manipulate the Redirect Parameter

In Repeater, modify the `site` parameter:

```
GET /index.php?page=redirect&site=test HTTP/1.1
```

Send the modified request.

---

## Step 6: Get the Flag

The application accepts the arbitrary value for the `site` parameter.

Instead of validating allowed destinations, it processes the request and reveals the flag.
