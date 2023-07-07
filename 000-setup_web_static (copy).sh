#!/usr/bin/env bash

# Install Nginx if it not already installed
apt update -y
apt install nginx -y

# create the folders and path if it does not exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/ 

# create file with content if not exist
file_path="/data/web_static/releases/test/index.html"
content=\
"<html>
    <body>
      <h1>This is my index.html file. Release 1.0 </h1>
    </body>
</html>"

if [ ! -f "$file_path" ]; then
    # Create the file with the desired content
    echo "$content" | tee "$file_path"
fi

# change user:group ownership of /data/
chown -R ubuntu:ubuntu /data/


# create symbolic link for current if not exist
ln -sf /data/web_static/releases/test/ /data/web_static/current

alias_config=\
"   location /hbnb_static {
	alias /data/web_static/current/;
}"
echo -e "$alias_config" | sudo tee -a /etc/nginx/sites-available/default

sudo systemctl restart nginx