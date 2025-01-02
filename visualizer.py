import sqlite3
import matplotlib.pyplot as plt

DB_FILE = "ping_data.db"


def plot_latency():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT target, AVG(latency) as avg_latency
        FROM ping_data
        GROUP BY target
    ''')
    data = cursor.fetchall()
    conn.close()

    targets = [row[0] for row in data]
    latencies = [row[1] for row in data]

    plt.bar(targets, latencies)
    plt.title("Average Latency")
    plt.ylabel("Latency (ms)")
    plt.xlabel("Targets")
    plt.show()