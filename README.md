# til
Today I Learned

systemd
-------
[Unit]
Description=uWSGI instance to serve til.viktors.info
After=network.target

[Service]
User=deployer
Group=nginx
WorkingDirectory=/srv/www/til
ExecStart=/usr/local/bin/pipenv run uwsgi --ini uwsgi.ini

[Install]
WantedBy=multi-user.target

Docker
------
Running mongodb container
```shell
docker run --name local-mongo -p 27017:27017 -d mongo:latest
```