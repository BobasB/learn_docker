# learn_docker
Contain examples with Dockerfiles/Docker and Python3.
- compatible with MacOS/Linux;
- [DockerHub repository](https://cloud.docker.com/repository/registry-1.docker.io/bobas/learn_docker)
- Useful links [Docker Labs](https://github.com/docker/labs/tree/master/beginner) 

### Simple Dockerfile
- build/tag/push simple Docker example with Python app:
```bash
make 1_create_dockerfile
```
- test if it works:
```bash
make example_1
```

### Web app with Docker
WE will use simple [Flask](https://palletsprojects.com/p/flask/) web server.
- build/tag/push image with Flask app:
```bash
make 2_web_in_docker
```
- test if it works, execute and open 'http://localhost:5000' in browser. CNTR+C to stop container:
```bash
make example_2
```