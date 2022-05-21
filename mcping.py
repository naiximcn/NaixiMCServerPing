'''
前言
----------
NaixiNana保留软件所有权利
本软件使用 GNUv3.0 协议开源
使用 多行注释的代码 都是屎山代码，别动
调用list.fansmc.com/api
logo解析暂时没写
----------
下方代码
----------
'''
print('程序启动')
print('预配置开始')
print('开始导入库')
#导入库
import requests
import time
import easygui
'''
import os
import base64
'''
print('库导入完毕')
print('开始定义方法')
#定义log方法
def log(text):
    #实时获取时间
    nowtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #输出
    print('[log] ['+
          nowtime+
          '] '+
          text)
#定义cdexit方法
def cxexit():
    log('主进程结束')
    log('3秒后开始退出')
    time.sleep(3)
    log('程序退出')
    '''
    exit()
    '''
    os.system('taskkill /f /im python.exe')
log('方法定义完毕')
log('预配置结束')
log('主进程开始')
#弹出窗口要求输入
'''
mcip=input('请输入IP:>  ')
'''
log('弹出窗口')
mcip=easygui.enterbox(msg='请输入服务器IP\n如 mc.hypixel.net',
                      title='NaixiMCServerPing-输入IP',
                      default='')
#检测IP是否为空
if mcip == '':
    log('服务器ip为空')
    log('弹出窗口')
    easygui.msgbox(msg='服务器ip为空!',
                   title='NaixiMCServerPing-IP为空',
                   ok_button='关闭')
    cxexit()
log('服务器IP获取完毕：'+mcip)
log('开始发送网络请求')
#发送网络请求到https://list.fansmc.com/api/<ip>
requestse=requests.get('https://list.fansmc.com/api/'+mcip)
log('已接受到返回信息')
#解析信息
log('开始解析信息')
mcrequestse=requestse.json()
#将解析结果str化(方便输出)
#退出
strmcrequestse=str(mcrequestse)
log('解析完毕，开始输出')
#输出解析信息
print('返回信息：'+strmcrequestse)
'''
print('服务器logo: '+str(base64.b64decode(mcrequestse['logo'])))
'''
print('服务器IP: '+mcip)
print('在线玩家数: '+str(mcrequestse['p'])+'/'+str(mcrequestse['mp']))
print('服务器motd: '+mcrequestse['motd'])
print('服务器mod数量: '+mcrequestse['mod'])
if mcrequestse['motd'] == '（此服务器离线或者服务器不存在）':
    log('此服务器不存在')
    log('弹出窗口')
    easygui.msgbox(msg='此服务器不存在或已离线！',
                   title='NaixiMCServerPing-不存在的服务器',
                   ok_button='关闭')
    cxexit()
#弹出窗口
log('弹出窗口')
easygui.msgbox(msg='解析完毕\n解析数据：\n服务器IP:'+
               mcip+'\n在线玩家数: '+
               str(mcrequestse['p'])+
               '/'+str(mcrequestse['mp'])+
               '\n服务器motd: '+
               mcrequestse['motd']+
               '\n服务器mod数量: '+
               mcrequestse['mod'],
               title='NaixiMCServerPing-解析结果',
               ok_button='关闭')
cxexit()