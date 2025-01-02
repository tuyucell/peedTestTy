import time
from emailer import send_email
from report_writer import write_report
from visualizer import create_latency_graph
import datetime

def generate_reports():
    today = datetime.date.today()

    # Günlük rapor
    print("Creating daily report...")
    daily_report_content = write_report(is_html=True)
    daily_graph_file_path = create_latency_graph()
    send_email(daily_report_content, graph_file_path=daily_graph_file_path, is_html=True)
    print("Daily report sent.")

    # Haftalık rapor (Pazar günleri)
    if today.weekday() == 6:
        print("Creating weekly report...")
        weekly_report_content = write_report(is_html=True)  # Haftalık rapor fonksiyonunu ekleyebilirsiniz
        send_email(weekly_report_content, is_html=True)
        print("Weekly report sent.")

    # Aylık rapor (Ayın ilk günü)
    if today.day == 1:
        print("Creating monthly report...")
        monthly_report_content = write_report(is_html=True)  # Aylık rapor fonksiyonunu ekleyebilirsiniz
        send_email(monthly_report_content, is_html=True)
        print("Monthly report sent.")

def main():
    while True:
        try:
            generate_reports()
        except Exception as e:
            print(f"Error occurred: {e}")
        print("Waiting for the next run...")
        time.sleep(86400)  # 1 gün (24 saat) bekleme

if __name__ == "__main__":
    main()