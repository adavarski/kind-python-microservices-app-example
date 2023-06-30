### Deployment

```
docker network create pr_network

# verify the docker network
docker network ls | grep pr_network

cd deployment-docker

docker-compose up --build
```

