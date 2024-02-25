# Python Flask Real Estate Template

## To create a virtual environment, you can use the following commands:

### Navigate to your project directory

> cd  [project_directory]

### Create a virtual environment

> python -m venv venv

### Use localhost on 5000 port to access:
> http://localhost:5000

## Activate the virtual environment (commands might vary based on your operating system)

### On Windows

> venv\Scripts\activate

### On macOS/Linux

> source venv/bin/activate

## Dockerfile for Container Env.

### Refer Dockerfile & requirements.txt for container image creation.  
created user **'myuser'** for ownership of the working directory to the non-root user. 

### Docker commands:
- Build Docker image:  
    > docker build -t <image_name> .
- Run Docker container & access via 'http://localhost:5000' :
    > docker run -p 5000:5000 <image_name>  
- Login to container:
    > docker exec -it <container_id> /bin/bash
- If using non root user within the container:
    > docker exec -it <container_id> su - myuser
- remove all docker container by image name and delete docker image:  
    (stop running container before running)  
    > docker ps -a | grep <image_name>  | awk '{print $1}' | xargs docker rm  
    > docker rmi <image_name> 

---