#!/usr/bin/env bash
# Install Nginx if it not already installed
sudo apt update -y
sudo apt install nginx -y

# create the folders and path if it does not exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# create file with content if not exist
echo echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# change user:group ownership of /data/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data

# create symbolic link for current if not exist
alias_config=\
"   location /hbnb_static {
	alias /data/web_static/current;
}"
sudo echo -e "$alias_config" | sudo tee -a /etc/nginx/sites-available/default
# sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default


sudo service nginx start
