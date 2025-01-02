Aşağıda projeniz için temel bir README.md taslağı bulunmaktadır. Bu dosya, projenizi açıklamak, kullanım talimatlarını ve geliştirme detaylarını paylaşmak için kullanılır.

README.md

# Speed Test Project

Bu proje, belirli hedeflere düzenli olarak **ping** göndererek internet bağlantınızı test eder. Hedeflere olan gecikme sürelerini (latency) ölçer ve verileri bir veritabanında saklar. Ayrıca günlük, haftalık ve aylık raporlar oluşturur.

## Özellikler

- Belirli hedeflere (ör. `8.8.8.8`, `1.1.1.1`, `google.com`) ping göndererek **latency** ölçer.
- Sonuçları bir **SQLite** veritabanında saklar.
- **Günlük raporlar** oluşturur ve .txt formatında kaydeder.
- **Haftalık ve aylık raporlar** oluşturma özelliği.
- Ortalama gecikme sürelerini görselleştirmek için **grafikler**.
- Kolay kurulum ve Docker ile uyumlu.

## Kurulum

1. Bu repository'yi klonlayın:

   ```bash
   git clone git@github.com:tuyucell/peedTestTy.git
   cd peedTestTy

	2.	Sanal bir Python ortamı oluşturun ve etkinleştirin:

python -m venv .venv
source .venv/bin/activate  # Windows için .venv\Scripts\activate


	3.	Gerekli bağımlılıkları yükleyin:

pip install -r requirements.txt


	4.	Uygulamayı çalıştırın:

python ping_tester.py



Kullanım
	•	Projeyi çalıştırarak günlük ping sonuçlarını ve raporlarını oluşturabilirsiniz.
	•	Raporlar daily_report_YYYY-MM-DD.txt formatında proje dizinine kaydedilir.
	•	Docker kullanarak uygulamayı zamanlanmış olarak çalıştırabilirsiniz.

Geliştirme
	1.	Yeni bir özellik üzerinde çalışmak için yeni bir branch oluşturun:

git checkout -b feature/new-feature


	2.	Değişikliklerinizi commit edip GitHub’a gönderin:

git add .
git commit -m "Add new feature"
git push origin feature/new-feature


	3.	Pull Request oluşturun.

Gereksinimler
	•	Python 3.8 veya üzeri
	•	ping komutunun çalışabileceği bir sistem
	•	İsteğe bağlı: Docker

Katkıda Bulunma
	1.	Repository’yi fork’layın.
	2.	Yeni bir branch oluşturun (git checkout -b feature/AmazingFeature).
	3.	Değişikliklerinizi commit edin (git commit -m 'Add some AmazingFeature').
	4.	Branch’inize push edin (git push origin feature/AmazingFeature).
	5.	Bir Pull Request açın.

Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.
