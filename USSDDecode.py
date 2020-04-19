#!/usr/bin/python3
# -*- coding: utf8 -*-

import time
import serial

def USSDDecode():
    rep = phone.read_until('\n').decode('latin1', "replace")
    #print(rep)

    if rep.find("+CUSD: 0") >=0:
        #print("0")
        rep0 = rep[rep.find("+CUSD: ")+len("+CUSD: 0, \""):len(rep)-7]
        try:
            int(rep0, 16)
            #print ('it is hex')
            rep0 = bytes.fromhex(rep0).decode('latin1', "replace")
            rep0 = rep0.replace(chr(00), "")
            #print(rep0)
            rep=rep0
        except ValueError:
            #print ('it is not hex')
            #print(rep0)
            rep=rep0
    elif rep.find("+CUSD: 1") >=0:
        #print("1")
        rep1 = rep[rep.find("+CUSD: ")+len("+CUSD: 1,\""):len(rep)-7]
        try:
            int(rep1, 16)
            #print ('it is hex')
            rep1 = bytes.fromhex(rep1).decode('latin1', "replace")
            rep1 = rep1.replace(chr(00), "")
            #print(rep1)
            rep=rep1
        except ValueError:
            #print ('it is not hex')
            #print(rep1)
            rep=rep1
    elif rep.find("+CUSD: 2") >=0:
        #print("2")
        rep="Not supported by network"
    return rep

phone = serial.Serial("COM14",  115200, timeout=2)
phone.flushInput()
phone.flushOutput()

phone.write(b'AT')
time.sleep(1)

phone.write(b'AT+CFUN=1')
time.sleep(1)

rep = phone.read_until('\n').decode('latin1', "replace")
#print(rep)
try:
    phone.write(b'ATZ\r')
    time.sleep(0.5)
    rep = phone.read_until('\n').decode('latin1', "replace")
    print(rep)
    
    phone.write(b'ATE1\r')
    time.sleep(0.5)
    rep = phone.read_until('\n').decode('latin1', "replace")
    print(rep)
    
    phone.write(b'AT+CUSD=1,"*123#",15\r')
    time.sleep(2)
    print(USSDDecode())
    phone.flush()
    
    phone.write(b'AT+CUSD=1,"*101#",15\r')
    time.sleep(2)
    print(USSDDecode())
    phone.flush()

    phone.write(b'AT+CUSD=1,"*110#",15\r')
    time.sleep(2)
    print(USSDDecode())
    phone.flush()
    
    phone.write(b'AT+CUSD=1,"2"\r')
    time.sleep(2)
    print(USSDDecode())
    phone.flush()
    
    phone.write(b'AT+CUSD=1,"1"\r')
    time.sleep(2)
    print(USSDDecode())
    phone.write(bytes([26]))
    
    phone.flushInput()
    phone.flushOutput()
    time.sleep(.5)

finally:
    phone.close()
