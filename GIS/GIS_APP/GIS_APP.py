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
while True:
    secim = input("Lütfen bir işlem türü seçiniz.Çıkış yapmak için 0 diyebilirsiniz.\nCevap:")
    if secim =="1.1-":
        from nokta_olusturma import nokta_olustur
        nokta_olustur()
    elif secim=="0":
        break
    

