"""
talk_spark.py

Description:

A utility program to communicate with Spark Core.

Website: electronut.in
"""

import argparse
import Queue
import threading
import time
import urllib2
import json
from sseclient import SSEClient

# list registered cores 
def listCores(access_token):
    baseURL = 'https://api.spark.io/v1/devices?access_token='
    fullURL = baseURL + access_token
    f = urllib2.urlopen(fullURL)
    f.close()
    print json.dumps(coreList, indent=4, sort_keys=True)


# worker thread method that fetches notifications
def fetchNotifications(q, access_token):
    baseURL = 'https://api.spark.io/v1/events/mycore_notify?access_token='
    fullURL = baseURL + access_token
    messages = SSEClient(fullURL)
    try:
        for msg in messages:
            strData = msg.data
                # skip empty messages
            if len(strData) > 0:
                # load to json object
                msgData = json.loads(strData)
                    #print(msgData)
                print('Notification: %s at %s' % (msgData['data'], 
                                                  msgData['published_at']))
    except KeyboardInterrupt:
        print('exiting.') 

# set up listening for notifications
def listen(access_token):
    q = Queue.Queue()
    t = threading.Thread(target=fetchNotifications, args=(q,access_token))
    t.daemon = True
    t.start()
    # loop 
    while True:
        try:
            # retrieve from queue
            if not q.empty():
                val = q.get()
                print(val)
                q.task_done()
            # sleep for a second
            time.sleep(1)
        except KeyboardInterrupt:
            print('exiting.') 
            break
    

# main() function
def main():
    # create parser
    descStr = "A utility program to communicate with Spark Core."
    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--at', dest='access_token', required=True)
    parser.add_argument('--list',dest='listCores',action='store_true')
    parser.add_argument('--listen',dest='listen',action='store_true')

    # parse args
    args = parser.parse_args()
    
    # list
    if args.listCores:
        coreList = listCores(args.access_token)
        print(coreList)

    # listen for notifications
    if args.listen:
        listen(args.access_token)
        
            
# call main
if __name__ == '__main__':
    main()
