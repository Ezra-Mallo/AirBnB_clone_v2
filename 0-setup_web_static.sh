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

datetim=$(date '+%d_%m_%Y_%H_%M_%S')
new_default="default_$datetim"
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/"$new_default"

#replacement="\t\talias /data/web_static/current;\n\t}\n"
#sudo sed -i "s/root /var/www/html;/$replacement/" /etc/nginx/sites-enabled/default
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx start
