import socket
from _thread import *

# Create a socket object
ServerSocket = socket.socket()

# Define the host and port
# Host is set to empty string, meaning it will listen on all available network interfaces
host = '' 
port = 8080
ThreadCount = 0

# Bind the socket to a specific address and port
try:
        ServerSocket.bind((host, port))
except socket.error as e:
        print(str(e))

# Listen for incoming connections
print('Waiting for a Connection..')
ServerSocket.listen(5)

# Function for handling multiple clients
def threaded_client(connection):
        # Send a welcome message to the client
        connection.send(str.encode('Welcome to the Server'))
        while True:
                # Receive data from the client
                data = connection.recv(2048)
                # If there is no data, break the loop
                if not data:
                        break
                # Convert the received data (in Fahrenheit) to Celsius
                fahrenheit = int(data.decode('utf-8'))
                celsius = (fahrenheit - 32) * (5/9)
                # Send the converted temperature back to the client
                reply = 'Server Says: ' + str(celsius) + 'C'
                connection.sendall(str.encode(reply))
        # Close the connection
        connection.close()

while True:
        # Accept a new connection
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))

        # Start a new thread for the new client
        start_new_thread(threaded_client, (Client, ))
        # Increment the thread count
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

# Close the server socket
ServerSocket.close()
