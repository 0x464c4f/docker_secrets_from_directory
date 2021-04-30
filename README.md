# Description
This script adds all files from a specified directory as Docker Swarm secrets. 
The filename of the files in the directory is used as the key of the secret. 
If a secret exists already it is removed and updated with a new secret (secret rotation).

# Usage
`python add_secrets_from_dir.py /certificate_directory`

# Notes 
Make sure you have access to the Docker daemon (it is mounted / master node) and that you have permissions to create and remove docker secrets.