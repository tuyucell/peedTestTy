import sqlite3
import datetime

DB_FILE = "ping_data.db"

def generate_daily_report():
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
    with open(f"daily_report_{today}.txt", "w") as file:
        file.write("Daily Report:\n")
        for row in report:
            file.write(f"Target: {row[0]}, Average Latency: {row[1]:.2f} ms\n")
    conn.close()
    print("Daily report saved.")

def generate_weekly_report():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    start = (datetime.date.today() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    end = datetime.date.today().strftime("%Y-%m-%d")
    cursor.execute('''
        SELECT target, AVG(latency) as avg_latency
        FROM ping_data
        WHERE timestamp BETWEEN ? AND ?
        GROUP BY target
    ''', (start, end))
    report = cursor.fetchall()
    with open(f"weekly_report_{datetime.date.today()}.txt", "w") as file:
        file.write("Weekly Report:\n")
        for row in report:
            file.write(f"Target: {row[0]}, Average Latency: {row[1]:.2f} ms\n")
    conn.close()
    print("Weekly report saved.")