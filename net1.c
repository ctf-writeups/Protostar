#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>

void err_msg(int ret, char *message){

	if(message == NULL){
		
		printf("%s\n", strerror(errno));
		exit(ret);
	}
	else{
	
		printf("%s\n", message);
		exit(ret);
	}
}

int main(int argc, char **argv){

	int sock_fd;
	char buffer[1024];
	struct sockaddr_in mystruct;
	//in_port_t port = 2998;

	if((sock_fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1)
		err_msg(1, NULL);

	memset(&mystruct, 0, sizeof(mystruct));
	mystruct.sin_family = AF_INET;
	mystruct.sin_port = htons(2998);
	inet_pton(AF_INET, "127.0.0.1", &mystruct.sin_addr.s_addr);

	if(connect(sock_fd, (struct sockaddr *)&mystruct, sizeof(mystruct))==-1)
		err_msg(2, NULL);

	memset(buffer, 0, sizeof(buffer));
		
	recv(sock_fd, buffer, sizeof(buffer), 0);

	int32_t EndianValue;
	char buf[50];
	
	memset(buf, 0, sizeof(buf));
	memcpy(&EndianValue, buffer, sizeof(EndianValue));	
	printf("%d\n", EndianValue);
	sprintf(buf , "%d", EndianValue);
	send(sock_fd, buf, sizeof(buf), 0);
	recv(sock_fd, buffer, sizeof(buffer), 0);	
	printf("%s\n", buffer);	

	return 0;
}
