# tcp client
import sys
import os
import socket
import time

#settings
protocol = "tcp"
server_port = 12345 # server port no
server_ip = "10.0.2.15" #server ip address
buffer_size = 32 #buffer size
max_book_name_size = 50 #max no of characters in book name
relative_path_to_client_downloads = "client_downloads" #storage path for client downloads

# print buffer size
print("Client buffer size: %d" % buffer_size)

# setting up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#connecting to the port on server
client_socket.connect((server_ip, server_port))    

# hard-code book name for time and throughput measurements
# book_name = "A Dictionary of Cebuano Visayan" 

# user input name of book
print("Which book do you want to download: ",end='',file=sys.__stdout__)
sys.__stdout__.flush()
book_name = input()

#start timer
start_time = time.time()*1000.0

#send book name to server
client_socket.send(book_name.encode("utf-8"))

# message from server indicating book found or not
book_found = int(client_socket.recv(1).decode("utf-8"))
if (book_found):
    print("Server reply: Book found")
else:
    print("Server reply: Book not found")
    client_socket.close()

# downloading book from server
if book_found:

    #path where downloaded book is saved
    book_save_path = "{path}/{book_name}-{protocol}-{pid}.{extension}".format(
            path=relative_path_to_client_downloads, 
            book_name=book_name.strip(), 
            protocol=protocol.upper(),
            pid=os.getpid(),
            extension="txt"
        )

    #file handler for writing received data from server into the book storage path
    book_writer = open(book_save_path,"wb")

    while True:

        #receive data from server
        data = client_socket.recv(buffer_size)

        if (not data):
            break
        book_writer.write(data)

    book_writer.close()

#close connection
# client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()

#stop timer
end_time = time.time()*1000.0

print("Time taken by {}: {:.5f} ms".format(protocol,end_time-start_time))

if book_found:
    print("Received book size: {} bytes".format(os.path.getsize(book_save_path)),)
    print("Throughput {:.5f} MB/s".format((os.path.getsize(book_save_path)/(2**20))/((end_time-start_time)*(10**(-3)))),  end="\n\n")