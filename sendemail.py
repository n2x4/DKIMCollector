import smtplib
import datetime
from email.mime.text import MIMEText

# Set up the SMTP server
server = smtplib.SMTP('smtp.server.com')

# Start secure connection
server.starttls()

# Authenticate
username = "sender@email.com"
password = "password"
server.login(username, password)

# Build the email message
now = datetime.datetime.now()
subject = f"DKIM Collector Report {now.strftime('%Y-%m-%d')}"
body = "This is the daily DKIM Collector report"
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = username
msg['To'] = "recipient@email.com"

# Send the email
server.sendmail(username, "recipeint@email.com", msg.as_string())

# Disconnect from the server
server.quit()
