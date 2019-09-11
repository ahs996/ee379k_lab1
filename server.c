#include <sys/socket.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h> 
 
void strUP(char str[]);
int main(){
    char str[1024];
    int server_fd, comm_fd; //server and communicating socket commands
    struct sockaddr_in address;

    if((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
        perror("Socket connection failed");
        exit(EXIT_FAILURE);
    }
    
    bzero(&address, sizeof(address));

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = htons(INADDR_ANY);
    address.sin_port = htons(12000);
    bind(server_fd, (struct sockaddr *) &address, sizeof(address));
 
    // listen for client connections
    if(listen(server_fd, 5)<0){
        perror("Failed to connect to client");
        exit(EXIT_FAILURE);
    }

    printf("The server is ready to receive. \n");

    while(1){
        bzero( str, 100);

        comm_fd = accept(server_fd, (struct sockaddr*) NULL, NULL);
        if(comm_fd < 0){
            perror("Failed to accept");
            exit(EXIT_FAILURE);
        }
        if(read(comm_fd,str,1024) < 0){
            perror("Error reading");
            exit(EXIT_FAILURE);
        }


        strUP(str);
        printf("%s", str);
 
        write(comm_fd, str, strlen(str)+1);

        shutdown(comm_fd, SHUT_RDWR);

        close(comm_fd);
 
    }
}

void strUP(char str[]){
    for(int i=0; str[i]!='\0'; i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] = str[i] - 32;
        }
    }
}