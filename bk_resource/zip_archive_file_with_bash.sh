#!/bin/bash

do_pack() {
    # A function that generates an archive of the contents of a specified folder

    folder=$1
    timestamp=$(date +"%Y%m%d%H%M%S")

    # Create the versions directory if it doesn't exist
    mkdir -p versions

    # Create the tarball
    tar -czvf "versions/${folder}_${timestamp}.tgz" "$folder"

    echo "versions/${folder}_${timestamp}.tgz"
}


if [[ "$#" -lt 1 ]]; then
  echo "Usage:  ./executable_file <folder_to_archive>"
  exit 1
fi

folder=$1

# Call the function with the folder name as an argument and store the result in a variable
result=$(do_pack "$folder")

if [[ -n $result ]]; then
    echo "Archive created successfully: $result"
else
    echo "Failed to create the archive."
fi

