import requests,os,time,base64,easygui
#mcip=input('请输入IP:>  ')
mcip=easygui.enterbox(msg='请输入服务器IP\n如 mc.hypixel.net',title='NaixiMCServerPing-输入IP',default='')
requestse=requests.get('https://list.fansmc.com/api/'+mcip)
mcrequestse=requestse.json()
strmcrequestse=str(mcrequestse)
print('解析完毕')
print('返回信息：'+strmcrequestse)
#print('服务器logo: '+str(base64.b64decode(mcrequestse['logo'])))
print('服务器IP: '+mcip)
print('在线玩家数: '+str(mcrequestse['p'])+'/'+str(mcrequestse['mp']))
print('服务器motd: '+mcrequestse['motd'])
print('服务器mod数量: '+mcrequestse['mod'])
easygui.msgbox(msg='解析完毕\n解析数据：\n服务器IP:'+
               mcip+'\n在线玩家数: '+
               str(mcrequestse['p'])+
               '/'+str(mcrequestse['mp'])+
               '\n服务器motd: '+
               mcrequestse['motd']+
               '\n服务器mod数量: '+
               mcrequestse['mod'],
               title='NaixiMcServerPing-解析结果',
               ok_button='关闭')
os.system('pause')
time.sleep(3)
exit
