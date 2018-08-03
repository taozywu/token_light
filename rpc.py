#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

url = "http://localhost:6332"
headers = {'content-type': 'application/json'}

def get_result(payload):
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    return json.dumps(response)

def get_all_address():
    payload = {
        "method": "getalladdress",
        "params": {},
        "jsonrpc": "2.0",
        "id": 1,
    }
    content = json.loads(get_result(payload))
    content=content["result"]
    address_arr=[]
    for (v) in content:
        address=v.split("-")[2]
        address_arr.append(address)
    return json.dumps(address_arr)


def get_balance():
    payload = {
        "method": "getbalance",
        "params": {},
        "jsonrpc": "2.0",
        "id": 1,
    }
    content = json.loads(get_result(payload))
    pending=content["result"]["base"]["pending"]
    stable=content["result"]["base"]["stable"]
    balance=pending+stable
    return json.dumps({"balance":balance,"pending":pending,"stable":stable})


def check_address(address):
    payload = {
        "method": "checkAddress",
        "params": [address],
        "jsonrpc": "2.0",
        "id": 1,
    }
    return get_result(payload)


def pay(address,amount,msg):
    if not msg:
        payload = {
            "method": "sendtoaddress",
            "params": [address,amount],
            "jsonrpc": "2.0",
            "id": 1,
        }
    else:
        payload = {
            "method": "sendtoaddresswithmessage",
            "params": [address,amount,msg],
            "jsonrpc": "2.0",
            "id": 1,
        }
    return get_result(payload)
