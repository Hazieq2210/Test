import threading
import random
import socket

# array of quotes
quotes = ["If you tell the truth, you don't have to remember anything.", "The reason I talk to myself is because I’m the only one whose answers I accept.", "A lie can travel half way around the world while the truth is putting on its shoes.", "Perhaps one did not want to be loved so much as to be understood."]

# Function to handle client connections
def handle_client(client_socket):
    # Choose a random quote
    quote = random.choice(quotes)
    # Send the quote to the client
    client_socket.send(quote.encode())
    # Close the client socket
    client_socket.close()

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to all available network interfaces and port 8888
server.bind(("0.0.0.0", 8888))
# Listen for incoming connections
server.listen(5)

while True:
    # Accept a new connection
    client, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
    # Start a new thread for the new client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
