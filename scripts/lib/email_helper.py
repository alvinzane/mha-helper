# -*- coding: UTF-8 -*-
# (c) 2013, Ovais Tariq <ovaistariq@gmail.com>
#
# This file is part of mha-helper
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import socket
import smtplib
from email.mime.text import MIMEText

class Email_helper(object):
    SMTP_HOST = "smtp.163.com"  #更改为真实的smtp服务器
    MAIL_USER = "wubingxi@163.com" #更改为自已的邮箱 
    MAIL_PASS = "xxxxxxxxx"   #更改为邮箱密码
    SENDER = "%s" % (MAIL_USER)

    def __init__(self):
        #self._email_sender = smtplib.SMTP(Email_helper.SMTP_HOST)
	self._email_sender = smtplib.SMTP()

    def send_email(self, subject, msg, to_email_list):
        if len(to_email_list) < 1:
            return False

        #email_msg = MIMEText(msg)
	email_msg = MIMEText(msg,_subtype='plain',_charset='gb2312')  
        email_msg['Subject'] = subject
        email_msg['From'] = Email_helper.SENDER
        email_msg['To'] = ';'.join(to_email_list)
	me = "%s<%s>" %(subject, Email_helper.SENDER)
	try:
		email_sender = smtplib.SMTP()
		email_sender.connect(Email_helper.SMTP_HOST)
		email_sender.login(Email_helper.MAIL_USER, Email_helper.MAIL_PASS)
		email_sender.sendmail(me, to_email_list,email_msg.as_string())
		email_sender.close()
        	return True
	except Exception, e:
			print str(e)
			print "error"
			return False
'''
if __name__ == '__main__':
	report_email_list=['wubingxi@gmail.com']
	Email_sender = Email_helper()
	Email_sender.send_email(subject="mha test", msg="hello world",to_email_list=report_email_list)
'''
