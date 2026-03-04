## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

Click the **Sign In** button to reach the login page.

---

## Step 2: Set Up Burp Suite

1. Launch **Burp Suite**
2. Configure your browser to use Burp as a proxy
3. Turn **Intercept** ON
4. Submit a login attempt to capture the request

---

## Step 3: Send Request to Intruder

In Burp:

1. Right-click the captured login request
2. Select **Send to Intruder**
3. Go to the **Intruder** tab

---

## Step 4: Configure the Attack

1. Set the **password** parameter as a variable (payload position)
2. Load a **password wordlist** into the Payloads tab
3. Choose **Attack Type**: `Sniper`
4. Start the attack

---

## Step 5: Identify the Correct Password

Monitor the Intruder results.

Look for the response with:

* Different **length**
* Different **response received**

The password with the **maximum response length** indicates a successful login.

---

## Step 6: Login as Admin

Use the discovered credentials:

```
Username: admin  
Password: shadow
```

---

## Step 7: Get the Flag

After successful login, the flag is displayed on the page.

## Fix Recommendations

* Implement rate limiting on login attempts
* Add account lockout after multiple failures
* Use strong password policies
* Monitor and alert on suspicious login activity
