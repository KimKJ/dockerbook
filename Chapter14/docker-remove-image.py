import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
c.remove_image('nginx:latest')
