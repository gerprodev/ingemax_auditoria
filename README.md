# Django - Docker
Aplicación de Auditoria de Ingemax


## Instalación de Docker (Ubuntu 16.04)
```sh
sudo apt-get update
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
sudo apt-get update
apt-cache policy docker-engine
sudo apt-get install -y docker-engine
sudo usermod -aG docker $(whoami)
```
Note: For Windows 7 Pro - Mac OS X use Docker Toolbox.

## Construir contenedor
```sh
sudo docker build -t ingemax-p3:latest .
sudo docker run -d --name=ingemax-auditoria --restart=unless-stopped --network=ingemax_network -e APP_NAME=ingemax_auditoria -v /srv:/srv -p 9000:8000 ingemax-p3:latest
```

## Conectarse al contenedor
```sh
sudo docker exec -it ingemax-auditoria /bin/bash
supervisorctl status/stop/start/restart app
```

## Modo de uso
Copiar la aplicación "auditoria" al proyecto, y agregar las variables, el middleware y configurar el nombre de la instancia:
```python
from auditoria.variables import *

MIDDLEWARE = [
	'...',
	'auditoria.middleware.ControlPeticionesMiddleware',
]

AUDITORIA_INSTANCIA_ID = 'Nombre instancia'
```