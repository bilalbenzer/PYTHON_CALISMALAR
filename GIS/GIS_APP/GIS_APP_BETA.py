giris_messaj = """
------------------------------------
--- GIS UYGULAMAMIZA HOŞGELDİNİZ ---
------------------------------------"""
cikis_mesaj = """
-----------------------------------------------------------
--- GIS UYGULAMAMIZI KULLANDIĞINIZ İÇİN TEŞEKKÜR EDERİZ ---
-----------------------------------------------------------"""

islem_turlerı = """
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
            from konusma_tanima import kayit
            text1=0
            kayit()
            print(text1)
            secenekler = ["1.1","1.1-","Nokta Oluşturma","Nokta Oluşturmak İstiyorum","Nokta Oluştur"]
            if text1 in secenekler:
                from nokta_olusturma import nokta_olustur
                nokta_olustur()
            else:
                print("DUrdu")
                
except KeyboardInterrupt as hata:
    print(hata,"\nİşlem iptal edilmiştir.\n",cikis_mesaj)
    

