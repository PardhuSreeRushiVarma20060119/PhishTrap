#!/bin/bash

# Start MailHog in background
echo "Starting MailHog..."
MailHog > mailhog.log 2>&1 &

# Wait for it to start
sleep 2

# Show MailHog interface link
echo "📬 MailHog web UI: http://localhost:8025"

# Start Flask App
echo "🚀 Starting Flask app at http://127.0.0.1:5000 ..."
python app.py
