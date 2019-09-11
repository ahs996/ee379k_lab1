#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h> 
#include<string.h>
#include <arpa/inet.h>
#include <unistd.h> 
 
int main()
{
    int sockfd,n;
    char sentence[1024];
    char modSentence[1024];
    struct sockaddr_in servaddr;
 
    sockfd=socket(AF_INET,SOCK_STREAM,0);
    bzero(&servaddr,sizeof servaddr);
 
    servaddr.sin_family=AF_INET;
    servaddr.sin_port=htons(12000);
 
    inet_pton(AF_INET,"127.0.0.2",&(servaddr.sin_addr));
 
    if(connect(sockfd,(struct sockaddr *)&servaddr,sizeof(servaddr)) < 0){
        perror("Socket connection failed");
        exit(EXIT_FAILURE);
    }
    printf("Input lowercase sentence\n");

    //clear write and read buffers
    bzero( sentence, 1024);
    bzero( modSentence, 1024);
    fgets(sentence,1024,stdin);

    write(sockfd, sentence,strlen(sentence)+1);
    read(sockfd,modSentence,1024);
    printf("From server: %s",modSentence);
 
}