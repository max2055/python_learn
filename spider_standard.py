#test rdp
import urllib.request
import re<br>
#��¼�õ��ʻ���Ϣ
data={}
data['fromUrl']=''
data['fromUrlTemp']=''
data['loginId']='12345'
data['password']='12345'
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#��¼��ַ
#url='http://192.168.1.111:8080/loginCheck'
postdata = urllib.parse.urlencode(data) 
postdata = postdata.encode('utf-8')
headers = { 'User-Agent' : user_agent }
#��¼ 
res = urllib.request.urlopen(url,postdata)
#ȡ��ҳ��html<br>strResult=(res.read().decode('utf-8'))
#��������ʽȡ������A��ǩ
p = re.compile(r'<a href="(.*?)".*?>(.*?)</a>')
for m in p.finditer(strResult):
    print (m.group(1))#group(1)��href��������ݣ�group(2)��a��ǩ�������
    
    
    
    