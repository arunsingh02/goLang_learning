# Author: Arun Singh
# Email: Arun.Singh2@netapp.com

#!/bin/bash

program="${0}"

echo "Creating dmake runnning env."

working_dir=$(pwd)

echo "Check rsa file status in ~/.ssh folder"

cd ~/.ssh

rsa_count=0
for _ in `ls -m solidfire_dev_rsa*`; do
   ((rsa_count=rsa_count+1))
   if [[ rsa_count -gt 3 ]]; then
       break;
   fi
done

echo "Total number of solidfire_dev_rsa file in .ssh folder: $rsa_count"

if [[ $rsa_count -ne 3 ]]; then
    echo "Getting extra rsa file in .ssh folder, deleting all rsa files and downloading again."
    rm -f solidfire_dev_rsa*
    # change directory to ssh
    wget -P ~/.ssh http://pw-jenkins.pw.solidfire.net/keys/solidfire_dev_rsa{,.pub,.phrase}
    chmod 600 ~/.ssh/solidfire_dev_rsa*
fi

echo "Activate your SSH-agent and then add the solidfire dev key to the agent (MANDATORY)"
ssh_password=`cat ~/.ssh/solidfire_dev_rsa.phrase`

echo $ssh_password

cd $working_dir

echo $(pwd)

eval `ssh-agent`
ssh-add ~/.ssh/solidfire_dev_rsa
echo "Done"

# eval `ssh-agent -k`
bash -i  # or other session starter
