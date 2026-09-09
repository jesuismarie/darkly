## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

Click the **Add Image** button to access the image upload page.

---

## Step 2: Intercept the Upload Request

1. Start **Burp Suite**
2. Configure your browser proxy
3. Enable **Intercept** in the Proxy tab
4. Attempt to upload a non-image file

Burp will capture the upload request.

---

## Step 3: Send to Repeater

1. Right-click the intercepted request
2. Select **Send to Repeater**

---

## Step 4: Modify the Content-Type Header

Locate the file upload part in the HTTP request.

Change the file’s `Content-Type` header from its original value (e.g., `text/plain` or `application/octet-stream`) to:

```
Content-Type: image/jpeg
```

Even if the file is not actually an image.

---

## Step 5: Send the Modified Request

Click **Send** in Repeater.

The server accepts the file because it only checks the `Content-Type` header instead of validating the actual file content.

The flag is then returned in the response.

## Fix Recommendations

* Validate file type server-side using MIME detection
* Verify file signatures (magic bytes)
* Restrict allowed file extensions
* Store uploaded files outside the web root
