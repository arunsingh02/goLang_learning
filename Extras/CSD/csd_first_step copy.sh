# Author: Arun Singh
# Email: Arun.Singh2@netapp.com


#!/bin/bash

mapnode_flag=false

if [[ -z "${2}" ]] ; then
    DIR="."
else
    echo "Given path for extraction should be directory and exists : ${2}"
    if [[ -d "${2}" ]] ; then
        DIR="${2}"
    else
        echo "Given path for extraction not a directory or not exists."
        DIR="."
    fi
fi

program="${0}"

function usage() {
        cat <<EOF >&2

    Usage:
        # extract tar files
        # In case of path of file in directory is empty then extraction will 
        # perform on current working directory
        $program "tar"(required) "path of file in directory"(optional)

        # extract tar.gz files
        $program "gz"(required) "path of file in directory"(optional)

    Example:
        # $program "tar" "/data"

EOF
}


function directory_check_and_extract_archive() {
    local tar_file_name="$1"
    file_name=(${tar_file_name//".tar"/ })
    if [[ -d "$file_name" ]] ; then
        echo "This $tar_file_name file already untared."
        return 1 
    fi
    mapnode_flag=true
    echo "Running the command 'tar -xf' on $tar_file_name file and extracted on $DIR directory"
    # https://www.geeksforgeeks.org/tar-command-linux-examples/
    tar -xf $tar_file_name -C $DIR
}



if [[ "${1}" == "tar" ]] ; then
    echo "Start untaring all tar files.."
    echo "ls -ll | grep '.*tar$'"
    ls -ll | grep '.*tar$'
    echo "Iterating all files ends with '.tar' and extracting files from Archive if file not extracted."
    for f in *.*tar; do
        if [[ $f == "*.*tar" ]] ; then
            echo "No tar file present in this CSD."
            break
        fi
        # calling function
        directory_check_and_extract_archive "$f"
    done
elif [[ "${1}" == "gz" ]] ; then
    echo "Start untaring all tar.gz files.."
    echo "ls -ll | grep '.*tar.gz'"
    ls -ll | grep '.*tar.gz'
    echo "Iterating all files ends with '.tar.gz' and extracting files from Archive if file not extracted."

    for f in *.*tar.gz; do
        if [[ $f == "*.*tar.gz" ]] ; then
            echo "No tar.gz file present in this CSD."
            break
        fi
        # calling function
        directory_check_and_extract_archive "$f"
    done
else
    usage
    exit 1
fi


if $mapnode_flag ; then
    echo "Running mapnodes command on extracted files to get more detailed information about Cluster."
    eval "mapnodes"
fi

echo "Finish.."
