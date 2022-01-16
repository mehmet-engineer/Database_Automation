import sqlite3

class University():
    def __init__(self,isim):
        self.veritabanı = sqlite3.connect("University_Database.sqlite")
        self.islem = self.veritabanı.cursor()
        self.isim = isim
        self.durum = True

        self.islem.execute("CREATE TABLE IF NOT EXISTS öğrenciler (İsim,Soyisim,Fakülte,Bölüm,Sınıf,Numara)")


    def menu(self):
        print("\n-----  {} Veritabanına Hoşgeldiniz  -----\n".format(self.isim))
        print(" 1) Öğrenci Ekle \n 2) Öğrenci Güncelle \n 3) Öğrenci Sil \n 4) Öğrencileri Görüntüle \n 5) Özel Sorgulama \n 6) Çıkış Yap")

        self.anahtar = "off"
        while self.anahtar == "off":
            secim = input("\nHangi işlemi yapmak istediğinizi string olarak yazınız: ")
            choice = secim.lower()

            if choice == "öğrenci ekle":
                self.Ogrenci_ekle()
                self.anahtar = "on"
            elif choice == "öğrenci güncelle":
                self.Ogrenci_guncelle()
                self.anahtar = "on"
            elif choice == "öğrenci sil":
                self.Ogrenci_sil()
                self.anahtar = "on"
            elif choice == "öğrencileri görüntüle":
                self.Ogrenci_goruntule()
                self.anahtar = "on"
            elif choice == "özel sorgulama":
                self.Ozel_sorgulama()
                self.anahtar = "on"
            elif choice == "çıkış yap":
                self.Cikis_yap()
                self.anahtar = "on"
            else:
                print("Girilen string anlaşılmadı. Lütfen tekrar deneyin. Örn: 'öğrenci ekle'")

    def Ogrenci_ekle(self):
        print("\n Yeni Kayıt:  -----------------------------------------------")

        key = "off"
        while key == "off":
            
            isim = input(" Adı: ").lower().capitalize()
            soyisim = input(" Soyadı: ").lower().capitalize()
            fakülte = input(" Fakülte: ").lower().capitalize()
            bölüm = input(" Bölüm: ").lower().capitalize()
            sınıf = input(" Sınıf: ").lower().capitalize()
            no = input(" Numara: ").lower().capitalize()

            listem = [isim,soyisim,fakülte,bölüm,sınıf,no]
            sayı = 0

            for i in listem:
                if i.isalnum() == True:
                    sayı = sayı + 1

            if sayı == 6:
                key = "on"
            else:
                print("\n Girilen verilerden bazıları hatalı! Tekrar yazın\n")
            
        
        self.islem.execute("INSERT INTO öğrenciler VALUES (?,?,?,?,?,?)", (isim,soyisim,fakülte,bölüm,sınıf,no))
        self.veritabanı.commit()
        print("\n Kayıt başarıyla yapılmıştır.")

    def Ogrenci_guncelle(self):
        print("\n Öğrenci Güncelleme:  --------------------------------")
        self.islem.execute("SELECT * FROM öğrenciler")
        data = self.islem.fetchall()
        karar = bool(data)

        if karar == True:
            print("-> Lütfen Güncelleme yapılacak öğrencinin sırasını seçin:\n")
            sayı = 0
            for sıra,veri in enumerate(data):
                print(sıra+1,") ",veri, sep="")
                sayı = sayı + 1
            
            while True:
                
                try:
                    secim = int(input("\n -- Seçiminiz: "))
                    
                    if secim > 0 and secim < sayı+1:
                        self.islem.execute("SELECT * FROM öğrenciler WHERE rowid = {}".format(secim))
                        alınan = self.islem.fetchall()
                        print("Seçilen Öğrenci -> ", alınan, end="\n\n")
                        print("(isim, soyisim, fakülte, bölüm, sınıf, numara) ")
                        choice = input(" -> Güncelleme yapılacak kriteri string şeklinde yazın: ")
                        choice = choice.lower()

                        if choice == "isim":
                            yeni_veri = input("\n-- Yeni veriyi girin: ")
                            self.islem.execute("UPDATE öğrenciler SET İsim = '{}' WHERE rowid = {}".format(yeni_veri,secim))
                            self.veritabanı.commit()
                            print("-- Güncelleme tamamlandı!")
                            break
                        elif choice == "soyisim":
                            yeni_veri = input("\n-- Yeni veriyi girin: ")
                            self.islem.execute("UPDATE öğrenciler SET Soyisim = '{}' WHERE rowid = {}".format(yeni_veri,secim))
                            self.veritabanı.commit()
                            print("-- Güncelleme tamamlandı!")
                            break
                        elif choice == "fakülte":
                            yeni_veri = input("\n-- Yeni veriyi girin: ")
                            self.islem.execute("UPDATE öğrenciler SET Fakülte = '{}' WHERE rowid = {}".format(yeni_veri,secim))
                            self.veritabanı.commit()
                            print("-- Güncelleme tamamlandı!")
                            break
                        elif choice == "bölüm":
                            yeni_veri = input("\n-- Yeni veriyi girin: ")
                            self.islem.execute("UPDATE öğrenciler SET Bölüm = '{}' WHERE rowid = {}".format(yeni_veri,secim))
                            self.veritabanı.commit()
                            print("-- Güncelleme tamamlandı!")
                            break
                        elif choice == "sınıf":
                            yeni_veri = input("\n-- Yeni veriyi girin: ")
                            self.islem.execute("UPDATE öğrenciler SET Sınıf = '{}' WHERE rowid = {}".format(yeni_veri,secim))
                            self.veritabanı.commit()
                            print("-- Güncelleme tamamlandı!")
                            break
                        elif choice == "numara":
                            yeni_veri = input("\n-- Yeni veriyi girin: ")
                            self.islem.execute("UPDATE öğrenciler SET Numara = '{}' WHERE rowid = {}".format(yeni_veri,secim))
                            self.veritabanı.commit()
                            print("-- Güncelleme tamamlandı!")
                            break
                        else:
                            print(" (!) Girilen Kriter anlaşılmadı. Doğru yazdığınızdan emin olun.\n")
                            break
                        

                    else:
                        print(" (!) Girilen sıra değerinde öğrenci yoktur. Sıra numarasını doğru girin!")

                except:
                    print(" (!) Girilen değer anlaşılmadı! Tekrar deneyin.\n")

        else:
            print("\n Veritabanında güncellenebilecek öğrenci kaydı bulunmamaktadır!\n")


    def Ogrenci_sil(self):
        print("\n Öğrenci Silme:  --------------------------------")
        self.islem.execute("SELECT * FROM öğrenciler")
        data = self.islem.fetchall()
        karar = bool(data)

        if karar == True:
            print("-> Lütfen Güncelleme yapılacak öğrencinin sırasını seçin:\n")
            sayı = 0
            for sıra,veri in enumerate(data):
                print(sıra+1,") ",veri, sep="")
                sayı = sayı + 1

            while True:
                
                try:
                    secim = int(input("\n -- Seçiminiz: "))
                    
                    if secim > 0 and secim < sayı+1:
                        self.islem.execute("DELETE FROM öğrenciler WHERE rowid = {}".format(secim))
                        self.veritabanı.commit()
                        print("\n Seçilen öğrenci başarıyla silinmiştir.\n")
                        break
                    else:
                        print("\n Seçilen değerde öğrenci kaydı yoktur. Tekrar deneyin.")
                except:
                    print("- Girilen değer anlaşılmadı!")

        else:
            print("\n Veritabanında silinebilecek öğrenci kaydı bulunmamaktadır!\n")


    def Ogrenci_goruntule(self):
        print("\n Veritabanındaki tüm öğrenciler:  --------------------------------------")
        self.islem.execute("SELECT * FROM öğrenciler")
        data = self.islem.fetchall()
        karar = bool(data)

        if karar == True:
            for sıra,veri in enumerate(data):
                print(sıra+1,") ",veri, sep="")
        else:
            print("-> Veritabanında hiç öğrenci bulunmamaktadır.")

    def Ozel_sorgulama(self):
        print("\n Özel Sorgulama:  --------------------------------------")
        print(" a) Ortak Kategoriye Göre (Fakülte,Bölüm,Sınıf)\n b) Özel bilgilere Göre (İsim,Soyisim,Numara)\n")
        while True:
            secim = input("-- Seçiminiz: ")
            if secim == "a" or secim == "b":
                break
            else:
                print(" (!) Girilen değer yanlış! 'a' ya da 'b' karakterinden birini girin.")

        if secim == "a":
            while True:
                try:
                    kategori = input("\n -Ortak Kategori: ").lower().capitalize()
                    aranan = input(" --Aranan: ").lower().capitalize()
                    self.islem.execute("SELECT * FROM öğrenciler WHERE {} = '{}' ".format(kategori,aranan))
                    veri = self.islem.fetchall()
                    karar = bool(veri)
                except:
                    print("Lütfen kategoriyi doğru girin!")
                    continue

                if karar == True:
                    break
                else:
                    print("\n Aranan kriterlerde bir sonuç bulunamadı.\n")

            print("\n    Kategori: {} / Aranan: {}  -------------------------\n".format(kategori,aranan))
            sayı = 0
            for i,j in enumerate(veri):
                print("    ", i+1, ") ", j, sep="")
                sayı = sayı + 1
            print("\n    - Toplam {} sonuç bulundu.".format(sayı))

        if secim == "b":  
            while True:
                try:
                    kategori = input("\n -Özel Kategori: ").lower().capitalize()
                    aranan = input(" --Aranan: ").lower().capitalize()
                    self.islem.execute("SELECT * FROM öğrenciler WHERE {} = '{}' ".format(kategori,aranan))
                    veri = self.islem.fetchall()
                    karar = bool(veri)
                except:
                    print("Lütfen kategoriyi doğru girin!")
                    continue

                if karar == True:
                    break
                else:
                    print("\n Aranan kriterlerde bir sonuç bulunamadı.\n")

            print("\n    Kategori: {} / Aranan: {}  -------------------------\n".format(kategori,aranan))
            sayı = 0
            for i,j in enumerate(veri):
                print("    ", i+1, ") ", j, sep="")
                sayı = sayı + 1
            print("\n    - Toplam {} sonuç bulundu.".format(sayı))

    def Cikis_yap(self):
        print("\n Çıkış başarıyla yapıldı.")
        self.veritabanı.close()
        self.durum = False


SAU = University("Sakarya University")

while SAU.durum == True:
    SAU.menu() 
