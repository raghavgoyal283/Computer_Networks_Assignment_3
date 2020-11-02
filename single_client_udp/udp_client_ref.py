# udp client
import os
import socket
import time

#settings
protocol = "udp"
server_port = 12345 # server port no
server_ip = "192.168.56.102" #server ip address
server_address = (server_ip, server_port)
buffer_size = int(input("Enter buffer size: "))
relative_path_to_client_downloads = "client_downloads"

# setting up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# hard-code book name for time and throughput measurements
book_name = "A Dictionary of Cebuano Visayan"

# user input name of book
# book_name = input("Which book do you want to download: ")
start_time = time.time()*1000.0
client_socket.sendto(book_name.encode("utf-8"), server_address)

# message indicating book found or not
book_found, _ = client_socket.recvfrom(100)
book_found = book_found.decode("utf-8")
print("Server reply: %s" % book_found)


if (book_found == "Book not found"):
    client_socket.close()
    exit()

# downloading book from server
book_save_path = "{path}/{book_name}-{protocol}-{pid}.{extension}".format(
        path=relative_path_to_client_downloads, 
        book_name=book_name.strip(), 
        protocol=protocol.upper(),
        pid=os.getpid(),
        extension="txt"
    )
book_writer = open(book_save_path,"wb")

while True:
    try:
        client_socket.settimeout(0.1)
        # print(time.time()*1000-start_time)
        data, _ = client_socket.recvfrom(buffer_size)
        if (not data):
            break
        book_writer.write(data)
    except:
        break

book_writer.close()
client_socket.close()

end_time = time.time()*1000.0

print("Time taken by {}: {:.5f} ms".format(protocol,end_time-start_time))
print("Received book size: {} bytes".format(os.path.getsize(book_save_path)))