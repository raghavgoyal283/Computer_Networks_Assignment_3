# Multi client UDP

## Code structure

* `server_storage`
    * *list.txt* : contains the name of the books stored in the server along with the file name for every book
    * Contains text files corresponding to available books

* `client_downloads`
    * The files downloaded by the client are stored in this folder 
    * The name  format for the downloaded file is: *"Bookname-Protocol-Process_id.txt"*

* `udp_server.py`: Program file containing the server side code
* `udp_client.py`: Program file containing the client side code

<br>

## Instructions for running code
1. First run the *tcp_server.py* file using the command `python3 udp_server.py`. This will start the server. The server will keep on running and can accept simultaneous requests from multiple clients
2. Then run the *tcp_client.py* file using the command `python3 udp_client.py`. This will start the first client process. Enter the name of the book to download when prompted. On hitting enter the server will be prompted to deliver the book to the first client
3. While the first client process is in progress, start another client process using the same procedure as in 2. Now, both the processes will run simultaneously and download books from the server
4. To observe the simultaneous execution of client processes, it is better to set the buffer sizes to a low value on both the client and server side. Also, use a large file for download, for eg: A Dictionary of Cebuano Visayan or Essays of Michel de Montaigne
3. The books (if found) will be downloaded in the *client_downloads* folder and the client processes will terminate
4. The server process in this case will have to be terminated manually as the server code will keep on running ready to accept client requests

<br>

## Variable parameters
* server_ip: This varibale corresponds to the IP address of the server
* server_port: This This varibale corresponds to the port no. of the server
* buffer_size: Indicates the no of bytes of data sent or received in one packet



