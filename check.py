#!/usr/bin/python
# -*- coding: UTF-8 -*-
import rpc,json
import time

while(True):
    new_blance=(json.loads(rpc.get_balance()))["pending"]

    print (new_blance)

    if new_blance==0:
        print ("off")
        time.sleep(2)
    else:
        print ("on")
        time.sleep(new_blance)


    
