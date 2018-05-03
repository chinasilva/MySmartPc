#encoding:utf8
import itchat
import os
import time
import subprocess
import string
# import  xunfei 
import pydub
import win32api  
import re
import sqlite3
from itchat.content import *
from aip import AipSpeech
from PIL import ImageGrab
import cv2 #如果使用opencv的话可以远程拍照
from config import dis as myProgramConfig

APP_ID = '10760089'
API_KEY = 'xE18GKvn5jGokZgSPMHx81Aq'
SECRET_KEY = 'b10eecLu5padR82T49VNpBlSBxM45Rb0'

sendMsg = u"[消息助手]:暂时无法回复" #自动回复内容
usageMsg = u"使用方法：\n1.运行CMD命令\n2.获取一张图片:cap\n3.启用消息助手:ast\n4.关闭消息助手:astc\n"+"5.0.截屏:scr\n"+"5.百度:bd XXX\n"+u"6.语音(百度XXX)\n7.语音(打开XXX)"




flag = 0 #消息助手开关
filename ="备份.txt"
myfile = open(filename,'a')
            
@itchat.msg_register('Text') #注册文本消息

def text_replytext_reply(msg): #心跳程序
    global flag
    message =  msg['Text'] #接收文本消息
    fromName =msg['FromUserName'] #发送方
    toName = msg['ToUserName'] #接收方
    print('消息:',message,'发送方',fromName)
    if toName == "filehelper":
        if message[0]+message[1] =="bd":
            keyword = message.strip(message[0]+message[1]+message[2])
            win32api.ShellExecute(0, 'open', "http://www.baidu.com/s?wd=" + keyword, '', '', 1)   # 打开网页  
            # driver.get("http://www.baidu.com/s?wd=" + keyword)
        if message=="scr":#截屏给手机
            im = ImageGrab.grab()
            im.save('screenshot.png')
            itchat.send('@img@%s'%u'screenshot.png','filehelper')
            return
        if message == "cap": #远程拍照并发送到手机
            cap=cv2.VideoCapture(0)
            ret,img =cap.read()
            cv2.imwrite("weixinTemp.jpg",img)
            itchat.send('@img@%s'%u'weixinTemp.jpg','filehelper')
            cap.release()
            return
        if message[0]+message[1]+message[2] == "cmd": #远程执行cmd命令 
            os.system(message.strip(message[0]+message[1]+message[2]+message[3])) #远程执行cmd命令，可以实现关机
            return
        if message == "ast":
            flag = 1
            itchat.send("消息助手已开启","filehelper")
            return
        if message == "astc":
            flag = 0
            itchat.send("消息助手已关闭","filehelper")
            return
    elif flag==1:
        itchat.send(sendMsg,fromName)
        myfile.write(message) #保存消息内容
        myfile.write("\n")
        myfile.flush()


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    global flag
    message =  msg['Text'] #接收语音消息
    fromName =msg['FromUserName'] #发送方
    toName = msg['ToUserName'] #接收方
    
    if toName == "filehelper":
        msg['Text'](r'./Recording/'+ msg['FileName'])      #下载文件
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        # 将mp3格式转换为wav
        sound = pydub.AudioSegment.from_mp3(r'./Recording/'+msg['FileName'])
        sound.export(r'./Recording/'+msg['FileName'], format="wav")

        response=client.asr(getFileContent(r'./Recording/'+msg['FileName']), 'wav', 8000, {
        'lan': 'zh',})
        # 识别正确
        if response["err_no"]==0:
            words=response['result']
            if len(words)>0:
                word=words[0]
                # 去标点
                word=re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]", '', word)
                itchat.send(word + '\n' + '[消息助手]', "filehelper")
                print (response)
                # word = re.sub(r, '', word)
                print (word)
                # 百度搜索
                if word[0:2] == '百度':
                    print (123)
                    word = word[2:]
                    win32api.ShellExecute(0, 'open', "http://www.baidu.com/s?wd=" + word, '', '', 1)  # 打开网页
                    return
                if '打开' in word:
                    word=word[2:]
                    # 从Sqlite取值
                    # programConfig=getSqlite()
                    programConfig=myProgramConfig
                    for dic in programConfig:
                        if word == dic['PROGRAM_NAME']:
                            win32api.ShellExecute(0, 'open',dic['PROGRAM_PATH'], '', '', 1)  # 打开对应配置下的程序
                            itchat.send('程序名:'+dic['PROGRAM_NAME']+'\n'+'程序位置:'+dic['PROGRAM_PATH']+'\n'+'[消息助手]', "filehelper")
                    return

        else:
            itchat.send("识别错误","filehelper")

    elif flag==1:
        itchat.send(sendMsg,fromName)
        myfile.write(message) #保存消息内容
        myfile.write("\n")
        myfile.flush()
    
# 读取文件
def getFileContent(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 从Sqlite中读取配置的程序名称,返回字典类型
def getSqlite():
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    cursor = c.execute("SELECT ID, PROGRAM_NAME,PROGRAM_PATH  from PROGRAM_CONFIG")
    dics=cursor.fetchall()
    conn.close()
    return dics
# 查询结果保存在字典类型中
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def main():
    itchat.auto_login(hotReload=True)
    itchat.send(usageMsg,"filehelper")
    itchat.run()
if __name__ == '__main__':
    main()
