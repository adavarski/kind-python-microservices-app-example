## Simple python:flask microservices app (for playgrounds & LABS) 

Simple app that connects frontend with backend and acts as a microservice.
Frontend serves the backend through backend consumer. App can be run using the docker-compose file in deployment-docker or using kubernetes (kind).

## Running locally

```
cd frontend
python3 app.py

cd backend
python3 app.py
```

## Dockerization

```
docker network create pr_network
```
verify the docker network
```
docker network ls | grep pr_network
```

```
cd deployment-docker
docker-compose up --build
```


## Kubernization

```
export KUBECONFIG=output/kubeconfig.yaml
kind create cluster --name pr-k8s
```

```
docker build -t pr-be backend/
docker build -t pr-fe frontend/
```

```
kind load docker-image pr-fe --name pr-k8s
kind load docker-image pr-be --name pr-k8s

```


```
kubectl apply -f k8s
```

```
kubectl port-forward svc/pr-fe 9090:80 &

$ curl localhost:9090/
Handling connection for 9090
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Information</title>
</head>
<body>
    Product Information
    <br>
    <form action='/product' method="post">
        <label for="product">Enter product:</label><br>
        <input type="text" id="product" name="product"><br>
        <input type="submit" value="Submit">
      </form>
      <br>
      

</body>
</html>

```

changes in the code

```
docker build -t pr-fe frontend/

kind load docker-image pr-fe --name pr-k8s

kubectl rollout restart deployment/pr-fe

kubectl port-forward svc/pr-ui 9090:80 &
```

Clean:

```
kind delete cluster --name=pr-k8s

```
