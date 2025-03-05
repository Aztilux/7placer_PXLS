import requests
import json

def getBoardData():
    Buffer = requests.get('https://pxls.space/boarddata', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'})
    return Buffer.content

def getInfo():
    Json = requests.get('https://pxls.space/info', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'})
    return json.loads(Json.content)