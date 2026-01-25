from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os



# ---------------- ENV VARIABLES (FROM GITHUB SECRETS) ----------------

SMTP_USER = os.getenv("EMAIL_USER")       # MailerSend SMTP username
SMTP_PASS = os.getenv("EMAIL_PASS")       # MailerSend SMTP password
SENDER_EMAIL = os.getenv("SENDER_EMAIL")  # Verified sender email address

# ---------------- LOAD CONTENT FILES ----------------

with open("quotes_motivate.txt", encoding="utf-8") as f:
    quotes = f.readlines()

with open("pythontips.txt", encoding="utf-8") as f:
    tips = f.readlines()

with open("dsaproblemssample.txt", encoding="utf-8") as f:
    dsa = f.readlines()

# ---------------- INDEX HANDLING ----------------

if not os.path.exists("index.txt"):
    with open("index.txt", "w") as f:
        f.write("0")

with open("index.txt") as f:
    index = int(f.read().strip())

max_len = min(len(quotes), len(tips), len(dsa))
index = index % max_len

quote = quotes[index].strip()
tip = tips[index].strip()
dsa_problem = dsa[index].strip()

with open("index.txt", "w") as f:
    f.write(str(index + 1))

# ---------------- FRIENDS ----------------

recipients = [
    "nathivinodkumar23@gmail.com",
    "nathivinodkumar0230@gmail.com",
    "jenigavinay973@gmail.com",
    "pavaninaik2k5@gmail.com",
    "shivachaturvedi145@gmail.com",
    "nagoluhemanthreddy@gmail.com",
    "chinnasaketh2@gmail.com",
    "saicharankasarapu2004@gmail.com",
    "yvignesh20@gmail.com",
    "siddubhukya725@gmail.com",
    "prashanthreddy3748@gmail.com",
    "boyavishnu86@gmail.com",
    "anithakatravath53@gmail.com",
    "nithinmalavath3233@gmail.com",
    "ruthikeswar21@gmail.com",
    "sandeepkumarpittala7@gmail.com",
]

# ---------------- EMAIL CONTENT ----------------

subject = "Today’s thought & challenge"

body = f"""
🌅 Motivation
{quote}

💡 Skill Tip
{tip}

🧠 DSA Challenge
{dsa_problem}
"""

# ---------------- SEND EMAILS (MAILERSEND SMTP) ----------------

with smtplib.SMTP("smtp.mailersend.net", 587) as server:
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)

    for recipient in recipients:
        msg = MIMEMultipart()
        
        msg["From"] = "VinodKumarNathi <{}>".format(SENDER_EMAIL.strip())

        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain", "utf-8"))


        server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
