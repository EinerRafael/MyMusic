# MyMusic

Permite a los usuarios adicionar musica y playlists.

  - Utiliza Notificaciones en Tiempo Real
  - Permite Enviar Correos
  - Indexación en Motor de busqueda

Para Usarlo

```sh
$ git clone https://github.com/EinerRafael/MyMusic.git
$ cd mymusic
$ docker-compose up --build
```

Para la base de datos, en una nueva pestaña o terminal:

```sh
$ docker exec -it mymusic_web /bin/bash
# ./manage.py makemigrations
# ./manage.py migrate
```

Uso de la Aplicacion Web: /web/index

Permite interacturar con los servicios.