# tcp server
import sys
import os
import socket                                         
import time

#nagle and delayed acks
nagle_disable = 0 #set to 1 if you want to disable Nagle's algorithm
delayed_ack_disable = 0 #set to 1 if you want to disable delayed acks

print("Server nagle disable: %d" % nagle_disable)
print("Server delayed_ack disable: %d" % delayed_ack_disable)

#settings
protocol = "tcp"
server_port = 12345 # server port no
server_ip = "10.0.2.15" #server ip address
buffer_size = 32 #buffer size
max_book_name_size = 50 #max no of characters in book name
relative_path_to_server_storage = "server_storage" #path where server files are stored
relative_path_to_books_list = relative_path_to_server_storage + "/list.txt"  #path to file containing the list of books

# print buffer size
print("Server buffer size: %d" % buffer_size)

# setting up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server_ip, server_port))                                  

if (nagle_disable):
    print("Disabling Nagle's Algorithm")
    server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)

server_socket.listen()                                          
print("Sever listening on port %d" % server_port)

# connection starts
connection_socket, client_address = server_socket.accept()      
print("Got a connection from %s" % str(client_address))

if (delayed_ack_disable):
    print("Disabling delayed acks...")
    server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_QUICKACK,True)

#Server receives book name from client
rcvd_book_name = connection_socket.recv(max_book_name_size).decode("utf-8").strip(" \n").lower()
print("Book name received by server: %s" % rcvd_book_name)

# Searching for book in the storage
with open("./"+relative_path_to_books_list) as book_list:
    
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
            print("Book path: %s" % book_storage_path)
            
            if (os.path.exists(book_storage_path)):
                found_file=1
                print("Book found. Sending book to client...")

                if (delayed_ack_disable):
                    server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_QUICKACK,True)
                
                #1 message indicates book found
                connection_socket.send("1".encode("utf-8"))
                
                #send the data to the client
                with open(book_storage_path,"rb") as book_reader:
                    data = book_reader.read(buffer_size)

                    while(data):
                        
                        if (delayed_ack_disable):
                            server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_QUICKACK,True)

                        connection_socket.send(data)
                        
                        data = book_reader.read(buffer_size)


#Book not found
if (found_in_list==False or found_file==False):
    print("Book not found")

    if (delayed_ack_disable):
        server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_QUICKACK,True)

    #0 message indicates book not found
    connection_socket.send("0".encode("utf-8"))

#close the connection
print("Closing connection...")
connection_socket.shutdown(socket.SHUT_RDWR)
connection_socket.close()
server_socket.shutdown(socket.SHUT_RDWR)
server_socket.close()

if (found_in_list and found_file):
    print("Original book size: {} bytes".format(os.path.getsize(book_storage_path)), end="\n\n")