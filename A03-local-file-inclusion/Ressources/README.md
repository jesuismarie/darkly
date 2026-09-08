## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

---

## Step 2: Identify the File Inclusion Parameter

Observe that the application uses a `page` parameter to load content dynamically:

```
http://<target-ip>/?page=xxxx
```

This indicates a potential file inclusion vulnerability.

---

## Step 3: Test for Directory Traversal

Attempt to traverse directories to access a sensitive system file:

```
http://<target-ip>/?page=../../../../../../../etc/passwd
```

---

## Step 4: Analyze the Response

The application returns an alert message.

This confirms:

* The input is being processed by the server
* Directory traversal is possible
* You are on the right exploitation path

---

## Step 5: Adjust the Payload

Increase the number of `../` sequences to reach the root directory correctly.

For example:

```
http://<target-ip>/?page=../../../../../../../../../../../../../../../../etc/passwd
```

---

## Step 6: Get the Flag

After reaching the correct path depth, the application loads the targeted file.

The flag is then displayed in the response.

## Fix Recommendations

* Never include files based on raw user input
* Implement strict allowlists for file names
* Normalize and validate file paths server-side
* Disable directory traversal sequences (../)
* Use fixed routing instead of file-based includes
