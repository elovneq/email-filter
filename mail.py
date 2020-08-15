

liste = list()

with open("mail.txt","r",encoding="utf-8") as file:
	total = file.read()
	satır = total.count("\n")
	file.seek(0)
	
	for i in range(satır):
		a = file.readline()
		
		if a[-5:-1] == ".com" :
			try:
				if a.index("@") !=0:
					liste.append(a[:-1])
			except ValueError:
				pass		
print(liste)
