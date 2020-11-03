# tcp server
import sys
import os
import socket                                         
import time
import _thread

#settings
protocol = "udp"
server_port = 6000 # server port no
server_ip = "10.0.2.15" #server ip address
buffer_size = 32 #buffer size
max_book_name_size = 50 #max no of characters in book name
relative_path_to_server_storage = "server_storage" #path where server files are stored
relative_path_to_books_list = relative_path_to_server_storage + "/list.txt" #path to file containing the list of books
 
# print buffer size
print("Server buffer size: %d" % buffer_size)

# client process function (multiple such processes run in parallet to cater to multiple clients simultaneously)
def client_process(rcvd_book_name, client_address):

    #Server receives book name from client
    rcvd_book_name = rcvd_book_name.decode("utf-8").strip(" \n").lower()

    print("Got a connection from {}".format(client_address))
    print("Book name received by server: %s" % rcvd_book_name)

    # Searching for book in the storage
    with open(relative_path_to_books_list) as book_list:
        
        found_in_list=0 #1 if book name found in list
        found_file=0 #1 if book found in storage
        
        print("Searching for book...") 
        
        for book_line in book_list: #reading a line from list.txt containing book name and path
        
            book_start = book_line.find(".")+1
            book_end = book_line.find("-")
            
            #name of book
            book_name = book_line[book_start:book_end].strip(" \n").lower()
            # print(book_name)

            if (book_name == rcvd_book_name):
                found_in_list=1
                # print("Found book name in list")
                
                book_index = book_line[book_end+1:].strip(" \n")

                #book path in server storage
                book_storage_path = relative_path_to_server_storage + "/" + book_index
                # print("Book path: %s" % book_storage_path)
                
                if (os.path.exists(book_storage_path)):
                    found_file=1
                    print("Book found. Sending book to client...")

                    #1 message indicates book found
                    server_socket.sendto("1".encode("utf-8"), client_address)
                    
                    #send the data to the client
                    with open(book_storage_path,"rb") as book_reader:
                        data = book_reader.read(buffer_size)

                        while(data):
                            server_socket.sendto(data, client_address)   

                            #100 microseconds sleep
                            time.sleep(0.0001)

                            data = book_reader.read(buffer_size)

    #Book not found
    if (found_in_list==False or found_file==False):
        print("Book not found")

        #0 message indicates book not found
        server_socket.sendto("0".encode("utf-8"), client_address)
    
    if (found_in_list and found_file):
        print("Original book size: {} bytes".format(os.path.getsize(book_storage_path)), end="\n\n")


# setting up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server_ip, server_port))                                  

#server always ready to accept client requests (infinite while loop)
while True:

    #new connection request
    rcvd_book_name, client_address = server_socket.recvfrom(max_book_name_size)

    #start a new thread (process) to download the book for this client
    _thread.start_new_thread(client_process,(rcvd_book_name, client_address))

#close the server
print("Closing connection...")
# server_socket.shutdown(socket.SHUT_RDWR)
server_socket.close()