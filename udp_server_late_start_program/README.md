# UDP Server Late Start Program

## Detail
* Constains code for **UDP Q4 (c) part 2**
* Handles the case when the *UDP server* is started 30 seconds after the *UDP client*
*  Uses client retransmissions and timeout to enable downloads even if server starts late
* Program files: **udp_server.py** and **udp_client.py**


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

## Explanation of the problem and solution approach

* In the normal case, when the server is already running when the client wants to connect:
    * The client sends a packet to the server containing the book name to download and waits for the server’s response
    * The server receives the packet containing the book name, indexes the book and transfers it to the client

* If the server is started 30 seconds after the client process:
    * The client sends a packet to the server (when the server is not up) containing the book name to download and waits for the server’s response. 
    * Thus, this packet never reaches the server and is lost.
    * When the server is started, it waits for the packet containing the book name whereas the client is waiting for the response from the server (the file) assuming that the server has already received the book name
    * Thus, the process is stuck on both ends

* Solution to the problem mentioned in the above point:
    * I solved the above problem by setting a timeout value for the server response on the client side ie. after sending the packet containing the book name, the client waits for the server response for some time
    * If the response is received it receives the file but if no response is received, it retransmits the packet containing the book name to the server
    * Thus, even if the server starts 30 seconds late, it receives the packet containing the book name and the client is able to download the file

<br>

## Instructions for running code
1. First run the *udp_client.py* file using the command `python3 udp_client.py`. This will start a client process. Enter the name of the book to download when prompted. On hitting enter the client will start transmitting the packet containing the book name to the server
2. Wait for 30 seconds. 
3. Run the *udp_server.py* file using the command `python3 udp_server.py`. This will start the server. 
4. The book (if found) will be downloaded in the *client_downloads* folder and the client process will terminate
4. The server process in this case will have to be terminated manually as the server code will keep on running ready to accept client requests

<br>

## Variable parameters
* server_ip: This varibale corresponds to the IP address of the server
* server_port: This This varibale corresponds to the port no. of the server
* buffer_size: Indicates the no of bytes of data sent or received in one packet



