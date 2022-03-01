giris_messaj = """
------------------------------------
--- GIS UYGULAMAMIZA HOŞGELDİNİZ ---
------------------------------------"""
cikis_mesaj = """
-----------------------------------------------------------
--- GIS UYGULAMAMIZI KULLANDIĞINIZ İÇİN TEŞEKKÜR EDERİZ ---
-----------------------------------------------------------"""

islem_turlerı = """
***SESLİ KONUŞMA ETKİN DEĞİL. SESLİ KONUŞMAYI KULLANMAK İÇİN 1 DİYEBİLİRSİNİZ***

1- GEOMETRİK NESNE OLUŞTURMA
    1.1- NOKTA OLUŞTURMA
    1.2- ÇİZGİ OLUŞTURMA
    1.3- ÇOKGEN OLUŞTURMA
    1.4- ÇOKLU NOKTA OLUŞTURMA
    1.5- ÇOKLU ÇİZGİ OLUŞTURMA
    1.6- ÇOKLU POLİGON OLUŞTURMA
2- SHAPEFILE AÇMA
3- SHAPEFILE AKTARMA

"""
print(giris_messaj)
print(islem_turlerı)

try:
    while True:
        sesli_komut = input("Sesli Komut Kullanmak İstiyor Musunuz?\nEvet:1\nHayır:2\nCevap:")
        print("Lütfen bir işlem türü seçiniz.Çıkış yapmak için 0 diyebilirsiniz.\nCevap:")
        if sesli_komut=="2":
            ayarlar(sesli_komut_acik_kapali="Kapalı")
            print("Lütfen bir işlem türü seçiniz.Çıkış yapmak için 0 diyebilirsiniz.\nCevap:")
            secim =input(":")         
            if secim =="1.4-":
                from coklu_nokta_olusturma import nokta_olustur
                nokta_olustur()
            elif secim=="1.1-":
                from nokta_olusturma import nokta_olustur
                nokta_olustur()
            elif secim=="0":
                break
        elif sesli_komut=="1":
            ###
            from siniflar import ayarlar, kayit_olustur
            b = ayarlar(sesli_komut_acik_kapali="Açık")
            a = kayit_olustur(b)
            a.kayit()
            ###
            komut1=a.text
            secenekler = ["1.1","1.1-","nokta oluşturma","nokta oluşturmak istiyorum","nokta oluştur"]
            print(f"Cevap:{komut1}")
            if secenekler.count(komut1) >= 1:
                from nokta_olusturma import nokta_olustur
                nokta_olustur()
                text = 0
            else:
                print("Durdu","\n",cikis_mesaj)
                break
                
                
except KeyboardInterrupt as hata:
    print(hata,"\nİşlem iptal edilmiştir.\n",cikis_mesaj)
    

