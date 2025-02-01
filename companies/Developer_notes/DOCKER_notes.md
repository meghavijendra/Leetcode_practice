DOCKER

-> Docker is a platform for building running and shipping applications in a consistent manner so if your application works on your development machine it can run and function the same way on other machines.
-> Docker is an open-source platform that automates the deployment, scaling, and management of applications using containerization. Containers are lightweight, portable, and self-sufficient environments that include everything needed to run a piece of software, including the code, runtime, libraries, and system tools.

-> Key Concepts:
1. Containers: Containers are isolated environments that run applications. They share the host system's kernel but have their own filesystem, network interfaces, and process space. This makes them lightweight and efficient compared to traditional virtual machines.

2. Images: Docker images are read-only templates used to create containers. An image includes the application code, libraries, dependencies, and other files needed to run the application. Images are built from a Dockerfile.

3. Dockerfile: A Dockerfile is a text document that contains a series of instructions to build a Docker image. Each instruction in a Dockerfile creates a new layer in the image.

4. Docker Hub: Docker Hub is a cloud-based repository where Docker users can store and share Docker images. It provides a centralized resource for finding and distributing container images.

5. Docker Engine: Docker Engine is the runtime that enables containers to run on a host operating system. It includes the Docker daemon, which manages containers, images, networks, and storage volumes.


-> Docker Engine or Docker is the base engine installed on your host machine to build and run containers using Docker components and services
* It uses a client-server architecture
* Docker Client and Server communicate using Rest API
What happens here?
* Docker Client is a service which runs a command.
The command is translated using REST API and is sent to the Docker Daemon (server)
* Then, Docker Daemon checks the client request and interacts with the operating system in order to create or manage containers

-> Basic Docker Commands:
1. Build an Image: docker build -t <image_name>:<tag> 
2. Run a Container: docker run -d --name <container_name> <image_name>:<tag>
3. List Running Containers: docker ps
4. Stop a Container: docker stop <container_id>
5. Remove a Container: docker rm <container_id>
6. List Images: docker images
7. Remove an Image: docker rmi <image_id>

-> Example Dockerfile:
# Use the official Ubuntu base image
FROM ubuntu:latest
# Update the package list and install Python 3
RUN apt-get update && apt-get install -y python3
# Copy the current directory contents into the container at /app
COPY . /app
# Set the working directory to /app
WORKDIR /app
# Run app.py when the container launches
CMD ["python3", "app.py"]

-> Workflow:
1. Write a Dockerfile: Define the environment and application dependencies.
2. Build an Image: Use the Dockerfile to build an image.
3. Run a Container: Create and start a container from the image.
4. Share the Image: Push the image to Docker Hub or another registry for sharing.

-> Docker simplifies the development and deployment process by ensuring that applications run consistently across different environments.

-> Docker is particularly helpful for full stack web applications due to its ability to create consistent, isolated environments for each component of the application. Here are some key benefits:
1. Consistency Across Environments:
Docker ensures that the application runs the same way in development, testing, and production environments. This eliminates the "it works on my machine" problem.
2. Isolation:
Each component of a full stack application (e.g., frontend, backend, database) can run in its own container. This isolation prevents conflicts between dependencies and allows each component to be managed independently.
3. Scalability:
Docker makes it easy to scale individual components of the application. For example, you can scale the backend API by running multiple instances of the backend container behind a load balancer.
4. Simplified Dependency Management:
Docker containers include all the dependencies needed to run the application. This simplifies dependency management and ensures that the correct versions of libraries and tools are used.
5. Portability:
Docker containers can run on any system that supports Docker, making it easy to move applications between different environments and cloud providers.
6. Efficient Resource Utilization:
Docker containers share the host system's kernel and resources, making them more lightweight and efficient compared to traditional virtual machines.
7. Version Control for Environments:
Docker images can be versioned and stored in repositories like Docker Hub. This allows you to track changes to the environment and roll back to previous versions if needed.

-> Example Use Case for a Full Stack Web Application:
1. Dockerfile for .NET Core Backend:
# Use the official .NET SDK image to build the application
FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
# Set the working directory
WORKDIR /app
# Copy the project file and restore dependencies
COPY *.csproj ./
RUN dotnet restore
# Copy the rest of the application code
COPY . .
# Build the application
RUN dotnet publish -c Release -o out
# Use the official .NET runtime image to run the application
FROM mcr.microsoft.com/dotnet/aspnet:5.0
# Set the working directory
WORKDIR /app
# Copy the built application from the build stage
COPY --from=build /app/out .
# Expose the application port
EXPOSE 80
# Start the application
ENTRYPOINT ["dotnet", "YourAppName.dll"]

2. Dockerfile for React Frontend:
# Use the official Node.js base image
FROM node:14
# Set the working directory
WORKDIR /app
# Copy package.json and install dependencies
COPY package.json ./
RUN npm install
# Copy the rest of the application code
COPY . .
# Build the application
RUN npm run build
# Use a lightweight web server to serve the static files
FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html
# Expose the application port
EXPOSE 80
# Start the web server
CMD ["nginx", "-g", "daemon off;"]

3. Docker Compose for Multi-Container Setup:
version: '3'
services:
  frontend:
    build: ./frontend
    ports:
      - "80:80"
  backend:
    build: ./backend
    ports:
      - "80:80"
    environment:
      - ASPNETCORE_ENVIRONMENT=Development
      - ConnectionStrings__DefaultConnection=Server=database;Database=mydb;User Id=sa;Password=YourStrong!Passw0rd;
  database:
    image: mcr.microsoft.com/mssql/server:2019-latest
    environment:
      SA_PASSWORD: "YourStrong!Passw0rd"
      ACCEPT_EULA: "Y"
    ports:
      - "1433:1433"

Workflow:
1. Write Dockerfiles: Define the environment and dependencies for each component (frontend, backend, database).
2. Build Images: Use the Dockerfiles to build images for each component.
3. Run Containers: Use Docker Compose to start and manage the containers.
4. Develop and Test: Develop and test the application in a consistent environment.
5. Deploy: Deploy the application to production using the same Docker images.

Example Directory Structure:
/your-project
|-- /frontend
|   |-- Dockerfile
|   |-- package.json
|   |-- src/
|
|-- /backend
|   |-- Dockerfile
|   |-- YourAppName.csproj
|   |-- Program.cs
|   |-- Startup.cs
|   |-- ...
|
|-- docker-compose.yml

Explanation:
~ Frontend Service: Builds and serves the React application using Node.js and Nginx.
~ Backend Service: Builds and runs the .NET Core application.
~ Database Service: Runs Microsoft SQL Server with the specified environment variables for the SA password and EULA acceptance.
This setup ensures that each component of your full stack application runs in its own isolated environment, making it easier to manage dependencies, scale components, and maintain consistency across different environments.

-> Containers are best suited for applications that require fast startup times, efficient resource usage, and easy scalability. They are ideal for microservices architectures and cloud-native applications.
-> Virtual Machines are better suited for scenarios where strong isolation is needed, or when running multiple different operating systems on the same hardware. They are useful for legacy applications and environments that require full OS-level isolation.

-> Comman to build the image from dockerfile:
docker build -t my-app .

-> to view all docker images:
docker image ls

-> to run the image:
docker run my-app
