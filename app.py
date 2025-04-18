from flask import Flask, render_template, request, redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ──────── Level 1 ────────
@app.route('/level1', methods=['GET', 'POST'])
def level1():
    if request.method == 'POST':
        # 🔁 Optional: Use this to simulate mail delivery
        # send_phish_mail("rohit.verma@catchmail.local", "Phishing Subject", "Phishing Body", "Hacker Name")
        return redirect('/level1_flag')
    return render_template('level1.html')  # Login page for Level 1

@app.route('/level1_flag')
def level1_flag():
    return render_template('level1_flag.html')

# ──────── Level 2 ────────
@app.route('/level2_slack', methods=['GET', 'POST'])
def level2_slack():
    if request.method == 'POST':
        return redirect('/level2_drive')
    return render_template('level2_slack.html')  # Fake Slack login

@app.route('/level2_drive', methods=['GET', 'POST'])
def level2_drive():
    if request.method == 'POST':
        return redirect('/level2_flag')
    return render_template('level2_drive.html')  # Fake Drive login

@app.route('/level2_flag')
def level2_flag():
    return render_template('level2_flag.html')

# ──────── Level 3 ────────
@app.route('/level3_invite', methods=['GET', 'POST'])
def level3_invite():
    if request.method == 'POST':
        return redirect('/level3_portal')
    return render_template('level3.html')  # Fake calendar/invite page

@app.route('/level3_portal', methods=['GET', 'POST'])
def level3_portal():
    if request.method == 'POST':
        return redirect('/level3_flag')
    return render_template('level3_portal.html')  # Fake internal admin portal

@app.route('/level3_flag')
def level3_flag():
    return render_template('level3_flag.html')

# Mailer 
@app.route('/send_mail', methods=['GET', 'POST'])
def send_mail():
    targets = {
        "rohit": "rohit.verma@catchmail.local",
        "anita": "anita.deshmukh@catchmail.local",
        "karthik": "karthik.iyer@catchmail.local"
    }
    
    if request.method == 'POST':
        target_key = request.form.get('target')
        subject = request.form.get('subject')
        body = request.form.get('body')
        sender = request.form.get('sender')
        
        if target_key in targets:
            to_email = targets[target_key]
            
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = f"{sender} <no-reply@phishlab.io>"
            msg['To'] = to_email
            msg.set_content(body)
            
            with smtplib.SMTP('localhost', 1025) as smtp:
                smtp.send_message(msg)

            return render_template('mail_sent.html', target=to_email)

    return render_template('send_mail.html')

if __name__ == '__main__':
    app.run(debug=True)
