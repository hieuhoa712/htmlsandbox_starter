import socket
import time
import statistics

# Create a UDP socket

server_address = ('localhost', 10000)
message = 'This is the message'
rtt = []
for index in range(10):
    print("Ping", index+1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set timeout of 2 seconds.
    sock.settimeout(2)
    try:
        # Send data
        message_bytes = bytes(message, "utf-8")
        start = time.time()
        # Send data to server.
        sent = sock.sendto(message_bytes, server_address)

        # Receive response or exit
        recieved = False
        try:
            recieved = True
            data, address = sock.recvfrom(1024)
            end = time.time()
            rtt.append(end-start)
            # Calculate and print relevant data.
            print(data)
            print("Min RTT =", min(rtt),"seconds")
            print("Max RTT =", max(rtt),"seconds")
            print("Average RTT =", statistics.mean(rtt),"seconds")
            print("Standard Deviation of RTTs =", statistics.stdev(rtt),"seconds")
            
            
        except:
            if not recieved:
                pass
        print("")
            
    finally:
        sock.close()
        
# Calculate and print packet loss rate
loss_rate = 100 - (len(rtt)/10)*100
print("Packet loss rate :", loss_rate,"%")