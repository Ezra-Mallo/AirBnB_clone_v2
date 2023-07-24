# [Previous](https://github.com/Ezra-Mallo/AirBnB_clone_v1/README.md)   | 0x02. AirBnB clone - MySQL. | [Next](https://github.com/Ezra-Mallo/AirBnB_clone_v2/blob/master/README_2.md)
<p align="center">
<img src="https://github.com/Ezra-Mallo/AirBnB_clone_v2/blob/master/images_logos/hbnb_logo.png"
	    alt="ALX_AirBnB logo">
</p>

This is the third step towards building our first full web application: the AirBnB clone. 

We shall modify our command interpreter, create database and link all our objects up. All these are still at the backend of this project.

<img src="https://github.com/Ezra-Mallo/AirBnB_clone_v2/blob/master/images_logos/hbnb_step3.png"
	    alt="ALX_AirBnB logo">
</p>
<p>
<img src="https://github.com/Ezra-Mallo/AirBnB_clone_v2/blob/master/images_logos/hbnb_db_structural_design.jpg"
	    alt="ALX_AirBnB DB structural Design">
</p>

# Install Flask
```
$ pip3 install Flask
```
# Resources Read or watch:

* [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
* [A Minimal Application](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)
* [Routing (except “HTTP Methods”)](https://flask.palletsprojects.com/en/1.0.x/quickstart/#routing)
* [Rendering Templates](https://flask.palletsprojects.com/en/1.0.x/quickstart/#rendering-templates)
* [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
* [Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
* [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
* [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
* [List of Control Structures (read up to “Call”)](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures)
* [Flask](https://palletsprojects.com/p/flask/)
* [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)


* When you encounter the error 
```
Ubuntu:~/alx/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app '0-hello_route' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
```
* Use this approach to release the port manually:
In some cases, the process using port 5000 might not be necessary, and you can release the port manually. On Linux, you can use the fuser command:
```
fuser -k 5000/tcp
```
This command will forcefully kill the process using port 5000, allowing you to start the Flask server on that port.

Remember that if you choose a different port for your Flask server, you will need to use that port number in the URL when accessing the application in your web browser or making HTTP requests.

After implementing one of the above options, you should be able to start the Flask application without any issues.
