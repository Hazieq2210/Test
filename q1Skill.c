#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int main(int argc, char* argv[]) 
{
    int socket_desc;
    int client_sock;
    int c;
    struct sockaddr_in server, client;
    int random_number;
    srand(time(0));

    // Create socket
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_desc == -1) 
	{
        printf("Could not create socket");
        return 1;
    }
    puts("Socket created");

    // Prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(8080);

    // Bind the socket
    if (bind(socket_desc, (struct sockaddr*)&server, sizeof(server)) < 0) 
	{
        perror("bind failed. Error");
        return 1;
    }
    puts("bind done");

    // listen to the socket
    listen(socket_desc, 3);

    puts("Waiting for incoming connections...");
    c = sizeof(struct sockaddr_in);

    // accept connection from an incoming client
    client_sock = accept(socket_desc, (struct sockaddr*)&client, (socklen_t*)&c);

    if (client_sock < 0) 
	{
        perror("accept failed");
        return 1;
    }

    puts("Connection accepted");

    // generate random number
    random_number = (rand() % (999 - 100 + 1) + 100);

    // send random number to client
    write(client_sock, &random_number, sizeof(random_number));
    printf("sent random number %d to the client",random_number);

    // close the socket
    close(client_sock);
    close(socket_desc);
    return 0;
}
