## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

Click the **Leave a Feedback** button to access the feedback page.

---

## Step 2: Test Basic XSS Payload

Try submitting a simple payload in the feedback message:

```html
<script>alert("XSS")</script>
```

**Result:**

```html
<table>
	<tbody style="border:medium none black;border-style:double double double double;">
	<tr>
		<td>Name : xss</td>
	</tr>
	<tr>
		<td>Comment : alert(\"XSS\")</td>
		</tr>
	</tbody>
</table>
```

This indicates:

* The server strips tags
* Basic filtering is applied
* The content inside the tags is preserved.
* Quotes are escaped (`\"`).
* The input is reflected inside an HTML `<td>` element (HTML body context), not inside a `<textarea>`.

---

## Step 3: Attempt Filter Bypass

Since basic `<script>` tags are stripped, attempt to bypass the weak filtering mechanism by injecting a payload that avoids simple pattern-based filtering:

```
" ><script>alert("XSS")</script>
```

Although the input is reflected inside an HTML `<td>` element (body context), the filtering mechanism appears to rely on simple pattern matching.
By adding extra characters before the `<script>` tag, the filter fails to properly sanitize the input, allowing the injected `<script>` tag to execute.

---

## Step 4: Get the Flag

After submitting the crafted payload, the script executes successfully.

The flag is then displayed.
