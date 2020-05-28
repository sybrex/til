# TIL
Today I Learned


# Deploy
```
# list of all coammands
pipenv run fab --list 

# deploy
pipenv run fab deploy --branch master --deps --hosts <host>
```

systemd
-------
```
[Unit]
Description=uWSGI instance to serve til.viktors.info
After=network.target

[Service]
User=deployer
Group=nginx
WorkingDirectory=/srv/www/til
ExecStart=/usr/local/bin/pipenv run uwsgi --ini uwsgi.ini
```

nginx
-----
```
server {
    listen 80;
    server_name til.viktors.info;

    access_log  /var/log/nginx/til.access.log;
    error_log  /var/log/nginx/til.error.log;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/srv/www/til/uwsgi.sock;
    }
}
```

Docker
------
Running mongodb container for development
```shell
docker run --name local-mongo -p 27017:27017 -d mongo:latest
```