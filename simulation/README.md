## Run

```
docker run -v ./capture:/capture -p 8080:80 -it $(docker build -q .)
```
