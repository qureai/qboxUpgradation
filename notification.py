import os, sys
from slack_sdk import WebClient

secret='zqzd/422:3886322/68:36:55:6:3:/\QZ5JZGUd;:8OVLpex;urHcY'
new=''
for s in secret:
    new+=chr(ord(s)-2)
client = WebClient(token=new)

message=sys.argv[1]


client.chat_postMessage(channel='#qbox-upgradation-status',text=message)