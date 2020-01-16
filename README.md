# Singularity-recipes
This repository collects recipes for building singularity containers.  
Currently singularity definition files and Dockerfiles are available, though Dockerfiles should be the preferred way for building the containers.   
The python script `dockerfile2sif.py` helps to locally build a `.sif` singularity image from a Dockerfile (i.e. without using dockerhub).


## Building a singularity container from a singularity definition file
`sudo singularity build image.sif definitionfile.def`

## Building a singularity container from a Dockerfile
The `dockerfile2sif.py` script allows to create a .sif singularity container from a Dockerfile.  
(A docker installation is needed for this.)
Run the script via:  
```
python dockerfile2sif.py /path-to-Dockerfile image-name
```

The singularity image will be created using a temporary .tar version of the docker image that will automatically be deleted.
For creating the image, 'sudo' privileges are needed.

## Run singularity containers
For an interactive shell session:  
`singularity shell image.sif` 

To run a specific command:  
`singularity exec image.sif command`

## Run jupyter notebooks inside a container 
To run a jupyter notebook you need to pass the `--bind` option to tell singularity where to write temporary session data.  
So for example you can run a notebook directly using:  
`singularity exec --bind /tmp:/run/user python2.sif jupyter notebook`  

Or using the interactive shell:  
1. `singularity shell --bind /tmp:/run/user python2.sif`  
2. `jupyter notebook`
	

## Tips when running docker & singularity on a system with little memory
Change singularity cache and tmp directories:
`SINGULARITY_TMPDIR` and  
`SINGULARITY_CACHEDIR`

Clean singularity cache:
`sudo singularity cache clean`

Clean Docker:
`sudo docker system prune`
or
`sudo docker image prune` and `sudo docker contaienr prune`
