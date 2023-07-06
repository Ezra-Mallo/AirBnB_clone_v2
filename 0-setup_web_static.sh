#!/usr/bin/env bash

# Install Nginx if it not already installed
sudo apt-get update -y
sudo apt-get install nginx -y

# create /data/web_static/releases/test/ if it does not exist
sudo mkdir -p /data/web_static/releases/test/

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
    echo "$content" > "$file_path"
    echo "File created: $file_path"
else
    echo "File already exists: $file_path"
fi

# change user:group ownership of /data/
sudo chown -R ubuntu:ubuntu /data/

# create folder if not exist
sudo mkdir -p /data/web_static/shared/ 

# create symbolic link for current if not exist
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

alias_config=\
"   location /hbnb_static {
	alias /data/web_static/current/;
}"
echo -e "$alias_config" | sudo tee -a /etc/nginx/sites-available/default

sudo systemctl restart nginx
