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

## Run jupyter notebooks (for python2 & python3): 
currently only works as sudo user:

1. `sudo singularity shell python2.sif`

2. `jupyter notebook --allow-root`
	
