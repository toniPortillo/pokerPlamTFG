# pokerPlamTFG
pokerPlam: Tool for the use of the Poker technique of planning by teams that work remotely.

## Architecture components 001, designed for dependency injection, testing and use of the repository pattern

### config
Directory for application configurations and databases.

### utils
Place for different database middlewares or other and their factories. 

### models
Definitions of the models of the different databases.

### repositories
Repositories with the set of operations of the different databases to use.

### services
Set of services with bussiness logic.

### actions
Endpoints with service orchestration and route definition.

### test
Unit test directory of repositories, services and endpoints.

## Deployment

### Dockerfile

Change Dockerfile values to grant database access with this environment variables:

```
ENV MONGOHOST = <your local mongodb instance IP.>
ENV MONGOPORT = <port assigned to your local mongodb instance>
ENV SECRET = <key to generate the secret jwt token>
ENV ENV = <enviroment in which the application and database are deployed. Write DEV for development, PRO for production and TEST for test enviroment>
```

### Built With
```
docker.exe run .\Dockerfile --name poccontainer -d -p 5000:5000
```
