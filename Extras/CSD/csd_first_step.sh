# Author: Arun Singh
# Email: Arun.Singh2@netapp.com

#!/bin/bash

program="${0}"

function usage() {
        cat <<EOF >&2

    Usage:
        -h (help),                  Display help

        -t (bundle type),           File type which we are going to extract. eg. tar / zip

        -d (directory),             Directory path where we are going to extract the bundle file.
        
        -b (bundle file name),      Bundle file name to extract.

        -m (mapnode),               symlinks providing nodeID (ensemble nodes) per bundle.

        -n (nazgul/gullom),         Run this first to potential solve the case right from the start.
        
        -f (node hardwrae info),    Generate hardware_info.txt file in all nodes with hardware details.
        
        -g (QoS graph),             Generate QoS pushback graphs.

    Example:
        # $program -t zip -g -n Enode1 -f -m
        or
        # $program -t tar -d /x/y/z -b abc.tar -g -n Enode1 -f
        or 
        # $program -d test -n "" -m -f -g (If don't want to run Nazgul)

EOF
}

nazgul="./"
extract_dir="."
bundle_file="*"

while getopts ="h?t::d::b::n::mfg" opt; do
  case "$opt" in
    h)
      usage
      exit 1
      ;;
    t)  file_type=$OPTARG
        if [[ ${file_type} != "tar" ]] && [[ ${file_type} != "zip" ]] ; then
            echo "Currently ${file_type} file type is not supported in this script. Please proceed with tar or zip." 1>&2
            exit 1
        fi
      ;;
    d)  extract_dir=$OPTARG
      ;;
    b)  bundle_file=$OPTARG
      ;;
    m)  mapnode=1
      ;;
    n)  nazgul=$OPTARG
      ;;
    f)  hardware_info=1
      ;;
    g)  qos_graph=1
      ;;
    \? ) echo "Invalid Option: -$OPTARG" 1>&2
          usage
          exit 1
      ;;
  esac
done

# TODO We can create new folder in case folder not exists
echo
if [[ -d "$extract_dir" ]] ; then
    DIR="$extract_dir"
elif [[ $extract_dir != "." ]]; then
    echo "Given path for extraction not a directory or not exists so exracting at the current path."
    DIR="."
fi


if [[ -n $file_type ]];then
    if [[ $file_type == "tar" ]];then
        echo "Start untaring the tar files.."
        echo "ls -ll | grep '.*tar$'"
        ls -ll | grep '.*tar$'
        for tar_file_name in $(ls -d $bundle_file);do
            echo "Running the command 'tar -xf' on $tar_file_name file"
            # https://www.geeksforgeeks.org/tar-command-linux-examples/
            tar -xf $tar_file_name -C $DIR
        done
    elif [[ $file_type == "zip" ]];then
        echo "Start unziping the zip files.."
        echo "ls -ll | grep '.*zip$'"
        ls -ll | grep '.*zip$'
        for zip_file_name in $(ls -d $bundle_file);do
            echo "Running the command 'unzip' on $zip_file_name file"
            # https://www.geeksforgeeks.org/zip-command-in-linux-with-examples/
            unzip $zip_file_name -d $DIR
        done
    fi
fi

echo
if [[ $DIR != "." ]]; then
  echo "cd $DIR"
  cd ${DIR}
  pwd
fi

echo
if [[ $mapnode -eq 1 ]] ; then
    echo "Running mapnodes: symlinks providing nodeID (ensemble nodes) per bundle."
    eval "mapnodes"
fi

echo
if [[ $nazgul != "" ]]; then
    echo "Running nazgul/gullom"
    tmux new-session -s nazgul "gollum.py full $nazgul"
    echo "nazgul/gullom is done successfully."
fi

echo
if [[ $hardware_info -eq 1 ]] ; then
    echo "Running node hardware info on all nodes" 
    eval "node_hardware_info"
fi

echo
if [[ $qos_graph -eq 1 ]] ; then
    echo "Running graph_all.sh to get qos pushback graphs"
    eval "graph_all.sh"
fi

echo "Finish.."

# TESTED
# ./test.sh -t tar -b CM.SPHCI-stg-01.tar -n CM.SPHCI-stg-01 -d test
# ./test.sh -d test -n "" -m -g -f (nazgul will not run)