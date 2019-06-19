# Singularity-recipes
This repository is a collection of my recipes for building singularity containers.

## Available recipes

### python2
+ Ubuntu 18.04
+ python 2.7
+ jupyter notebook
+ numpy,  scipy,  pandas, matplotlib

### python3
+  Ubuntu 18.04
+ python 3.6
+ jupyter notebook
+ numpy,  scipy,  pandas, matplotlib

### julia
+  Ubuntu 18.04
+ julia 1.1.1

## Building the container
`sudo singularity build python2.sif python2.def`

## Runing singularity images
For an interactive shell session:  
`singularity shell image.sif` 

To run a specific command:  
`singularity exec image.sif command`

## Run jupyter notebooks (for python2 & python3): 
To run a jupyter notebook you need to pass the `--bind` option to tell singularity where to write temporary session data.  
So for example you can run the notebook directly using:  
`singularity exec --bind /tmp:/run/user python2.sif jupyter notebook`  

Or from shell:  
1. `singularity shell --bind /tmp:/run/user python2.sif`  
2. `jupyter notebook`
	
