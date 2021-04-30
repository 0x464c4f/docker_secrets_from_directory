#!/usr/bin/env python

"""add_secrets_from_dir.py - Takes all filenames of a directory and adds the file contents as secrets in docker swarm with the filename being the secret"""
""" If the secret already exists it is overwritten """
__author__ = "Florian Gottwalt "

from os import listdir
from os.path import isfile, join, exists,basename
import subprocess
import sys

if len(sys.argv)<2:
    exit("Error - please specify directory path as argument")
dir_path = sys.argv[1]
if not exists(dir_path):
    exit("Error - directory path specified does not exist")

for filename in listdir(dir_path):
    filename_with_path = join(dir_path, filename)
    if isfile(filename_with_path):
        # Remove secret if it already exists
        out = subprocess.Popen(["docker", "secret","rm", filename],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        if stderr:
            print("Secret does not exist yet")
        else:
            print("Old secret {0} has been removed".format(filename))
        print("Adding secret {0}".format(filename))
        out = subprocess.Popen(["docker", "secret","create", filename, filename_with_path],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        print(stdout)
        if stderr:
            print(stderr)
    else:
        print("error in file {0}".format(filename))
