import json,requests
from os import mkdir,listdir

latestnumber = 0
folderfull = 0

print("Shibe Downloader made by @bosniandoge\n")
print("Shibe downloaded from shibe.online\n")
number = int(input("Enter how many shibe pictures u want : "))

if 'shibe' in (listdir()):
	folderfull = folderfull + 1
	print("it seems you already have a shibe folder")
else:
	print("it seems you dont have a shibe folder, it'll be created")
	mkdir('shibe',0o755)

def listshibe():
	print(folderfull)
	if folderfull == 1:
		numbering = []
		for file in listdir('shibe'):
			numbering.append(int(file[6:-4]))
		print(numbering)
		numbering.sort()
		return (numbering[-1])



for i in range(0,number):
	url = 'https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true'
	r = requests.get(url)
	dogeurl = r.content
	urlsecond = dogeurl[2:-2].decode('utf-8')
	#print(urlsecond)
	g = requests.get(urlsecond)
	filename = ''
	if folderfull == 1:
		latestnumber = listshibe()
		filename = 'shibe-' + str(latestnumber + 1)
		print('Shiba ' + str(latestnumber+1) + ' downloaded')
	elif folderfull == 0:
		filename = 'shibe-' + str(i+1)
		print('Shiba ' + str(i+1) + ' downloaded')
	open('shibe/' + filename + '.jpg', 'wb').write(g.content)

print(str(number) + ' shibe have been downloaded')
