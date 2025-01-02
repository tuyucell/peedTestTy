from reports import generate_daily_report, generate_weekly_report
from visualizer import plot_latency

# Ping testlerini yap, ardından rapor ve grafik oluştur
generate_daily_report()
generate_weekly_report()
plot_latency()