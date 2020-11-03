# Single client UDP

## Code structure

* `server_storage`
    * *list.txt* : contains the name of the books stored in the server along with the file name for every book
    * Contains text files corresponding to available books

* `client_downloads`
    * The files downloaded by the client are stored in this folder 
    * The name  format for the downloaded file is: *"Bookname-Protocol-Process_id.txt"*

* `files_related_to_different_buffer_sizes_experiments`
    * Contains files for *Q3 (c)* (relevant files hyperlinked in report). 
    * `files_received_by_client`: Contains the files received by client from server for different buffer sizes. Buffer size suffixed in the file name
    * `files_generated_using_diff_command`: 
        * Contains the differences between the received file and the original file. 
        * Contains the output of the bash command: `diff received_file  original_file` for every entry

* `udp_server.py`: Program file containing the server side code
* `udp_client.py`: Program file containing the client side code

<br>

## Instructions for running code
1. First run the *udp_server.py* file using the command `python3 udp_server.py`. This will start the server.
2. Then run the *udp_client.py* file using the command `python3 udp_client.py`. This will start the client process. Enter the name of the book to download when prompted.
3. The book (if found) will be downloaded in the *client_downloads* folder
4. The server and client processes will terminate

<br>

## Variable parameters
* server_ip: This varibale corresponds to the IP address of the server
* server_port: This This varibale corresponds to the port no. of the server
* buffer_size: Indicates the no of bytes of data sent or received in one packet



