import configparser
from bilibiliupload import *
import os
import requests

#log 初始化
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='Uploader.log', level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

#读取config文件
def getConfig(section, key):
    config = configparser.ConfigParser()
    configpath =  './Uploader.conf'
    config.read(configpath,'utf-8')
    return config.get(section, key)
#上传
def UploadFile(file):
    VP = VideoPart(path+'/'+file,file[5:11],file[5:11]+'录像')
    if file == 'file'+type:
        print('dupe file')
        #我也不知道为啥会重复上传,打个特判
    else:
        b = Bilibili()
        b.login(username, password)
        PartTitle = title + file[5:13]# time.strftime("%m-%d-%H", time.localtime())
        logging.info("login successful, begin uploading"+PartTitle)
        print("login successful, begin uploading"+PartTitle)
        b.upload(VP, PartTitle, tid, tag, desc, dynamtic)
        logging.info("finish uploading "+PartTitle)
        print("finish uploading "+PartTitle)


VideoPartList = []
#读取相对路径和录像文件名词
path = getConfig('Common','path')
type = getConfig('Common','type')
#读取监听的B站直播间
room_id = int(getConfig('BilibiliLive','room_id'))
#读取用户名和密码,以及B站上传设置
username = getConfig('Bilibili','username')
password = getConfig('Bilibili','password')
title = getConfig('Bilibili','title')
tid = int(getConfig('Bilibili','tid'))
tag = getConfig('Bilibili','tag').split(',')
desc = getConfig('Bilibili','desc')
dynamtic = getConfig('Bilibili','dynamtic')
#log 读取的数据
logging.debug("Readed"+"path: "+path+' type: '+type+' room_id: '+str(room_id)+' username: '+username+' password: '+ password +' title: '+title)
logging.debug("Readed"+"tid: "+str(tid)+' tag: '+str(tag)+' desc: '+desc+' dynamtic: '+dynamtic+' From the config file')

#暴力死循环
while(True):
        files = os.listdir(path)
        #遍历录像目录
        for file in files:
            #寻找指定类型的录像文件
            if file.endswith(type):
                #检测录像文件体积编号
                tmpsizeA = os.path.getsize(path+'/'+file)
                time.sleep(10)
                tmpsizeB = os.path.getsize(path+'/'+file)
                #如果录像体积无变化,开始上传
                if tmpsizeA == tmpsizeB:
                    UploadFile(file)
                    logging.info("delete uploaded file" + file)
                    print("delete uploaded file" + file)
                    os.remove(path + '/' + file)
                    print(os.listdir(path))
                else:
                    print("This video file is writing while streaming, do nothing")
        time.sleep(200)









"""
def getVcount(UID):
  
      UID: UP主的ID
      :return: 返回视频数量
      
    url = "http://space.bilibili.com/ajax/member/getSubmitVideos"
    p = {'mid':UID,'pagesize':1,'page':1}
    r = requests.get(url,p)
    data = json.load(r)
    return data['count']
def getVList(UID):
  
    UID: UP主的ID
    :return: 返回视频列表
    
    url = "http://space.bilibili.com/ajax/member/getSubmitVideos"
    videocount = getVcount(UID)
    pages = math.ceil(videocount/100)
    vList = []
    for page in range(0,pages):
        p = {'mid': UID, 'pagesize': 100, 'page': page+1}
        r = requests.get(url, p)
        data = json.load(r)
        vList += data['vlist']
    return vList
#监听直播状态, 0下播 1开播
def GetLiveStates(id):
    Room = {'room_id': id}
    RoomInfo = requests.get("https://api.live.bilibili.com/room/v1/Room/get_info", params=Room)
    states =  RoomInfo.json()['data']['live_status']
    return states
"""