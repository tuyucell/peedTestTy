import matplotlib.pyplot as plt
import sqlite3
import datetime

DB_FILE = "ping_data.db"

def create_latency_graph():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today()
    start = f"{today} 00:00:00"
    end = f"{today} 23:59:59"

    # Verileri sorgula
    cursor.execute('''
        SELECT target, AVG(latency) as avg_latency
        FROM ping_data
        WHERE timestamp BETWEEN ? AND ?
        GROUP BY target
    ''', (start, end))
    data = cursor.fetchall()
    conn.close()

    # Grafik oluştur
    targets = [row[0] for row in data]
    latencies = [row[1] for row in data]

    plt.figure(figsize=(10, 6))
    plt.bar(targets, latencies, color='blue')
    plt.xlabel("Targets")
    plt.ylabel("Average Latency (ms)")
    plt.title("Daily Latency Report")
    plt.tight_layout()

    # Grafik dosyasını kaydet
    graph_file_path = f"daily_latency_{today}.jpg"
    plt.savefig(graph_file_path)
    plt.close()

    print(f"Graph saved to {graph_file_path}")
    return graph_file_path