# Speed Test Project

Bu proje, belirli hedeflere düzenli olarak ping göndererek internet bağlantınızın hızını test eder. Hedeflere olan gecikme sürelerini (latency) ölçer ve günlük, haftalık ve aylık raporlar oluşturur. Ayrıca raporları e-posta ile görselli bir biçimde gönderir.

## Özellikler

- Belirli hedeflere (ör. `8.8.8.8`, `1.1.1.1`, `google.com`) ping göndererek **latency** ölçer.
- Günlük, haftalık ve aylık raporlar oluşturur.
- **E-posta raporları**: Günlük raporları görselli ve ekli grafik dosyalarıyla e-posta olarak gönderir.
- Docker ile kolay dağıtım ve çalıştırma.

---

## Kurulum

### 1. Proje Dosyalarını Klonlama
```bash
git clone <repository-url>
cd speedTestTy

2. Gerekli Bağımlılıkları Yükleme

Sanal ortam kullanıyorsanız:

python -m venv .venv
source .venv/bin/activate  # Windows için: .venv\Scripts\activate
pip install -r requirements.txt

config.py Ayarları

Proje ile birlikte bir config.py şablonu sağlanmaktadır. Bu dosyayı kendi e-posta sunucusu bilgilerinize göre doldurun.

config.py Örneği:

SMTP_CONFIG = {
    "host": "mail.yourdomain.com",
    "port": 465,  # TLS kullanıyorsanız 465
    "username": "your_email@yourdomain.com",
    "password": "your_email_password",
    "from_email": "your_email@yourdomain.com",
    "to_email": "recipient_email@example.com"
}

3. Docker İmajını Oluşturma ve Çalıştırma

Projenizi Docker ile çalıştırmak için:

Docker İmajını Oluşturma:

docker build -t speedtestty .

Docker Container’ı Çalıştırma:

docker run -d --name speedtestty speedtestty

Container otomatik olarak günlük, haftalık ve aylık raporları oluşturup e-posta gönderecektir.

Kullanım

Günlük, Haftalık ve Aylık Raporlar
	•	Günlük Rapor: Her gün gönderilir.
	•	Haftalık Rapor: Haftanın son günü (Pazar).
	•	Aylık Rapor: Her ayın ilk günü.

E-posta Testi

SMTP ayarlarınızı doğrulamak için emailer.py içerisinde bir test fonksiyonu bulunmaktadır.

Katkıda Bulunma
	1.	Projeyi fork’layın.
	2.	Yeni bir branch oluşturun (git checkout -b feature/AmazingFeature).
	3.	Değişikliklerinizi commit edin (git commit -m 'Add some AmazingFeature').
	4.	Branch’inize push edin (git push origin feature/AmazingFeature).
	5.	Bir Pull Request açın.

Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.