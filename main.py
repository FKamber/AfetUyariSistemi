# Observer tasarım örüntüsü kullanılarak bir Afet Uyarı Sistemi

# Subject Sınıfı (Deprem Sensörleri)
class DepremSensoru:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)

    def detect_earthquake(self, magnitude):
        if magnitude >= 5.0:  # Belirli bir eşik değeri
            print(f"Deprem tespit edildi: Büyüklük {magnitude}")
            self.notify_observers(magnitude)

# Observer Arayüzü
class Observer:
    def update(self, data):
        pass

# Observer Sınıfları
class AcilDurumYonetimMerkezi(Observer):
    def update(self, data):
        print(f"Acil Durum Yönetim Merkezi bilgilendirildi: Deprem büyüklüğü {data}")

class HalkBildirimSistemi(Observer):
    def update(self, data):
        print(f"Halk Bildirim Sistemi bilgilendirildi: Deprem büyüklüğü {data}")

class AcilMudahaleEkibi(Observer):
    def update(self, data):
        print(f"Acil Müdahale Ekibi bilgilendirildi: Deprem büyüklüğü {data}")

# Kullanım Senaryosu
if __name__ == "__main__":
    # Subject ve Observer nesneleri oluşturulur
    deprem_sensoru = DepremSensoru()
    acil_durum_yonetim_merkezi = AcilDurumYonetimMerkezi()
    halk_bildirim_sistemi = HalkBildirimSistemi()
    acil_mudahale_ekibi = AcilMudahaleEkibi()

    # Observer nesneleri, subject'e kaydedilir
    deprem_sensoru.register_observer(acil_durum_yonetim_merkezi)
    deprem_sensoru.register_observer(halk_bildirim_sistemi)
    deprem_sensoru.register_observer(acil_mudahale_ekibi)

    # Deprem tespiti simülasyonu
    deprem_sensoru.detect_earthquake(6.5)
