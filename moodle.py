import urllib2
import os

def moodle(url, name):
    try:
        source = urllib2.urlopen(url).read()
    except BaseException, e:
        print "[!] Error:", e
    try:
        f = file("descargas/" + name, "wb")
        f.write(source)
        f.close()
    except:
        print "Hubo un problema con el nombre de archivo!"
    if os.path.getsize("descargas/" + name) > 10000:
        os.remove("descargas/" + name)
    else:
        print name + "=> Descargado! =>", os.path.getsize("descargas/" + name), " bytes"

i = 0

while i < 50000:
    name = str(i) + ".jpg"
    moodle("http://moodle4.ehu.es/user/pix.php/" + str(i) + "/f1.jpg", name)
    i = i + 1
