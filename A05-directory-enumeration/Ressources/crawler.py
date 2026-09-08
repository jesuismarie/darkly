#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep

def crawl(url):
	try:
		html = requests.get(url, timeout=7).text
	except:
		return

	soup = BeautifulSoup(html, "html.parser")

	for a in soup.find_all("a", href=True):
		href = a["href"]
		if href in ("../", ".."):
			continue

		full = urljoin(url, href)

		if href.lower() == "readme":
			try:
				text = requests.get(full, timeout=7).text
				if "flag" in text.lower():
					with open("flag.txt", "w", encoding="utf-8") as f:
						f.write(text)
					exit("Flag saved → flag.txt")
			except:
				pass

		elif href.endswith("/"):
			crawl(full)

crawl("http://10.113.231.80/.hidden/")
