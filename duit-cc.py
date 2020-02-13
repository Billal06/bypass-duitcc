# Copyright 2020 BILLAL FAUZAN
# Saya Bersumpah Tidak Akan Mengedit Ini tanpa seizin author
# Belajar Lah Sedikit demi sedikit
# Jangan Recode Mulu -_

import requests
from bs4 import BeautifulSoup as bs

def bypass(url):
	data = []
	r = requests.get(url)
	if r.status_code == 200:
		b = bs(r.text, "html.parser")
		for a in b.findAll("input"):
			if "geturl" == a.get("name"):
				data.append(a["value"])
	if len(data) > 0:
		print ("[STATUS]> berhasil di bypass")
		print ("[RESULT]> "+data[0])

def main():
	print ("        [  BYPASS DUIT CC  ]")
	print ("           [ BY BILLAL ]")
	url = input("LINK: ")
	bypass(url)

main()
