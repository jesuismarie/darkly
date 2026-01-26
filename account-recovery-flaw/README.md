## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

---

## Step 2: Go to Sign In

Click the **Sign In** button.

On the login page, select:

```
"I forgot my password"
```

---

## Step 3: Inspect the Page

Right-click anywhere on the page and choose **Inspect** (Developer Tools).

Look for a hidden input field in the password recovery form:

```html
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

---

## Step 4: Modify Hidden Field

Edit the hidden input field directly in the browser and replace the email value with any other email:

```
test@test.com
```

---

## Step 5: Submit & Get the Flag

Submit the password recovery form.

The application accepts the modified hidden field and immediately reveals the flag.
