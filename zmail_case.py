#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2020年9月17日
@author: yuejing
'''
#https://github.com/ZYunH/zmail/

import zmail
class emlHandle:
	def __init__(self,user,password,host):
		self.host=host
		self.user=user
		self.password=password

	def emilSend(self,recipients,subject,contents,attachment=''):
		server = zmail.server(self.user,self.password,self.host)
		mail = {
		    'subject': subject,  
		    'content_text': contents,  
		    'attachments': attachment,  
		}
		try:
			server.send_mail(recipients,mail)
			print('邮件发送成功！')
		except Exception as e:
			print('邮件发送失败！')
			raise e

	def emilSendCC(self,recipients,cc,subject,contents,attachment=''):
		server = zmail.server(self.user,self.password,self.host)
		mail = {
		    'subject': subject,  
		    'content_text': contents,  
		    'attachments': attachment,  
		}
		try:
			server.send_mail(recipients,mail,cc)
			print('邮件发送成功！')
		except Exception as e:
			print('邮件发送失败！')
			raise e

if __name__ == '__main__':
	recipients=[('jimmy1','jimmy1@emil.com'),'jimmy2@emil.com']
	subject='邮件主题'
	content='Dear all：\n邮件正文！'
	cc=['jimmy1@emil.com','jimmy2@emil.com']
	attachments=['test.txt','测试.png']
	#无抄送邮件
	emlHandle(emil_user,emil_password,emil_host).emilSend(recipients,subject,content,attachments)
	#有抄送邮件
	emlHandle(emil_user,emil_password,emil_host).emilSendCC(recipients,cc,subject,content,attachments)





