import socket as soc
import threading as thread
import os
import pyfiglet
os.system("cls")

os.system("color 6")
title = pyfiglet.figlet_format("\t ! WELCOME TO MY UDP CHAT APP FROM WINDOWS ! \n")
print( title)
print(" \n ##################################################################### \n")
print("\t\t SO FRIEND LET'S START OUR CHATTING \n")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ \n")

your_ip = input("ENTER THE YOUR IP ADDRESS HERE : ")

your_port = int(input("ENTER THE YOUR PORT NUMBER HERE : "))

frd_ip = input("ENTER THE FRIEND IP ADDRESS HERE :")

frd_port = int(input("ENTER THE FRIEND PORT NUMBER HERE : "))
print("\n")        

# TO CREATE A SOCKET AND BIND THE IP AND PORT NUMBER : 

skt1 = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
skt1.bind((your_ip, your_port))


# WE CAN USE THIS FUNCTION TO RECEIVING AND PRINTING THE MESSAGE :

def recieve_msg():
    while True:
        os.system("color 5")
        msgRcv = skt1.recvfrom(1024)
        if msgRcv[0].decode() == "quit" or msgRcv[0].decode() == "bye bye" or msgRcv[0].decode() == "exit":
            print("NOW YOUR FRIEND GOES OFFLINE!")
            os._exit(1)
        print("\n\t\t\t YOUR FRIEND'S MSG --->" + msgRcv[0].decode())


# WE CAN USE THIS FUNCTION TO SENDING THE MESSAGE :

def send_msg():
    while True:
        data = input().encode()
        msgSent = skt1.sendto(data, (frd_ip, frd_port))
        if data.decode() == "quit" or data.decode() == "bye bye" or data.decode() == "exit":
            os._exit(1)

# WE CAN USE THIS THREAD FOR SENDING THE MESSAGE FUNCTION :
t1= thread.Thread(target=send_msg)

# WE CAN USE THIS THREAD FOR RECIEVING THE MESSAGE FUNCTION :
t2 = thread.Thread(target=recieve_msg)

# WE CAN USE THIS FUNCTION TO STARTING OUR THREADS :
t1.start()
t2.start()

