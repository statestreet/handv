#coding=utf-8
#导入smtplib和MIMEText
import smtplib
from email.mime.text import MIMEText
from email.Header import Header
from email.MIMEMultipart import MIMEMultipart
#############
#要发给谁，这里发给2个人
mailto_list=["yixiugg@gmail.com"]
#####################
#设置服务器，用户名、口令以及邮箱的后缀
mail_host="smtp.126.com"
mail_user="yixiugg"
mail_pass="87931517"
mail_postfix="126.com"
######################
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,'html') #实例化为html部分
    msg.set_charset('utf-8') #设置编码
    msg['Subject'] =  Header(sub,'utf-8') #组装信头
    msg['From'] = r'%s <%s>' %(me,Header('h&v,一休和老刘的小窝','utf-8')) 
    msg['To'] = ";".join(to_list)
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user,mail_pass)
    s.sendmail(me, to_list, msg.as_string())
    s.close()
if __name__ == '__main__':
    if send_mail(mailto_list,"subject","content"):
        print "发送成功"
    else:
        print "发送失败"