import sqlite3
import datetime

DB_FILE = "ping_data.db"

def write_report(is_html=False):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today()
    start = f"{today} 00:00:00"
    end = f"{today} 23:59:59"
    cursor.execute('''
        SELECT target, AVG(latency) as avg_latency
        FROM ping_data
        WHERE timestamp BETWEEN ? AND ?
        GROUP BY target
    ''', (start, end))
    report = cursor.fetchall()
    conn.close()

    # Raporu HTML veya düz metin olarak oluştur
    if is_html:
        report_content = ""
        for row in report:
            report_content += f"<tr><td>{row[0]}</td><td>{row[1]:.2f}</td></tr>"
        return report_content
    else:
        report_file_path = f"daily_report_{today}.txt"
        with open(report_file_path, "w") as file:
            file.write("Daily Report:\n")
            for row in report:
                file.write(f"Target: {row[0]}, Average Latency: {row[1]:.2f} ms\n")
        print(f"Report saved to {report_file_path}")
        return report_file_path