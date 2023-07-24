#!/usr/bin/env bash
# Write a Bash script that transfers a file from our client to a server:

if [ "$#" -lt "3" ];
  then
  #  echo "Usage: ./transfer_file <Path_to_and_source_file> <UserName> <Remote_Host_IP> <Path_to_and_Dest_file>"
  echo "Usage: ./transfer_file </alx/index.html>  <ubuntu>  <10.2.34.5.5>  <~/var/www/html/>"
else
  # Path_to_and_source_file
  argv1=$1  
  
  # username
  argv2=$2

  # remote host IP 
  argv3=$3 
  
  # Path_to_and_Dest_file
  argv4=$4  
  
  # scp [options] SourceFileName UserName@TargetHost:TargetPath
# scp -i "$PATH_TO_SSH_KEY" -o StrictHostKeyChecking=no "$PATH_TO_FILE" "$USERNAME"@"$IP":~/
  scp -o StrictHostKeyChecking=no -i ~/.ssh/id_rsa "$argv1" "$argv2"@"$argv3":"$argv4"
fi
