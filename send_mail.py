import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def send(filename):
    from_mail = "palv499@gmail.com"
    to_mail = "19bece30204@gmail.com"
    subject = "Finance Stock Report"

    msg=MIMEMultipart()
    msg["From"] = from_mail
    msg["To"] = to_mail
    msg["Subject"] = subject

    body= "<b>Today's Stock Report</b>"
    msg.attach(MIMEText(body,"html"))

    my_file= open(filename,"rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition","attachment; filename= "+filename)
    msg.attach(part)




    message=msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_mail,'vdgtdizipdcgbdfv')


    server.sendmail(from_mail,to_mail,message)

    server.quit()