from tkinter import *
import tkinter.ttk as ttk
import smtplib
import random
import os
from email.header import Header
from email.mime.text import MIMEText







#窗口
window=Tk()
window.title("注册与登录")
window.geometry("500x600+600+400")
window.minsize(290,140)

# 登录
l1=Label(window,text="邮箱：",font=("Comic Sans MS",12))
l2=Label(window,text="密码：",font=("Comic Sans MS",12))

s1=ttk.Entry(window,textvariable=IntVar())
ss1=s1.get()










data=str(random.randrange(100000,999999))

subject='验证码' 


#文本
label1=Label(window,text="验证码：",font=("Comic Sans MS",12))
label2=Label(window,text="邮箱：",font=("Comic Sans MS",12))
#输入框
receivers1=ttk.Entry(window,textvariable=IntVar())
receivers=[receivers1.get()]

yzm=ttk.Entry(window,textvariable=IntVar())




def sendMail(data,receivers,subject):
        receivers=[receivers1.get()]
        print(receivers,type(receivers),receivers1.get())


  # 第三方 SMTP 服务
        mail_host="smtp.qq.com"  #设置服务器
        mail_user="123456789@qq.com"    # 发送邮箱
        mail_pass="zk*************he"   #口令 
        
        sender = '123456789@qq.com' # 发送邮箱
        

        message = MIMEText(data, 'plain', 'utf-8')
        message['From'] = Header("Python邮件", 'utf-8')
        
        message['Subject'] = Header(subject, 'utf-8')


        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    #端口
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print ("邮件发送成功")
            
            text1=Label(text='已发送',font=("Comic Sans MS",12))
            text1.place(relx=0.59,rely=0.3,anchor=CENTER)



        except smtplib.SMTPException:
            print ("Error: 无法发送邮件")
            text2=Label(text='发送失败',font=("Comic Sans MS",12))
            text2.place(relx=0.59,rely=0.3,anchor=CENTER)


def yz():
    if yzm.get()==data:
        text3=Label(text='注册成功',font=("Comic Sans MS",12))
        text3.place(relx=0.59,rely=0.3,anchor=CENTER)
    else:
        text4=Label(text='验证码错误',font=("Comic Sans MS",12))
        text4.place(relx=0.59,rely=0.3,anchor=CENTER)



#按键
press=Button(window,text="获取",font=("Comic Sans MS",12),command=lambda: sendMail(data,receivers,subject))
press2=Button(window,text="确定",font=("Comic Sans MS",12),command=yz)
#布局
label1.place(relx=0.22,rely=0.50,anchor=CENTER)
yzm.place(relx=0.52,rely=0.50,anchor=CENTER)
press2.place(relx=0.52,rely=0.70,anchor=CENTER)
label2.place(relx=0.22,rely=0.15,anchor=CENTER)
receivers1.place(relx=0.59,rely=0.17,anchor=CENTER)
press.place(relx=0.8,rely=0.17,anchor=CENTER)









l1.place(relx=0.22,rely=0.50,anchor=CENTER)
l2.place(relx=0.22,rely=0.70,anchor=CENTER)

s1.place(relx=0.59,rely=0.17,anchor=CENTER)

#保持
window.mainloop()

