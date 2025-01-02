# Python 3.9 slim imajını kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri yüklemeden önce pip'i güncelle
RUN pip install --upgrade pip

# Gereksinim dosyasını kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tüm dosyaları konteynıra kopyala
COPY . .

# Ana dosyayı çalıştır
CMD ["python", "ping_tester.py"]