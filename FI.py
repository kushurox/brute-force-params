#!/usr/bin/env python
import requests as rq
import sys
import getopt
import time


"""
Does not support multi Parameters right now.
Please do python3 FI -h for Help

"""

argumentList = sys.argv[1:]
arguments, _ = getopt.getopt(argumentList, 'hu:l:t:p:')
hm = {'-t': "0.8"}
for i, j in arguments:
    hm[i] = j


if '-h' in hm:
    print('Usage: FI -u <url> -l <wordlist> -p parameter \n-t OPTIONAL:[delay between each request]')
    exit()
responses = []

url = hm['-u']
try:
    wordlist = hm['-l']
except KeyError:
    print('-l is required.\n Please use -h to know how to use this')
    exit()

with open(wordlist, 'r') as fp:
    wl = fp.readlines()
for k in wl:
    responses.append(rq.post(url, params={hm['-p']: k}))
    time.sleep(float(hm['-t']))

