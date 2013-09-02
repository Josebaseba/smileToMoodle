import urllib2
import os

DOMINIO = 'moodle4.ehu.es'
CANTIDAD = 1000

def moodle(url, name):
	try:
		source = urllib2.urlopen(url).read()
	except BaseException, e:
		print "[!] Error:", e
	try:
		carpeta = "img/"
		if not os.path.isdir(carpeta):
			os.mkdir(carpeta)
		f = file(carpeta + name, "wb")
		f.write(source)
		f.close()
	except:
		print "Hubo un problema con el nombre del archivo!"
	if os.path.getsize(carpeta + name) > 10000:
		os.remove(carpeta + name)
	else:
		print name + "=> Descargado! =>", os.path.getsize("descargas/" + name), "Bytes"

for i in range(CANTIDAD):
	name = str(i) + ".jpg"
	moodle('http://' + DOMINIO + '/user/pix.php/' + str(i) + '/f1.jpg', name)
