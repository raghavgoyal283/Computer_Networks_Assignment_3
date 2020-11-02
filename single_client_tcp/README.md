# Single client TCP

## Code structure

* `server_storage`
    * *list.txt* : contains the name of the books stored in the server along with the file name for every book
    * Contains text files corresponding to available books

* `client_downloads`
    * The files downloaded by the client are stored in this folder 
    * The name  format for the downloaded file is: *"Bookname-Protocol-Process_id.txt"*

* `tcp_server.py`: Program file containing the server side code
* `tcp_client.py`: Program file containing the client side code

<br>

## Instructions for running code
1. First run the *tcp_server.py* file using the command `python3 tcp_server.py`. This will start the server.
2. Then run the *tcp_client.py* file using the command `python3 tcp_client.py`. This will start the client process. Enter the name of the book to download when prompted.
3. The book (if found) will be downloaded in the *client_downloads* folder

<br>

## Variable parameters
* server_ip: This varibale corresponds to the IP address of the server
* server_port: This This varibale corresponds to the port no. of the server
* nagle_disable: Indicates whether Nagle's algorithm is disabled or not. Set to 1 if you want to disable Nagle's Algorithm.
* delayed_ack_disable: Indicates whether Delayed Acks are disabled or not. Set to 1 if you want to disable Delayed Acks.



