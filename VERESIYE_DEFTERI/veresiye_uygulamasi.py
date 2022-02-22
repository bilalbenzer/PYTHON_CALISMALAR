hosgeldin_mesaji = """
-----------------------------------------
----VERESİYE UYGULAMASINA HOŞGELDİNİZ----
-----------------------------------------
"""
cikis_mesaji = """
-------------------------------------------------------
----UYGULAMAMIZI KULLANDIĞINIZ İÇİN TEŞEKKÜR EDERİZ----
-------------------------------------------------------
"""
"""
1- VERESİYE LİSTESİNİ GÖRME
2-BORÇLU EKLEME
3-BORÇLU SİLME
4- BORÇLU SAYISINI GÖRME
5- ÖDEME TARİHİ GEÇEN BORÇLULARI GÖRME
"""

def veresiye_listesi():
    with open("veresiye_defteri.csv","r",encoding="UTF-8") as listegorme:
        satir_liste = listegorme.readlines()
        satir_sayisi = len(satir_liste)
        listegorme.seek(0)
        for i in range(1,satir_sayisi):
            obje = satir_liste[i]
            borclu_no ,adi_soyadi ,tel_no, proje_adi, borc_miktari, son_odeme_tarihi = obje.split(";")
            print(f"BORÇLU NO: {borclu_no}\nAD-SOYAD: {adi_soyadi}\nTELEFON NO: {tel_no}\nPROJE ADI: {proje_adi}\nBORÇ MİKTARI: {borc_miktari}\nSON ÖDEME TARİHİ: {son_odeme_tarihi}")
def borclu_ekleme():
    for i in range(1):
        with open("veresiye_defteri.csv","r+",encoding="UTF-8") as listegorme:
            borclu_no,ad_soyad,tel_no,proje_adi,borc_miktari,son_odeme_tarihi=input("Lütfen borçlu kişinin nosunu giriniz.\n:"),input("Lütfen borçlu kişinin ad ve soyadını giriniz.\n:"),input("Lütfen borçlu kişinin telefon numarasını giriniz.\n:"),input("Lütfen borçlu kişiye ait projeyi giriniz.\n:"),input("Lütfen borçlu kişinin borç miktarını giriniz.\n:"),input("Lütfen borçlu kişinin borç son ödeme tarihini giriniz.\n:")
            ad_soyad.encode("UTF-8"),proje_adi.encode("UTF-8"),son_odeme_tarihi.encode("UTF-8"),borc_miktari.encode("UTF-8")
            ad_soyad = ad_soyad.title()
            proje_adi = proje_adi.title()
            borc_miktari = borc_miktari.title()
            son_odeme_tarihi = son_odeme_tarihi.title()
            b = listegorme.readline()
            print(f"Girmiş olduğunuz bilgiler şu şekildedir.\nBorçlu No = {borclu_no}\nAd-Soyad = {ad_soyad}\nTelefon No = {tel_no}Proje Adı = {proje_adi}\nBorç Miktarı = {borc_miktari}\nSon Ödeme Tarihi = {son_odeme_tarihi}")
            a = input("Lütfen girilen bilgileri kontrol ediniz. Herhangi bir değişiklik yapacaksanız 1, devam etmek ve listeye eklemek için 2 cevabını veriniz. İşlemden vazgeçmek için 3 diyiniz.")
            if a =="1":
                borclu_no,ad_soyad,tel_no,proje_adi,borc_miktari,son_odeme_tarihi=input("Lütfen borçlu kişinin nosunu giriniz.\n:"),input("Lütfen borçlu kişinin ad ve soyadını giriniz.\n:"),input("Lütfen borçlu kişinin telefon numarasını giriniz.\n:"),input("Lütfen borçlu kişiye ait projeyi giriniz.\n:"),input("Lütfen borçlu kişinin borç miktarını giriniz.\n:"),input("Lütfen borçlu kişinin borç son ödeme tarihini giriniz.\n:")
                ad_soyad.encode("UTF-8"),proje_adi.encode("UTF-8"),son_odeme_tarihi.encode("UTF-8"),borc_miktari.encode("UTF-8")
                ad_soyad = ad_soyad.title()
                proje_adi = proje_adi.title()
                borc_miktari = borc_miktari.title()
                son_odeme_tarihi = son_odeme_tarihi.title()
                b = listegorme.readline()
                print(f"Girmiş olduğunuz bilgiler şu şekildedir.\nBorçlu No = {borclu_no}\nAd-Soyad = {ad_soyad}\nTelefon No = {tel_no}\nProje Adı = {proje_adi}\nBorç Miktarı = {borc_miktari}\nSon Ödeme Tarihi = {son_odeme_tarihi}")
                a = input("Lütfen girilen bilgileri kontrol ediniz. Devam etmek için 1, işlemden vazgeçmek için 2 diyiniz.")
                if a == "1":
                    liste = f"\n{borclu_no};{ad_soyad};{tel_no};{proje_adi};{borc_miktari};{son_odeme_tarihi}"
                    listegorme.write(liste)
                elif a =="2":
                    print("İşlem sonlanmıştır. Tekrar ekleme işlemi yapmak için programı yeniden başlatınız.")
                    break

            elif a == "2":
                liste = f"\n{borclu_no};{ad_soyad};{tel_no};{proje_adi};{borc_miktari};{son_odeme_tarihi}"
                listegorme.write(liste)
            elif a =="3":
                print("İşlem sonlanmıştır. Tekrar ekleme işlemi yapmak için programı yeniden başlatınız.")
                break
def borclu_silme():
    for i in range(1):
        a = input("Borç Silerken Hangi Referansa Göre Sileceksiniz?\nAd-Soyad Bilgisi İle: 1\nTelefon No İle: 2\nProje Adı İle: 3\nBorçlu No İle 4")
        if a =="1":
            ad_soyad = input("Borçlunun ad ve soyadını giriniz.")
            ad_soyad = ad_soyad.title()
            satir_liste=[]
            print(ad_soyad)
            with open("veresiye_defteri.csv","r+",encoding="UTF-8") as listegorme:
                satir_liste = listegorme.readlines()
                satir_sayisi = len(satir_liste)
                listegorme.seek(0)
                print(satir_liste)
                for i in range(1,satir_sayisi):
                    obje = satir_liste[i]
                    borclu_no ,adi_soyadi ,tel_no, proje_adi, borc_miktari, son_odeme_tarihi = obje.split(";")
                    print(f"BORÇLU NO: {borclu_no}\nAD-SOYAD: {adi_soyadi}\nTELEFON NO: {tel_no}\nPROJE ADI: {proje_adi}\nBORÇ MİKTARI: {borc_miktari}\nSON ÖDEME TARİHİ: {son_odeme_tarihi}")
                    if adi_soyadi==ad_soyad:
                        del satir_liste[i]
                        print(satir_liste)
                        break
            with open("veresiye_defteri.csv","w",encoding="UTF-8") as liste1:
                satir_liste.append("\n")
                liste1.writelines(satir_liste)
        elif a=="2":
            telefon_no = input("Borçlu Kişinin Telefon Numarasını Giriniz.")
            satir_liste = []
            print(telefon_no)
            with open("veresiye_defteri.csv","r+",encoding="UTF-8") as listegorme:
                satir_liste = listegorme.readlines()
                satir_sayisi = len(satir_liste)
                listegorme.seek(0)
                print(satir_liste)
                for i in range(1,satir_sayisi):
                    obje = satir_liste[i]
                    borclu_no ,adi_soyadi ,tel_no, proje_adi, borc_miktari, son_odeme_tarihi = obje.split(";")
                    print(f"BORÇLU NO: {borclu_no}\nAD-SOYAD: {adi_soyadi}\nTELEFON NO: {tel_no}\nPROJE ADI: {proje_adi}\nBORÇ MİKTARI: {borc_miktari}\nSON ÖDEME TARİHİ: {son_odeme_tarihi}")
                    if tel_no==telefon_no:
                        del satir_liste[i]
                        print(satir_liste)
                        break
            with open("veresiye_defteri.csv","w",encoding="UTF-8") as liste1:
                satir_liste.append("\n")
                liste1.writelines(satir_liste)
        elif a=="3":
            projee_adi = input("Borçlu Kişinin Telefon Numarasını Giriniz.")
            projee_adi = projee_adi.title()
            satir_liste = []
            print(projee_adi)
            with open("veresiye_defteri.csv","r+",encoding="UTF-8") as listegorme:
                satir_liste = listegorme.readlines()
                satir_sayisi = len(satir_liste)
                listegorme.seek(0)
                print(satir_liste)
                for i in range(1,satir_sayisi):
                    obje = satir_liste[i]
                    borclu_no ,adi_soyadi ,tel_no, proje_adi, borc_miktari, son_odeme_tarihi = obje.split(";")
                    print(f"BORÇLU NO: {borclu_no}\nAD-SOYAD: {adi_soyadi}\nTELEFON NO: {tel_no}\nPROJE ADI: {proje_adi}\nBORÇ MİKTARI: {borc_miktari}\nSON ÖDEME TARİHİ: {son_odeme_tarihi}")
                    if projee_adi==proje_adi:
                        del satir_liste[i]
                        print(satir_liste)
                        break
            with open("veresiye_defteri.csv","w",encoding="UTF-8") as liste1:
                satir_liste.append("\n")
                liste1.writelines(satir_liste)
        elif a=="4":
            borclu_no1 = input("Borçlu No'yu Giriniz.")
            satir_liste = []
            print(projee_adi)
            with open("veresiye_defteri.csv","r+",encoding="UTF-8") as listegorme:
                satir_liste = listegorme.readlines()
                satir_sayisi = len(satir_liste)
                listegorme.seek(0)
                print(satir_liste)
                for i in range(1,satir_sayisi):
                    obje = satir_liste[i]
                    borclu_no ,adi_soyadi ,tel_no, proje_adi, borc_miktari, son_odeme_tarihi = obje.split(";")
                    print(f"BORÇLU NO: {borclu_no}\nAD-SOYAD: {adi_soyadi}\nTELEFON NO: {tel_no}\nPROJE ADI: {proje_adi}\nBORÇ MİKTARI: {borc_miktari}\nSON ÖDEME TARİHİ: {son_odeme_tarihi}")
                    if borclu_no == borclu_no1:
                        del satir_liste[i]
                        print(satir_liste)
                        break
            with open("veresiye_defteri.csv","w",encoding="UTF-8") as liste1:
                satir_liste.append("\n")
                liste1.writelines(satir_liste)
        else:
            print("Yanlış bir seçim yaptınız. Program sonlanmıştır.")
def borclu_sayisi():
    with open("veresiye_defteri.csv","r",encoding="UTF-8") as listegorme:
        satir_liste = listegorme.readlines()
        satir_sayisi = len(satir_liste)
        listegorme.seek(0)
    a= 0
    for i in range(1,satir_sayisi):
        obje = satir_liste[i]
        borclu_no ,adi_soyadi ,tel_no, proje_adi, borc_miktari, son_odeme_tarihi = obje.split(";")
        a += float(borc_miktari)
    print(f"Borçlu Sayısı = {satir_sayisi-1}\nToplam Alacak Tutarı = {a}")
def odeme_tarihi_gecenler():
    with open("veresiye_defteri.csv","r",encoding="UTF-8") as listegorme:
        satir_liste = listegorme.readlines()
        satir_sayisi = len(satir_liste)
        listegorme.seek(0)
        mevcut_gun,mevcut_ay,mevcut_yil = 6,2,2022
        print("Aşağıda yer alan borçlu kişilerin, son ödeme tarihleri geçniştir.")
        for i in range(1,satir_sayisi):
            obje = satir_liste[i]
            borclu_no ,adi_soyadi ,tel_no, proje_adi, borc_miktari, son_odeme_tarihi = obje.split(";")
            borc_gun,borc_ay,borc_yil = son_odeme_tarihi.split(".")
            if int(borc_yil)<mevcut_yil:
                print(f"BORÇLU NO: {borclu_no}\nAD-SOYAD: {adi_soyadi}\nTELEFON NO: {tel_no}\nPROJE ADI: {proje_adi}\nBORÇ MİKTARI: {borc_miktari}\nSON ÖDEME TARİHİ: {son_odeme_tarihi}")
            elif int(borc_yil)==mevcut_yil:
                if int(borc_ay)<mevcut_ay:
                    print(f"BORÇLU NO: {borclu_no}\nAD-SOYAD: {adi_soyadi}\nTELEFON NO: {tel_no}\nPROJE ADI: {proje_adi}\nBORÇ MİKTARI: {borc_miktari}\nSON ÖDEME TARİHİ: {son_odeme_tarihi}")
                elif int(borc_ay)==mevcut_ay:
                    if int(borc_gun)<mevcut_gun:
                        print(f"BORÇLU NO: {borclu_no}\nAD-SOYAD: {adi_soyadi}\nTELEFON NO: {tel_no}\nPROJE ADI: {proje_adi}\nBORÇ MİKTARI: {borc_miktari}\nSON ÖDEME TARİHİ: {son_odeme_tarihi}")
                    elif int(borc_gun)>mevcut_ay:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
while True:
    print(hosgeldin_mesaji)
    a = input("Yapmak istediğiniz işlemi giriniz.\nVeresiye Listesi : 1\nBorçlu Ekleme : 2\nBorçlu Silme : 3\nBorçlu Sayısını ve Toplam Borcu Görme : 4\nÖdeme Tarihi Geçen Borçluları Görme : 5\n-->")
    if a == "1":
        veresiye_listesi()
    elif a =="2":
        borclu_ekleme()
    elif a =="3":
        borclu_silme()
    elif a == "4":
        borclu_sayisi()
    elif a == "5":
        odeme_tarihi_gecenler()
    else:
        print("Program sonlanmıştır.")
        print(cikis_mesaji)
