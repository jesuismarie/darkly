## Step 1: Open the Website

Open the target application in your browser:

```
http://<target-ip>
```

Click the **Survey** button to access the voting page.

---

## Step 2: Understand the Survey Page

The page displays a table with the following columns:

```
Grade | Average | Subject | Nb of vote (indicative)
```

Each row contains a dropdown menu allowing you to select a grade (1–10).

---

## Step 3: Inspect the Page Source

Right-click on the page and select **Inspect** (Developer Tools).

You will find the following HTML structure for each survey entry:

```html
<td align="center">
	<form action="#" method="post">
		<input type="hidden" name="sujet" value="2">
		<select name="valeur" onchange="javascript:this.form.submit();">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
		</select>
	</form>
</td>
```

---

## Step 4: Manipulate the Input Value

Edit one of the `<option>` values in the HTML.
For example, change:

```
<option value="10">10</option>
```

to:

```
<option value="999">999</option>
```

Now select this modified option from the dropdown.

---

## Step 5: Submit & Get the Flag

When the form auto-submits, the server accepts the tampered value.

The flag is immediately displayed.

## Fix Recommendations

* Validate all input values server-side
* Enforce allowed ranges (e.g., 1–10)
* Reject unexpected or tampered parameters
