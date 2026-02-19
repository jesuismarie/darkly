## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

---

## Step 2: Check robots.txt

Most websites expose a `robots.txt` file.

Navigate to:

```
http://<target-ip>/robots.txt
```

Contents:

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

This reveals hidden directories that should not be indexed by search engines — but are still accessible.

---

## Step 3: Explore Hidden Directory

Navigate to:

```
http://<target-ip>/.hidden
```

Inside this directory:

* Many nested subdirectories exist
* At deeper levels, there are `README` files

---

## Step 4: Search for the Flag

Because the directory structure is very large and deeply nested, manual browsing is inefficient.

Write a script to:

1. Recursively traverse all subdirectories
2. Locate all `README` files
3. Search their contents for the flag

Example approach (conceptually):

* Use `wget` or `curl` recursively
* Or write a small script to:

	* Fetch directory listing
	* Follow links
	* Check file contents

---

## Step 5: Retrieve the Flag

After scanning all nested directories and reading the `README` files, the flag is found inside one of them.

## Fix Recommendations

* Do not expose sensitive paths in robots.txt
* Implement proper access control restrictions
* Disable directory listing
* Protect hidden resources with authentication
