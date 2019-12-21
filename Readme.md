## Phrabasy

Python Application Desktop to register phrases by situation en English:

Using:
- Tkinder (python library)
- SQLLite
- DB Browser for SQLlite

### Run Phrabasy:
```shell-script
    python3 index.py
```

### Using Docker Image

### Build Dockerfile
```shell-script
    docker build -t phrases_desktop .
```
### Run the container

```shell-script
    docker run -ti --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    phrases_desktop
```