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
		'''发送无抄送名单的邮件'''
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
		'''发送有抄送名单的邮件'''
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

	def GetEmil(self,sender,subject):
		'''按发件人和主题获取邮件'''
		server = zmail.server(self.user,self.password,self.host)
		#获取邮箱信息
		mailbox_info = server.stat()
		print('邮件的数量：%s，邮箱的大小：%s' % mailbox_info)
		#获取邮件

		mails = server.get_mails(subject=subject,sender=sender)
		for mail in mails:
			print('ID:%s\n发件人：%s\n发送时间：%s\n邮件主题：%s\n邮件内容：%s\n附件：%s\n' % (mail['Id'],mail['From'],mail['Date'],mail['Subject'],mail['Content_text'],mail['Attachments']))
		return mails

	def GetEmil_id(self,n):
		'''获取第n封邮件'''
		server = zmail.server(self.user,self.password,self.host)
		#获取邮箱信息
		mailbox_info = server.stat()
		print('邮件的数量：%s，邮箱的大小：%s' % mailbox_info)
		#获取邮件
		mail = server.get_mail(n)
		zmail.show(mail)
		return mail

	def GetEmil_lastest(self):
		'''获取最新一封邮件'''
		server = zmail.server(self.user,self.password,self.host)
		#获取邮箱信息
		mailbox_info = server.stat()
		print('邮件的数量：%s，邮箱的大小：%s' % mailbox_info)
		#获取邮件
		mail = server.get_latest()
		for k,v in mail.items():
			print(k,v)
		return mail


if __name__ == '__main__':
	recipients=[('jimmy','jimmy_job@126.com')]
	subject='邮件主题'
	content='Dear all：\n邮件正文！'
	cc=['jimmy_job@126.com']
	attachments=['test.txt']

	eml=emlHandle(eml_username,eml_password,eml_host)
	#无抄送邮件
	eml.emilSend(recipients,subject,content,attachments)
	#有抄送邮件
	eml.emilSendCC(recipients,cc,subject,content,attachments)
	#获取邮件
	eml.GetEmil_lastest()


