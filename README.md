moodlePhoto
===========

Descargar fotos de los usuarios registrados en cualquier Moodle.

Este pequeño script escrito en Python permite descargar todas las fotos de perfil de los usuarios de Moodle. No hace falta estar registrado en ningún moodle para ver la foto de perfil de los usuarios, no me hago cargo del mal uso de este script. Las fotos estan colgadas de forma que cualquiera puede acceder a ellas, yo solo lo he automatizado.

Esta puesto como defecto que descargue del Moodle de la UPV, cambiando la ruta por la de cualquier otro Moodle funciona.

  USO
========

1 - Descargamos el Script

2 - Creamos al lado del script la carpeta descargas

3 - En caso de querer cambiar de Moodle, solo cambiamos la primera parte de la URL. Es decir, la parte http://moodle4.ehu.es se sustituye por la ruta que sea. Lo demas -> /user/pix.php/ etc. no se toca en ningún caso.

4 - Cambiamos el número de iteraciones del While dependiendo de la cantidad de usuarios que estimemos que haya en el Moodle.

5 - Doble click sobre el script y listo, en la consola te irán saliendo que fotos se han descargado y se guardarán en la carpeta descargas.

==

La velocidad de descarga dependera en gran parte de nuestra conexión, el tamaño de cada imagen ronda los 5kb.
