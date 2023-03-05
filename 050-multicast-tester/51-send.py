'''
The multicast main source is from the internet search, maybe
https://pymotw.com/2/socket/multicast.html

Use python3 because of encoding issue.
'''

import socket, struct, sys, datetime, time

i = 0
message = 'very important data'

multicast_group = ('224.3.29.72', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 10)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Send data to the multicast group
while 1>0:
 message = bytes (str(i), 'utf-8')
 print ( "send 72", i, datetime.datetime.now() )
 sent = sock.sendto(message, multicast_group)
 time.sleep(0.5)
 i = i + 1

'''
wankim@WANKIM-M-P1E1 050-multicast-tester % ls
51-send.py	52-recieve.py
wankim@WANKIM-M-P1E1 050-multicast-tester % python3 51-send.py 
send 72 0 2023-03-05 14:05:23.754918
send 72 1 2023-03-05 14:05:24.257667
send 72 2 2023-03-05 14:05:24.762620
send 72 3 2023-03-05 14:05:25.265432
send 72 4 2023-03-05 14:05:25.770360
send 72 5 2023-03-05 14:05:26.273598
send 72 6 2023-03-05 14:05:26.777773
send 72 7 2023-03-05 14:05:27.282058
send 72 8 2023-03-05 14:05:27.786595
send 72 9 2023-03-05 14:05:28.289588
send 72 10 2023-03-05 14:05:28.791364
send 72 11 2023-03-05 14:05:29.296284
send 72 12 2023-03-05 14:05:29.799259
send 72 13 2023-03-05 14:05:30.304005
send 72 14 2023-03-05 14:05:30.808698
send 72 15 2023-03-05 14:05:31.310235
send 72 16 2023-03-05 14:05:31.812616
send 72 17 2023-03-05 14:05:32.316240
send 72 18 2023-03-05 14:05:32.821174
send 72 19 2023-03-05 14:05:33.324337
send 72 20 2023-03-05 14:05:33.828349
send 72 21 2023-03-05 14:05:34.328949

'''