#!/usr/bin/env bash
# Install Nginx if it not already installed
sudo apt update -y
sudo apt install nginx -y

# create the folders and path if it does not exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create file with content if not exist
content="<!DOCTYPE html><html><body><h1>This is my index.html file. Release 1.0 </h1></body></html>"
echo "$content" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# change user:group ownership of /data/
sudo chown -R ubuntu:ubuntu /data

# create symbolic link for current if not exist
alias_config=\
"   location /hbnb_static {
	alias /data/web_static/current/;
}"
sudo echo -e "$alias_config" | sudo tee -a /etc/nginx/sites-available/default

sudo service nginx restart
#sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
#sudo service nginx restart
