---
title: Docker Quick Notes
---

**Docker** is a platform that allows you to package an application and all of its requirements into a single unit called a **container**.

# What Docker is used for

- **Consistency Across Environments:** Ensuring that code runs the same on a developer's laptop, a testing server, and the cloud.
- **Microservices Architecture:** Breaking down large, monolithic applications into smaller, independent services that communicate with each other.
- **Isolation:** Running multiple applications with conflicting dependencies (e.g., two different versions of Python) on the same physical machine without them interfering with one another.
- **Rapid Deployment:** Speeding up the "build, ship, and run" cycle because containers are lightweight and start in seconds compared to virtual machines.
- **Simplified Scaling:** Easily spinning up more copies (instances) of a container to handle increased web traffic.
- **CI/CD Integration:** Automating the testing and deployment process by providing a clean, predictable environment for every code change.

# Dockerfile

Basic dockerfile example

```
# Base image
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Copy dependency files first (cache layer)
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN npm install -g pnpm && pnpm install --frozen-lockfile

# Copy source code
COPY . .

# Build
RUN pnpm build

# Production stage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
USER node
CMD ["node", "dist/index.js"]
```

|Instruction|Purpose|
|---|---|
|`FROM`|Base image|
|`WORKDIR`|Set working directory|
|`COPY`|Copy files from host|
|`ADD`|Copy + extract archives / fetch URLs|
|`RUN`|Execute command during build|
|`CMD`|Default command when container starts|
|`ENTRYPOINT`|Fixed command (CMD becomes arguments)|
|`EXPOSE`|Document which port the app uses|
|`ENV`|Set environment variable|
|`ARG`|Build-time variable|
|`VOLUME`|Create mount point|
|`USER`|Switch to non-root user|
|`HEALTHCHECK`|Define health check command|
# Containers
|Command|Description|
|---|---|
|`docker run <image>`|Run a container|
|`docker run -d <image>`|Run in background (detached)|
|`docker run -it <image> /bin/sh`|Run interactive shell|
|`docker run --name myapp <image>`|Run with a custom name|
|`docker run -p 8080:80 <image>`|Map host port 8080 → container port 80|
|`docker run -v ./data:/app/data <image>`|Mount a volume|
|`docker run -e MY_VAR=value <image>`|Set environment variable|
|`docker run --env-file .env <image>`|Load env vars from file|
|`docker run --rm <image>`|Auto-remove container when it stops|
|`docker run --restart unless-stopped <image>`|Auto-restart on failure|
|`docker ps`|List running containers|
|`docker ps -a`|List all containers (including stopped)|
|`docker stop <container>`|Stop a container|
|`docker start <container>`|Start a stopped container|
|`docker restart <container>`|Restart a container|
|`docker rm <container>`|Remove a stopped container|
|`docker rm -f <container>`|Force remove (even running)|
|`docker exec -it <container> /bin/sh`|Shell into a running container|
|`docker exec <container> <command>`|Run a command in a container|
|`docker cp <container>:/path ./local`|Copy file from container to host|
|`docker cp ./local <container>:/path`|Copy file from host to container|
|`docker rename <old> <new>`|Rename a container|
|`docker stats`|Live resource usage for all containers|
|`docker top <container>`|Show processes in a container|
|`docker inspect <container>`|Full JSON details of a container|


- Normally if you run a container without options it will start and stop immediately, if you want keep it running you can use the command, `docker run -td container_id` this will use the option `-t` that will allocate a pseudo-TTY session and `-d` that will detach automatically the container (run container in background and print container ID).
- If you want a transient container, `docker run --rm` will remove the container after it stops.
- If you want to remove also the volumes associated with the container, the deletion of the container must include the `-v` switch like in `docker rm -v`.
- Another useful option is `docker run --name yourname docker_image` because when you specify the `--name` inside the run command this will allow you to start and stop a container by calling it with the name the you specified when you created it.

# Images

|Command|Description|
|---|---|
|`docker images`|List local images|
|`docker pull <image>`|Pull image from registry|
|`docker pull <image>:<tag>`|Pull specific tag|
|`docker build -t myapp .`|Build image from Dockerfile|
|`docker build -t myapp:v1 .`|Build with tag|
|`docker build -f Dockerfile.prod .`|Build with custom Dockerfile|
|`docker build --no-cache .`|Build without cache|
|`docker tag <image> <new-name>:<tag>`|Tag an image|
|`docker rmi <image>`|Remove an image|
|`docker image prune`|Remove dangling images|
|`docker image prune -a`|Remove all unused images|
|`docker history <image>`|Show image layers|
|`docker save -o backup.tar <image>`|Export image to tar|
|`docker load -i backup.tar`|Import image from tar|

# Volumes

|Command|Description|
|---|---|
|`docker volume create mydata`|Create a named volume|
|`docker volume ls`|List volumes|
|`docker volume inspect mydata`|Volume details|
|`docker volume rm mydata`|Remove a volume|
|`docker volume prune`|Remove all unused volumes|
|`docker run -v mydata:/app/data <image>`|Mount named volume|
|`docker run -v $(pwd)/data:/app/data <image>`|Bind mount (host dir)|
|`docker run -v /app/node_modules <image>`|Anonymous volume|
|`docker run --mount type=tmpfs,target=/tmp <image>`|tmpfs mount (RAM)|

# Networks

|Command|Description|
|---|---|
|`docker network ls`|List networks|
|`docker network create mynet`|Create a network|
|`docker network inspect mynet`|Network details|
|`docker network rm mynet`|Remove a network|
|`docker network connect mynet <container>`|Connect container to network|
|`docker network disconnect mynet <container>`|Disconnect from network|
|`docker run --network mynet <image>`|Run container on a specific network|
|`docker network prune`|Remove unused networks|
# Docker Compose

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

|Command|Description|
|---|---|
|`docker compose up`|Start all services|
|`docker compose up -d`|Start in background|
|`docker compose up --build`|Rebuild images + start|
|`docker compose down`|Stop + remove containers|
|`docker compose down -v`|Stop + remove containers + volumes|
|`docker compose ps`|List running services|
|`docker compose logs`|View logs for all services|
|`docker compose logs -f <service>`|Follow logs for one service|
|`docker compose exec <service> /bin/sh`|Shell into a service|
|`docker compose build`|Build all images|
|`docker compose pull`|Pull latest images|
|`docker compose restart <service>`|Restart a single service|
|`docker compose stop`|Stop without removing|
|`docker compose config`|Validate and view merged config|
|`docker compose --profile debug up`|Start with a specific profile|

- Starting the application
```
docker-compose -f <docker-compose-file> up
```
- You can also run docker-compose in detached mode using -d flag, then you can stop it whenever needed by the following command:
```
docker-compose stop
```
## Basic `docker-compose.yml` example

```
services:
  app:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - ./src:/app/src
    environment:
      - NODE_ENV=development
    depends_on:
      - db

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  pgdata:
```

# Buildx & Multi-platform

|Command|Description|
|---|---|
|`docker buildx create --use`|Create + activate a new builder|
|`docker buildx ls`|List builders|
|`docker buildx build --platform linux/amd64,linux/arm64 -t myapp .`|Multi-platform build|
|`docker buildx build --push -t user/myapp .`|Build + push in one step|
|`docker buildx build --cache-from type=registry,ref=user/myapp:cache .`|Use registry cache|
|`docker buildx prune`|Clean build cache|

# Cleanup & Maintenance

|Command|Description|
|---|---|
|`docker system df`|Show disk usage|
|`docker system prune`|Remove stopped containers + dangling images + unused networks|
|`docker system prune -a`|Remove ALL unused data|
|`docker system prune -a --volumes`|Nuclear option — remove everything unused|
|`docker container prune`|Remove stopped containers|
|`docker image prune -a`|Remove unused images|
|`docker volume prune`|Remove unused volumes|
|`docker builder prune`|Remove build cache|
# Installation

## Windows

Instructions to install Docker Desktop for Windows can be found [here](https://docs.docker.com/desktop/windows/install/)

**Check version**

```
# Display the version of docker installed:
docker version

# Pull, create, and run 'hello-world':
docker run hello-world

$ docker version --format '{{.Server.Version}}'
1.8.0

$ docker version --format '{{json .}}'
{"Client":{"Version":"1.8.0","ApiVersion":"1.20","GitCommit":"f5bae0a","GoVersion":"go1.4.2","Os":"linux","Arch":"am"}
```
Additionally, if you have WSL or WSL2 installed on your desktop, you might want to install the Linux Kernel for Windows. Instructions can be found [here](https://techcommunity.microsoft.com/t5/windows-dev-appconsult/using-wsl2-in-a-docker-linux-container-on-windows-to-run-a/ba-p/1482133). This requires the Windows Subsystem for Linux feature. This will allow for containers to be accessed by WSL operating systems, as well as the efficiency gain from running WSL operating systems in docker. It is also preferred to use [Windows terminal](https://docs.microsoft.com/en-us/windows/terminal/get-started) for this.


# Useful One-Liners

```
# Stop all running containers
docker stop $(docker ps -q)

# Remove all stopped containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

# Get container IP
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>

# Enter the last started container
docker exec -it $(docker ps -lq) /bin/sh

# Show container resource usage (sorted by memory)
docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}\t{{.CPUPerc}}"

# Export all container logs to a file
docker logs <container> > container.log 2>&1

# Run a quick throwaway container
docker run --rm -it alpine /bin/sh
```

# Other notes

## Check version

```
# Display the version of docker installed:
docker version

# Get server version
$ docker version --format '{{.Server.Version}}'
1.8.0

# dump raw JSON data
$ docker version --format '{{json .}}'
{"Client":{"Version":"1.8.0","ApiVersion":"1.20","GitCommit":"f5bae0a","GoVersion":"go1.4.2","Os":"linux","Arch":"am"}
```


## Exposing ports

```
docker run -p 127.0.0.1:$HOSTPORT:$CONTAINERPORT \
  --name CONTAINER \
  -t someimage
```


Expose ports at compose.yml

```
EXPOSE <CONTAINERPORT>
```

Note that `EXPOSE` does not expose the port itself - only `-p` will do that.

To expose the container's port on your localhost's port, run:
```
iptables -t nat -A DOCKER -p tcp --dport <LOCALHOSTPORT> -j DNAT --to-destination <CONTAINERIP>:<PORT>
```

If you forget what you mapped the port to on the host container, use `docker port` to show it:

```
docker port CONTAINER $CONTAINERPORT
```




# References
- [atryx/docker-cheatsheet: Docker commands cheat sheet — containers, images, volumes, networks, Compose, and Buildx in one place (2026)](https://github.com/atryx/docker-cheatsheet)
- [wsargent/docker-cheat-sheet: Docker Cheat Sheet](https://github.com/wsargent/docker-cheat-sheet)
- [Everyday Hacks for Docker | Codefresh](https://codefresh.io/blog/everyday-hacks-docker/)