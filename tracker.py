import cloudscraper
from bs4 import BeautifulSoup
import time

# --- AYARLAR ---
URL = "https://www.kitapyurdu.com/kitap/seker-portakali/10137.html"
HEDEF_FIYAT = 120.0  # Denemek için mevcut fiyattan yüksek bir rakam koydum
TELEGRAM_TOKEN = "TOKEN_BURAYA"
CHAT_ID = "ID_BURAYA"

def mesaj_gonder(mesaj):
    import requests
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mesaj}"
    requests.get(url)

def fiyati_kontrol_et():
    print(f"\n🔍 {time.strftime('%H:%M:%S')} - Kontrol ediliyor...")
    
    scraper = cloudscraper.create_scraper()
    
    try:
        cevap = scraper.get(URL, timeout=10)
        if cevap.status_code == 200:
            soup = BeautifulSoup(cevap.text, "html.parser")
            
            
            fiyat_elementi = soup.find(class_="price")
            
            if fiyat_elementi:
                fiyat_metni = fiyat_elementi.text.strip() # "115,50 TL"
                print(f"💰 Ham Fiyat: {fiyat_metni}")
                
                # Sayıya çevirme (115,50 TL -> 115.50)
                temiz_fiyat = fiyat_metni.replace("TL", "").replace(".", "").replace(",", ".").strip()
                guncel_fiyat = float(temiz_fiyat)
                
                print(f"📈 İşlenmiş Fiyat: {guncel_fiyat} TL")
                print(f"🎯 Hedef Fiyat: {HEDEF_FIYAT} TL")

                if guncel_fiyat < HEDEF_FIYAT:
                    print("🚀 Hedef fiyata ulaşıldı! Mesaj gönderiliyor...")
                    mesaj_gonder(f"🔥 BRO FIRSAT! Şeker Portakalı şu an {guncel_fiyat} TL!\nLink: {URL}")
                    return True
                else:
                    print("⏳ Fiyat henüz düşmemiş.")
            else:
                print("❌ Fiyat etiketi bulunamadı!")
                
    except Exception as e:
        print(f"💥 Hata oluştu: {e}")
    return False

if __name__ == "__main__":
    print("🚀 Fiyat Takip Botu Hazır!")
    # Test için bir kez çalıştır, sonra döngüye al
    fiyati_kontrol_et()
    
    # Gerçek kullanımda burayı aktif edebilirsin:
    # while True:
    #     fiyati_kontrol_et()
    #     time.sleep(3600) # 1 saat bekle
