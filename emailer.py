import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config import SMTP_CONFIG

def send_email(report_content, graph_file_path=None, is_html=False):
    config = SMTP_CONFIG

    # E-posta başlığı
    message = MIMEMultipart()
    message["From"] = config["from_email"]
    message["To"] = config["to_email"]
    message["Subject"] = "Daily Ping Report with Graph"

    # E-posta içeriği (HTML veya düz metin)
    if is_html:
        body = f"""
        <html>
        <body>
            <h1>Daily Ping Report</h1>
            <p>Here is the daily latency data:</p>
            <table border="1" style="border-collapse: collapse;">
                <thead>
                    <tr>
                        <th>Target</th>
                        <th>Average Latency (ms)</th>
                    </tr>
                </thead>
                <tbody>
                    {report_content}
                </tbody>
            </table>
        </body>
        </html>
        """
        message.attach(MIMEText(body, "html"))
    else:
        message.attach(MIMEText(report_content, "plain"))

    # Grafik dosyasını e-posta ekine ekle
    if graph_file_path:
        with open(graph_file_path, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={graph_file_path.split('/')[-1]}",
            )
            message.attach(part)

    # SMTP sunucusuna bağlan ve e-posta gönder
    try:
        with smtplib.SMTP_SSL(config["host"], config["port"]) as server:
            server.login(config["username"], config["password"])
            server.sendmail(config["from_email"], config["to_email"], message.as_string())
        print("Mail sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")