# 📉 PriceTrackerBot - Python ile Telegram Entegreli Fiyat Takipçisi

PriceTrackerBot, e-ticaret sitelerindeki (Örn: Kitapyurdu) ürün fiyatlarını otomatik olarak takip eden ve fiyat belirlediğiniz limitin altına düştüğünde size anlık olarak **Telegram** üzerinden bildirim gönderen bir otomasyon aracıdır.

## ✨ Özellikler

- **Gelişmiş Web Scraping:** `cloudscraper` kütüphanesi ile bot korumalarını aşar.
- **Anlık Bildirim:** Telegram Bot API entegrasyonu sayesinde telefonunuza bildirim gönderir.
- **Dinamik Fiyat Analizi:** HTML etiketleri arasından fiyat bilgisini cımbızla çeker ve sayısal veriye dönüştürür.
- **Kolay Yapılandırma:** Takip edilecek ürün linki ve hedef fiyat kolayca değiştirilebilir.

## 🛠 Kullanılan Teknolojiler

- **Python 3**
- **BeautifulSoup (bs4):** HTML verilerini parçalamak ve analiz etmek için.
- **Cloudscraper:** Modern sitelerdeki bot engellerini aşmak için.
- **Telegram API:** Bildirim sistemi için.

## 🚀 Kurulum ve Kullanım

1. Bu repoyu bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/burkibuz-ui/PriceTrackerBot.git](https://github.com/burkibuz-ui/PriceTrackerBot.git)
