import csv
import smtplib
import json
from email.mime.text import MIMEText

def load_alerts(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def load_email_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def check_prices(alerts):
    results = []
    for alert in alerts:
        # Simulate a current price (replace this with real scraping or API)
        current_price = 10.00
        if current_price <= float(alert['target_price']):
            results.append((alert['title'], current_price, alert['aliexpress_url']))
    return results

def send_email(alerts, config):
    if not alerts:
        return
    body = "\n".join([f"{title} is now ${price:.2f}: {url}" for title, price, url in alerts])
    msg = MIMEText(body)
    msg['Subject'] = "AliExpress Price Alert"
    msg['From'] = config['from_email']
    msg['To'] = config['to_email']

    with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
        server.starttls()
        server.login(config['from_email'], config['password'])
        server.send_message(msg)

if __name__ == '__main__':
    alerts = load_alerts('alerts.csv')
    email_config = load_email_config('email_config.json')
    matched_alerts = check_prices(alerts)
    send_email(matched_alerts, email_config)
