#!/bin/bash


if [[ "$#" -lt 1 ]]; then
  echo "Usage:  ./executable_file <zip_archived_filename.tgz>"
  exit 1
fi


archive_path=$1
file=$(basename "$archive_path")
name="${file%.*}"
file_without_stamp="${file%_*}"

file_path="/tmp/$file"

if [[ -f "$file_path" ]]; then

  sudo rm -rf /data/"$file_without_stamp"/releases/"$name"/

  sudo mkdir -p /data/"$file_without_stamp"/releases/"$name"/

  sudo tar -xzf "$file_path" -C /data/"$file_without_stamp"/releases/"$name"/

  sudo mv /data/"$file_without_stamp"/releases/"$name"/"$file_without_stamp"/*\
   /data/"$file_without_stamp"/releases/"$name"/

  sudo rm -rf /data/"$file_without_stamp"/releases/"$name"/"$file_without_stamp"

  sudo rm -rf /data/"$file_without_stamp"/current

  sudo ln -s /data/"$file_without_stamp"/releases/"$name"/\
   /data/"$file_without_stamp"/current

else :
  echo "Archive distributed successfully"

fi
