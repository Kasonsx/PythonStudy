from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

import smtplib

from_addr = 'sxk644653293@163.com'
to_addr = '895969293@qq.com'
password = input('Password:')
smtp_server = 'smtp.163.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr))

msg = MIMEText('Hello from Python', 'plain', 'utf-8')
msg['From'] = _format_addr('Send testing: <%s>' % from_addr)
msg['To'] = _format_addr('Receive testing: <%s>' % to_addr)
msg['Subject'] = Header('Python Email Testing', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()