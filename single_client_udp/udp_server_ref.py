# udp server
import os
import socket                                         
import time

#settings
protocol = "udp"
server_port = 12345 # server port no
server_ip = "192.168.56.102" #server ip address
buffer_size = int(input("Enter buffer size: "))
relative_path_to_server_storage = "server_storage"
relative_path_to_books_list = relative_path_to_server_storage + "/list.txt" 

# setting up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))                                  

rcvd_book_name, client_address = server_socket.recvfrom(100)
rcvd_book_name = rcvd_book_name.decode("utf-8").strip(" \n").lower()
print("Book name received by server: %s" % rcvd_book_name)


with open(relative_path_to_books_list) as book_list:
    
    found_in_list=0
    found_file=0
    
    print("Searching for book...")
    
    for book_line in book_list:
    
        book_start = book_line.find(".")+1
        book_end = book_line.find("-")
        
        book_name = book_line[book_start:book_end].strip(" \n").lower()
        # print(book_name)

        if (book_name == rcvd_book_name):
            found_in_list=1
            # print("Found book name in list")
            
            book_index = book_line[book_end+1:].strip(" \n")
            book_storage_path = relative_path_to_server_storage + "/" + book_index
            # print("Book path: %s" % book_storage_path)
            
            if (os.path.exists(book_storage_path)):
                found_file=1
                print("Book found. Sending book to client...")
                server_socket.sendto("Book found".encode("utf-8"), client_address)
                
                with open(book_storage_path,"rb") as book_reader:
                    data = book_reader.read(buffer_size)

                    while(data):
                        server_socket.sendto(data, client_address)                        
                        data = book_reader.read(buffer_size)
            
                server_socket.sendto("Book sent".encode("utf-8"), client_address)

if (found_in_list==False or found_file==False):
    print("Book not found")
    server_socket.sendto("Book not found".encode("utf-8"), client_address)

print("Closing connection...")
server_socket.close()

print("Original book size: {} bytes".format(os.path.getsize(book_storage_path)))