# tcp server
import sys
import os
import socket                                         
import time
import _thread

#log file
# sys.stdout = open('log.txt', 'a')

#settings
protocol = "udp"
server_port = 6000 # server port no
server_ip = "10.0.2.15" #server ip address
buffer_size = 32
max_book_name_size = 50 #no of characters
relative_path_to_server_storage = "server_storage"
relative_path_to_books_list = relative_path_to_server_storage + "/list.txt" 

# print buffer size
print("Server buffer size: %d" % buffer_size)

#print server port
print("Server port: %d" % server_port)

# client process
def client_process(rcvd_book_name, client_address):
    rcvd_book_name = rcvd_book_name.decode("utf-8").strip(" \n").lower()

    print("Got a connection from {}".format(client_address))
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
                    server_socket.sendto("1".encode("utf-8"), client_address)
                    
                    with open(book_storage_path,"rb") as book_reader:
                        data = book_reader.read(buffer_size)

                        while(data):
                            server_socket.sendto(data, client_address)   

                            #100 microseconds sleep
                            time.sleep(0.0001)

                            data = book_reader.read(buffer_size)

    if (found_in_list==False or found_file==False):
        print("Book not found")
        server_socket.sendto("0".encode("utf-8"), client_address)
    
    if (found_in_list and found_file):
        print("Original book size: {} bytes".format(os.path.getsize(book_storage_path)), end="\n\n")


# setting up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server_ip, server_port))                                  

while True:
    rcvd_book_name, client_address = server_socket.recvfrom(max_book_name_size)
    _thread.start_new_thread(client_process,(rcvd_book_name, client_address))

print("Closing connection...")
# server_socket.shutdown(socket.SHUT_RDWR)
server_socket.close()