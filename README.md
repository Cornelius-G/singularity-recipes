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
	

## Available recipes
(will be updated)

### python2
+ Ubuntu 18.04
+ python 2.7
+ jupyter notebook
+ numpy,  scipy,  pandas, matplotlib

### python3
+ Ubuntu 18.04
+ python 3.6
+ jupyter notebook
+ numpy,  scipy,  pandas, matplotlib

### julia
+ Ubuntu 18.04
+ julia 1.1.1

### ROOT
+ Ubuntu 18.04
+ ROOT 6.16.00

### Geant4
+ Ubuntu 18.04
+ ROOT 6.16.00
+ Geant4 10.5.1