'''
The multicast main source is from the internet search, maybe
https://pymotw.com/2/socket/multicast.html

Use python3 because of encoding issue.
When run, the first packet makes the error.
And, it's the expected behavior.
'''

import socket, struct, sys, datetime

old=1
data2 = 1

multicast_group = '224.3.29.72'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
while True:
    data, address = sock.recvfrom(1024)
    data2 = int(data)
    
    if data2 == old :
        print ("R5 REC 72 okay", data, "   ", datetime.datetime.now())
    else:
        print ("R5 REC 72 #### wrong ####", "Arrived ", data, "expected ", old, datetime.datetime.now())

    old = data2 + 1


'''


wankim@WANKIM-M-P1E1 050-multicast-tester % python3 52-recieve.py 
R5 REC 72 #### wrong #### Arrived  b'10' expected  1 2023-03-05 14:05:28.793684
R5 REC 72 okay b'11'     2023-03-05 14:05:29.296509
R5 REC 72 okay b'12'     2023-03-05 14:05:29.799476
R5 REC 72 okay b'13'     2023-03-05 14:05:30.304213
R5 REC 72 okay b'14'     2023-03-05 14:05:30.808921
R5 REC 72 okay b'15'     2023-03-05 14:05:31.310452
R5 REC 72 okay b'16'     2023-03-05 14:05:31.812915
R5 REC 72 okay b'17'     2023-03-05 14:05:32.316454
R5 REC 72 okay b'18'     2023-03-05 14:05:32.821365
çR5 REC 72 okay b'19'     2023-03-05 14:05:33.324583
R5 REC 72 okay b'20'     2023-03-05 14:05:33.828619
R5 REC 72 okay b'21'     2023-03-05 14:05:34.329245
R5 REC 72 okay b'22'     2023-03-05 14:05:34.830367
R5 REC 72 okay b'23'     2023-03-05 14:05:35.331593
R5 REC 72 okay b'24'     2023-03-05 14:05:35.835121
R5 REC 72 okay b'25'     2023-03-05 14:05:36.339474
R5 REC 72 okay b'26'     2023-03-05 14:05:36.840187
R5 REC 72 okay b'27'     2023-03-05 14:05:37.344531
^CTraceback (most recent call last):
  File "/Users/wankim/Documents/Py/yamebook2_youtube_not_git/050-multicast-tester/52-recieve.py", line 32, in <module>
    data, address = sock.recvfrom(1024)
KeyboardInterrupt

wankim@WANKIM-M-P1E1 050-multicast-tester % 
'''