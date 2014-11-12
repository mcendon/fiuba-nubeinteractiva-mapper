FIUBA NubeInteractiva Mapper
============================

Mapper REST de la Nube Interactiva de la FIUBA usada en TEDx UBA 2013

SETUP

1. Setup de Python 2.7.5 http://www.python.org/download/
============================

2. Setup de PIP
============================

Bajar https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py

python ez_setup.py

Bajar https://raw.github.com/pypa/pip/master/contrib/get-pip.py

python get-pip.py

Nota 1: Lo instala en C:\Python27\Scripts (p ej en Windows) Nota 2: No olvidar agregar este directorio al path de Windows (o al de Linux) para ejecutar el comando pip desde consola

3. Setup de Flask http://flask.pocoo.org/
============================

pip install Flask

4. Arrancar el servicio REST (Mapper)
============================

Windows: mapper/run.bat

Linux: mapper/run.sh

El servicio escucha en http://localhost:5000 por default 
