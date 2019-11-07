#!/usr/bin/env python

import sys
import subprocess

# path containing the Dockerfile (and the .sif file afterwards)
path = sys.argv[1]

# name for .sif image
imagename = sys.argv[2]

#==================================================================================================
def info(msg):
    print("\n" + "dockerfile2sif.py: " + msg)

def show_command(msg):
    print("> " + msg )

def err(msg):
    print("dockerfile2sif.py: ERROR when executing " + quote(msg))

def quote(msg):
   return "\"" + msg + "\""

#==================================================================================================
def build_docker(path, imagename):
    build_image = "sudo docker build -t " + imagename + " " + path

    info("building docker image from Dockerfile in " + quote(path))
    show_command(build_image)
    try:
        subprocess.check_call(build_image, shell=True)
    except subprocess.CalledProcessError:
        err(build_image)
        exit(1)


def save_tar(path, imagename):
    save_tar = "sudo docker save " + imagename + " -o " + path +"/"+imagename + ".tar"

    info("saving docker image to temporary .tar file")
    show_command(save_tar)
    try:
        subprocess.check_call(save_tar, shell=True)
    except subprocess.CalledProcessError:
        err(save_tar)
        remove_dockerimage(path, imagename)
        exit(1)


def build_sif(path, imagename):
    build_sif = "sudo singularity build " + path+"/"+imagename+".sif" + " docker-archive://"+path+"/"+imagename+".tar"

    info("building .sif file from .tar file")
    show_command(build_sif)

    try:
        subprocess.check_call(build_sif, shell=True)
    except subprocess.CalledProcessError:
        err(build_sif)
        remove_dockerimage(path, imagename)
        remove_tar(path, imagename)
        exit(1)


def remove_tar(path, imagename):
    remove_tar = "rm -f " + path+"/"+imagename+".tar"

    info("removing temporary .tar file")
    show_command(remove_tar)

    subprocess.check_call(remove_tar, shell=True)


def remove_dockerimage(path, imagename):
    remove_dockerimage = "sudo docker image rm " +imagename

    info("removing temporary docker image from docker")
    show_command(remove_dockerimage)

    subprocess.check_call(remove_dockerimage, shell=True)
#==================================================================================================

# build docker image from dockerfile
build_docker(path, imagename)

# save docker image to temporary .tar file
save_tar(path, imagename)

# build .sif from .tar
build_sif(path, imagename)

# remove temporary .tar
remove_tar(path, imagename)

# remove temporary docker image from docker
remove_dockerimage(path, imagename)

#==================================================================================================