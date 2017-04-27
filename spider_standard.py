#test rdp
import urllib.request
import re<br>
#登录用的帐户信息
data={}
data['fromUrl']=''
data['fromUrlTemp']=''
data['loginId']='12345'
data['password']='12345'
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#登录地址
#url='http://192.168.1.111:8080/loginCheck'
postdata = urllib.parse.urlencode(data) 
postdata = postdata.encode('utf-8')
headers = { 'User-Agent' : user_agent }
#登录 
res = urllib.request.urlopen(url,postdata)
#取得页面html<br>strResult=(res.read().decode('utf-8'))
#用正则表达式取出所有A标签
p = re.compile(r'<a href="(.*?)".*?>(.*?)</a>')
for m in p.finditer(strResult):
    print (m.group(1))#group(1)是href里面的内容，group(2)是a标签里的文字
    
    
    
    