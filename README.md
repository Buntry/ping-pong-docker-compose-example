# docker compose example

ping - pong example with docker containers and compose

app consists of 2 apis, pinger which can be found at http://localhost:3000/ping
and ponger which can be found at http://localhost:3010/pong. The pinger will call
the ponger and report back the number of milliseconds it took.

to run the project, ensure you have docker and docker-compose installed locally and
that the docker daemon is running. all you need to do from there is run 

```
$ docker-compose up --build
```

and the app should build and run automatically.