# [Previous](https://github.com/Ezra-Mallo/AirBnB_clone_v2/edit/master/README.md)   | 0x03. AirBnB clone - Deploy static| [Next]()

<p align="center">
<img src="https://github.com/Ezra-Mallo/AirBnB_clone_v2/blob/master/images_logos/hbnb_logo.png"
	    alt="ALX_AirBnB logo">
</p>

# DevOps | Python | SysAdmin | Scripting | CI/CD |


Background Context
Ever since you completed project 0x0F. Load balancer of the SysAdmin track, you’ve had 2 web servers + 1 load balancer but nothing to distribute with them.

It’s time to make your work public!

In this first deployment project, you will be deploying your web_static work. You will use Fabric (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.

<p>
<img src="https://github.com/Ezra-Mallo/AirBnB_clone_v2/blob/master/images_logos/aribnb_diagram_0.jpg"
	    alt="ALX_AirBnB DB structural Design">
</p>

For this project, we expect you to look at these concepts:

* [CI/CD](#ci/cd)
* [AirBnB clone](https://github.com/Ezra-Mallo/AirBnB_clone_v1)

## Resources to read or watch:
* [How to use Fabric](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)
* [How to use Fabric in Python](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python)
* [Fabric and command line options](https://docs.fabfile.org/en/1.13/usage/fab.html)
* [CI/CD concept page](#ci/cd)
* [Nginx configuration for beginners](http://nginx.org/en/docs/beginners_guide.html)
* [Difference between root and alias on NGINX](https://github.com/mathiasertl/fabric)
* [Fabric for Python 3]()
* [Fabric Documentation](https://www.fabfile.org/)
* [tar commad](https://linuxize.com/post/how-to-create-and-extract-archives-using-the-tar-command-in-linux/)

## Install Fabric for Python 3 - version 1.14.post1
```
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1
```


## CI/CD
The lean/agile methodology (See: Twelve Principles of Agile Software) is now widely used by the industry and one of its key principles is to iterate as fast as possible. If you apply this to software engineering, it means that you should:

code
ship your code
measure the impact
learn from it
fix or improve it
start over
As fast as possible and with small iterations in days or even hours (whereas it used to be weeks or even months). One big advantage is that if product development is going the wrong direction, fast iteration will allow to quickly detect this, and avoid wasting time.

From a technical point of view, quicker iterations mean fewer lines of code being pushed at every deploy, which allows easy performance impact measurement and easy troubleshooting if something goes wrong (better to debug a small code change than weeks of new code).



Applied to software engineering, CI/CD (Continuous Integration/Continuous Deployment) is a principle that allows individuals or teams to have a lean/agile way of working.

This translates to a “shipping pipeline” which is often built with multiple tools such as:

Shipping the code:
Capistrano, Fabric
Encapsulating the code
Docker, Packer
Testing the code
Jenkins, CircleCi, Travis
Measuring the code
Datadog, Newrelic, Wavefront

