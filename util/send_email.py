#coding:utf-8
import smtplib
from email.mime.text import MIMEText
class SendEmail:
	global send_user
	global email_host
	global password
	email_host = "smtp.163.com"
	send_user = "chenzhongren123456@163.com"
	#todo  使用账户密码可能授权失败，改为授权码，参考连接
	#https://jingyan.baidu.com/article/c275f6ba33a95de33d7567d9.html
	password = "OFPKUVWZEHMKVVMW"
	def send_mail(self,user_list,sub,content):
		user = "13023294697"+"<"+send_user+">"
		message = MIMEText(content,_subtype='plain',_charset='utf-8')
		message['Subject'] = sub
		message['From'] = user
		message['To'] = ";".join(user_list)
		server = smtplib.SMTP()
		server.connect(email_host)
		server.login(send_user,password)
		server.sendmail(user,user_list,message.as_string())
		server.close()

	def send_main(self,pass_list,fail_list):
		pass_num = float(len(pass_list))
		fail_num = float(len(fail_list))
		count_num = pass_num+fail_num
		#90%
		pass_result = "%.2f%%" %(pass_num/count_num*100)
		fail_result = "%.2f%%" %(fail_num/count_num*100)

		user_list = '810483775@qq.com'
		sub = 'ceshi'
		content = "此次一共运行接口个数为%s个，通过list为%s，失败list为%s，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num,pass_list,fail_list,pass_num,fail_num,pass_result,fail_result )
		self.send_mail(user_list,sub,content)

if __name__ == '__main__':
	sen = SendEmail()
	# user_list = '810483775@qq.com'
	# sub = 'ceshi'
	# content = '测试邮箱'
	# sen.send_mail(user_list,sub,content)
	sen.send_main([1,2],[4,5,6,7])