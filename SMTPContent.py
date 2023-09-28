from socket import *
import smtplib
import ssl
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
msg=MIMEMultipart('related')
endmsg = "\r\n.\r\n"
msg['subject']='test'
