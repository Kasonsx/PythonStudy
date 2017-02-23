import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'sxk644653293@163.com'
password = input('Password:')
to_addr = '895969293@qq.com'
stmp_server = 'smtp.163.com'

msg = MIMEText('hello!', 'plain', 'utf-8')
msg['From'] = format_addr('send testing <%s>' % from_addr)
msg['To'] = format_addr('accept testing <%s>' % to_addr)
msg['Subject'] = Header('python smtp send email', 'utf-8').encode()

server = smtplib.SMTP(stmp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr,msg.as_string())
server.quit()
