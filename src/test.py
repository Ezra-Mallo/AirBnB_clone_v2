#!/usr/bin/python3

from fabric import Connection

def test_fabric():
    # Establish a connection to a remote host
    # Replace 'your_username' and 'your_host' with appropriate values
    conn = Connection(host='your_username@your_host')

    # Run a simple command on the remote host
    result = conn.run('echo "Hello, Fabric!"')

    # Print the output of the command
    print(result.stdout)

test_fabric()

