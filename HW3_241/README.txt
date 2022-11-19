=========== Task 1 ===============
Q1.
mininet> nodes
h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7

mininet> net
h1 h1-eth0:s3-eth2
h2 h2-eth0:s3-eth3
h3 h3-eth0:s4-eth2
h4 h4-eth0:s4-eth3
h5 h5-eth0:s6-eth2
h6 h6-eth0:s6-eth3
h7 h7-eth0:s7-eth2
h8 h8-eth0:s7-eth3
s1 lo:  s1-eth1:s2-eth1 s1-eth2:s5-eth1
s2 lo:  s2-eth1:s1-eth1 s2-eth2:s3-eth1 s2-eth3:s4-eth1
s3 lo:  s3-eth1:s2-eth2 s3-eth2:h1-eth0 s3-eth3:h2-eth0
s4 lo:  s4-eth1:s2-eth3 s4-eth2:h3-eth0 s4-eth3:h4-eth0
s5 lo:  s5-eth1:s1-eth2 s5-eth2:s6-eth1 s5-eth3:s7-eth1
s6 lo:  s6-eth1:s5-eth2 s6-eth2:h5-eth0 s6-eth3:h6-eth0
s7 lo:  s7-eth1:s5-eth3 s7-eth2:h7-eth0 s7-eth3:h8-eth0

Q2.
h7-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::f091:1cff:fe4f:f60b  prefixlen 64  scopeid 0x20<link>
        ether f2:91:1c:4f:f6:0b  txqueuelen 1000  (Ethernet)
        RX packets 140  bytes 10820 (10.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 11  bytes 866 (866.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


=========== Task 2 ===============
Q1.
_handle_PacketIn() -> act_like_hub() -> resend_packet()

Q2.
a. "h1 ping h2" Avg: 3.484 ms | "h1 ping h8" Avg: 8.568 ms
b. "h1 ping h2" Min: 0.760 ms, Max: 7.179 ms | "h1 ping h8" Min: 4.576 ms, Max: 12.737 ms
c. "h1 ping h2" is faster than "h1 ping h8". It is because there are less switches and hops between h1 and h2 comparing to h1 and h8. 

Q3.
a. iperf is used to measure network performance and tuning. It tests TCP bandwidth.
b. "iperf h1 h2" results: ['29.5 Mbits/sec', '33.7 Mbits/sec'] | "iperf h1 h8" results: ['4.35 Mbits/sec', '4.74 Mbits/sec']
c. "iperf h1 h2" is better than "iperf h1 h8". It may due to that it has shorter route between h1 and h2, and it has quicker return time. There is also many other factors that may affect the bandwidth.

Q4.
I tested with "h1 h2" and "h1 h8". All switches got traffic. In "h1 h2", s3 observed traffic. In "h1 h8", s1, s2, s3, s5, s7 observed traffic. The way for observing is that I added a print statement inside _handle_PacketIn function to print the switch and packet's source & destination.


=========== Task 3 ===============
Q1.
The code is working as following:
Every time when a new source arrive at a switch and if it is not in map, it will inserts it into the map with packet.src as key and port as value. After that, it will check if destination is in the map. If the destination is in the map, it will send the packet directly to the port associate with it using resend_packet() function. If the destination is not in the map, it will flood the packet to all ports except the input port.

Q2.
a. "h1 ping h2" Avg: 3.937 ms | "h1 ping h8" Avg: 8.131 ms
b. "h1 ping h2" Min: 1.560 ms, Max: 6.137 ms | "h1 ping h8" Min: 4.305 ms, Max: 14.573 ms
c. The difference is that the results in task 3 are better than results in task 2. The avg/min/max ping are all decreased. it is due to the map that could learn and improve the performance. Every time the map will learn and store the information, and use it to expedite the process. And for h1 and h2, the time increased. One reason is that there is no need to use map to store informations between nodes for short distance.
 

Q3.
a. "iperf h1 h2" results: ['32.5 Mbits/sec', '36.8 Mbits/sec'] | "iperf h1 h8" results: ['4.57 Mbits/sec', '5.14 Mbits/sec']
b. 
Overall, the throughputs of task 3 increase and are better than the throughputs of tasks 2. It is due to the same reason of Q2, and it is more efficient when using the map to learn instead of flood packets to the network for long distance.


