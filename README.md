# learn_docker
Contain examples with Dockerfiles/Docker and Python3.
- compatible with MacOS/Linux;

### Simple Dockerfile
- build/tag/push simple Docker example with Python app:
```bash
make 1_Create_Dockerfile
```
- test if it works:
```bash
make example_1
```

### Web app with Docker
- build/tag/push image with Flask app:
```bash
make 2_web_in_docker
```
- test if it works, execute and open 'http://localhost:5000' in browser. CNTR+C to stop container:
```bash
make example_2
```