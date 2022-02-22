hosgeldin_mesaji="""
---------------------------------------------------------------------------
---- BANKA HESAP EKLEME-PARA ÇEKME VE YATIRMA UYGULAMAMIZA HOŞGELDİNİZ ----
---------------------------------------------------------------------------
"""
cikis_mesaji="""
-------------------------------------------------------------------
---- UYGULAMA SONLANMIŞTUR. KULLANDIĞINIZ İÇİN TEŞEKKÜR EDERİZ ----
-------------------------------------------------------------------
"""

sozluk1_musteriler={12345678911:{
    "Ad-Soyad":"Bilal Benzer",
    "Doğum Tarihi":"16/6/1997",
    "İl":"Afyonkarahisar",
    "İlçe":"Ihsaniye",
    "Mahalle":"Fatih,Döğer"}}
sozluk2_hesap_bilgi={
    12345678911:{
        "Hesap Türü":"Vadesiz",
        "Hesap Bakiyesi":1000,
        "Hesap Para Cinsi":"Türk Lirası",
        "Ek Para Limiti" : 0 }}
sozluk3_kredi_bilgi= {
    12345678911:{
        "Kredi Adeti":0,
        "Kredi Limiti":0 }}
hata_listesi=[]
kuraller=dict()
def musteri_olma():
    for i in range(1):
        tire_satiri = len("Lütfen T.C. Kimlik Numaranızı 11 haneli olarak giriniz")*"-"+"\n"
        try:
            kimlik_no = input("Lütfen T.C. Kimlik Numaranızı 11 haneli olarak giriniz.\nKimlik No:")
            a=0
            for i in (kimlik_no[0:10]):
                a+=int(i)
            else:
                a=str(a)            
            if len(kimlik_no)==11 and a[-1]==kimlik_no[-1]:
                kimlik_no=int(kimlik_no)
                pass
            else:
                print(len("Hatalı bir giriş yaptınız. Lütfen T.C. Kimlik numaranızı 11 haneli olarak giriniz.")*"-"+"\nHatalı bir giriş yaptınız. Lütfen T.C. Kimlik numaranızı 11 haneli olarak giriniz.")
                kimlik_no = input("Kimlik No:")
                a=0
                for i in (kimlik_no[0:10]):
                    a+=int(i)
                else:
                    a=str(a)            
                    if len(kimlik_no)==11 and a[-1]==kimlik_no[-1]:
                        kimlik_no=int(kimlik_no)
                        pass
                    else:
                        print("2. kez hatalı giriş yaptınız. Program sonlanmıştır.")
                        break
        except:
            print("Hatalı bir giriş yaptınız. Lütfen tekrar deneyiniz.")
            continue        
        ad_soyad=input("Lütfen adınızı ve soyadınızı giriniz.\nAd-Soyad:").title()
        try:            
            dogum_tarihi_gun=(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
            dogum_tarihi_ay=(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
            dogum_tarihi_yil=(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
            if not 12>=int(dogum_tarihi_ay)>0 and 31>=int(dogum_tarihi_gun)>0 and 2004>=int(dogum_tarihi_yil)>1900:
                print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
                dogum_tarihi_gun=(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=int(dogum_tarihi_ay)>0 and 31>=int(dogum_tarihi_gun)>0 and 2004>=int(dogum_tarihi_yil)>1900:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
                else:
                    pass
        except ValueError:
            print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
            try:
                dogum_tarihi_gun=(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=int(dogum_tarihi_ay)>0 and 31>=int(dogum_tarihi_gun)>0 and 2004>=int(dogum_tarihi_yil)>1900:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
            except ValueError:
                print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                break
        dogum_tarihi=dogum_tarihi_gun+"/"+dogum_tarihi_ay+"/"+dogum_tarihi_yil
        il = input("Lütfen ikamet ettiğiniz ili giriniz.").title()
        ilce = input("Lütfen ikamet ettiğiniz ilçeyi giriniz.").title()
        mahalle = input("Lütfen ikamet ettiğiniz mahalleyi giriniz.").title()
        #sözlüğe verileri ekleme:
        bos_sozluk ={kimlik_no:{
    "Ad-Soyad":ad_soyad,
    "Doğum Tarihi":dogum_tarihi,
    "İl":il,
    "İlçe":ilce,
    "Mahalle":mahalle}}
        
        sozluk1_musteriler.update(bos_sozluk)
        bos_sozluk2={kimlik_no:{
        "Hesap Türü":None,
        "Hesap Bakiyesi":None,
        "Hesap Para Cinsi":None,
        "Ek Para Limiti" : None }}
        sozluk2_hesap_bilgi.update(bos_sozluk2)
        bos_sozluk3={
    kimlik_no:{
        "Kredi Adeti":None,
        "Kredi Limiti":None }}
        sozluk3_kredi_bilgi.update(bos_sozluk3)
        for a,b in sozluk1_musteriler[kimlik_no].items():
            print(a,b)
        for a,b in sozluk2_hesap_bilgi[kimlik_no].items():
            print(a,b)
        for a,b in sozluk3_kredi_bilgi[kimlik_no].items():
            print(a,b)

def kayitli_musteri_hesap_acma():
    for i in range(1):
        try:
            kimlik_no = int(input("Lütfen T.C. Kimlik Numaranızı 11 haneli olarak giriniz.\nKimlik No:"))        
            if kimlik_no in sozluk1_musteriler:
                pass
            else:
                kimlik_no = int(input("Lütfen T.C. Kimlik Numaranızı 11 haneli olarak giriniz.\nKimlik No:"))        
                if kimlik_no in sozluk1_musteriler:
                    pass
                else:
                    print("2. kez hatalı giriş yaptınız:İşlem sonlandırılmıştır.")
                    break
        except:
            print("Hatalı bir giriş yaptınız. Lütfen tekrar deneyiniz.")
            continue        
        print("Lütfen kimliğinizi doğrulayabilmemiz için; Ad-Soyad, Doğum tarihi, İkamet edilen il,ilçe ve mahalleyi giriniz. ")
        print("---UYARI---\nLütfen bilgilerinizi doğru giriniz. Hatalı girmeniz durumunda 2. kez deneyebilirsiniz. Tekrar hatalı girerseniz program sonlanacaktır.")
        ad_soyad=input("Lütfen adınızı ve soyadınızı arasında 1 boşluk olacak şekilde giriniz.").title()       
        try:            
            dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
            dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
            dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
            if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
                dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
                else:
                    pass
        except ValueError:
            print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
            try:
                dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
            except ValueError:
                print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                break
        dogum_tarihi=str(str(dogum_tarihi_gun)+"/"+str(dogum_tarihi_ay)+"/"+str(dogum_tarihi_yil))
        il = input("İkamet ettiğiniz il :").title()
        ilce = input("İkamet ettiğiniz ilçe :").title()
        mahalle = input("İkamet ettiğiniz mahalle :")
        if sozluk1_musteriler[kimlik_no]["Ad-Soyad"] == ad_soyad and sozluk1_musteriler[kimlik_no]["Doğum Tarihi"] == dogum_tarihi and sozluk1_musteriler[kimlik_no]["İl"]==il and sozluk1_musteriler[kimlik_no]["İlçe"]==ilce and sozluk1_musteriler[kimlik_no]["Mahalle"]==mahalle:
            try:
                a=(("Girdiğiniz bilgiler doğrudur. İşleme devam ederek, Vadeli/Vadesiz olarak 2 tür;Türk Lirası/Euro/Dolar olarak 3 tür,Ekpara tanımlanacak mı(tanımlanacak ise limit de sorulacaktır) Evet/Hayır seçeneklerini doğru bir şekilde girerek hesabınızı oluşturabilirsiniz.\nUYARI:Yanlış girmeniz durumunda program sonlanacaktır. Lütfen seçeneklere uyarak giriniz."))
                print(a)
                hesap_turu = input("Vadeli:1\nVadesiz:2")
                hesap_para_cinsi = input("Türk Lirası:1\nDolar:2\nEuro:3")
                ekpara=input("Evet:1\nHayır:2")
                if (hesap_turu=="1" or hesap_turu=="2") and (hesap_para_cinsi=="1" or hesap_para_cinsi=="2" or hesap_para_cinsi=="3") and (ekpara=="1" or ekpara=="2"):
                    print("Girdiğiniz bilgiler geçerlidir. Lütfen bekleyiniz.\n.\n.\n.\n.\n")
                    if hesap_turu=="1":
                        sozluk2_hesap_bilgi[kimlik_no]["Hesap Türü"]= "Vadeli"
                    else:
                        sozluk2_hesap_bilgi[kimlik_no]["Hesap Türü"]= "Vadesiz"
                    if hesap_para_cinsi=="1":
                        sozluk2_hesap_bilgi[kimlik_no]["Hesap Para Cinsi"]= "Türk Lirası"
                    elif hesap_para_cinsi=="2":
                        sozluk2_hesap_bilgi[kimlik_no]["Hesap Para Cinsi"]= "Dolar"
                    else:
                        sozluk2_hesap_bilgi[kimlik_no]["Hesap Para Cinsi"]= "Euro"
                    if ekpara=="1":
                        try:
                            ekpara_limit=input("Ekpara limitiniz ne kadar olacak?(Lütfen sayısal değerler giriniz.")
                            sozluk2_hesap_bilgi[kimlik_no]["Ek Para Limiti"] =int(ekpara_limit)
                        except ValueError:
                            print("Ek para limitiniz için yanlış bir değer girdiniz. Lütfen tekrar deneyiniz.")
                            try:
                                ekpara_limit=input("Ekpara limitiniz ne kadar olacak?(Lütfen sayısal değerler giriniz.")
                                sozluk2_hesap_bilgi[kimlik_no]["Ek Para Limiti"] =int(ekpara_limit)
                            except ValueError:
                                print("Ek para limitiniz için 2. kez yanlış bir değer girdiniz. Program sonlanmıştır.")
                    else:
                        sozluk2_hesap_bilgi[kimlik_no]["Ek Para Limiti"] = 0
                    print("Tebrikler, hesabınız oluşturulmuştur.")
                else:
                    print("Hatalı giriş yaptınız.Lütfen seçeneklere uygun bir şekilde cevap veriniz.")
                    try:
                        a=("Girdiğiniz bilgiler doğrudur. İşleme devam ederek, Vadeli/Vadesiz olarak 2 tür;Türk Lirası/Euro/Dolar olarak 3 tür,Ekpara tanımlanacak mı(tanımlanacak ise limit de sorulacaktır) Evet/Hayır seçeneklerini doğru bir şekilde girerek hesabınızı oluşturabilirsiniz.\nUYARI:Yanlış girmeniz durumunda program sonlanacaktır. Lütfen seçeneklere uyarak giriniz.")
                        print(a)
                        hesap_turu = input("Vadeli:1\nVadesiz:2")
                        hesap_para_cinsi = input("Türk Lirası:1\nDolar:2\nEuro:3")
                        ekpara=input("Evet:1\nHayır:2")
                        if (hesap_turu=="1" or hesap_turu=="2") and (hesap_para_cinsi=="1" or hesap_para_cinsi=="2" or hesap_para_cinsi=="3") and (ekpara=="1" or ekpara=="2"):
                            print("Girdiğiniz bilgiler geçerlidir. Lütfen bekleyiniz.\n.\n.\n.\n.\n")
                            if hesap_turu=="1":
                                sozluk2_hesap_bilgi[kimlik_no]["Hesap Türü"]= "Vadeli"
                            else:
                                sozluk2_hesap_bilgi[kimlik_no]["Hesap Türü"]= "Vadesiz"
                            if hesap_para_cinsi=="1":
                                sozluk2_hesap_bilgi[kimlik_no]["Hesap Para Cinsi"]= "Türk Lirası"
                            elif hesap_para_cinsi=="2":
                                sozluk2_hesap_bilgi[kimlik_no]["Hesap Para Cinsi"]= "Dolar"
                            else:
                                sozluk2_hesap_bilgi[kimlik_no]["Hesap Para Cinsi"]= "Euro"
                            if ekpara=="1":
                                try:
                                    ekpara_limit=input("Ekpara limitiniz ne kadar olacak?(Lütfen sayısal değerler giriniz.")
                                    sozluk2_hesap_bilgi[kimlik_no]["Ek Para Limiti"] =int(ekpara_limit)
                                except ValueError:
                                    print("Ek para limitiniz için yanlış bir değer girdiniz. Lütfen tekrar deneyiniz.")
                                    try:
                                        ekpara_limit=input("Ekpara limitiniz ne kadar olacak?(Lütfen sayısal değerler giriniz.")
                                        sozluk2_hesap_bilgi[kimlik_no]["Ek Para Limiti"] =int(ekpara_limit)
                                    except ValueError:
                                        print("Ek para limitiniz için 2. kez yanlış bir değer girdiniz. Program sonlanmıştır.")
                                        break
                            else:
                                sozluk2_hesap_bilgi[kimlik_no]["Ek Para Limiti"] = 0
                            print("Tebrikler, hesabınız oluşturulmuştur.")
                        else:
                            print("Hesap bilgileriniz uyuşmamaktadır. Program sonlanmıştır.")
                            break
                    except ValueError:
                        print("2. kez hatalı giriş yaptınız. Program sonlanmıştır.")
                        break
            except ValueError:
                print("Hatalı giriş yaptınız. Program sonlamıştır.")
                break
        else:
            print("Hesap bilgileriniz uyuşmamaktadır. Program sonlanmıştır.")
            break

def musteri_kayit_silme():
    for i in range(1):
        try:
            kimlik_no = int(input("Lütfen T.C. Kimlik Numaranızı 11 haneli olarak giriniz.\nKimlik No:"))        
            if kimlik_no in sozluk1_musteriler:
                pass
            else:
                kimlik_no = int(input("Lütfen T.C. Kimlik Numaranızı 11 haneli olarak giriniz.\nKimlik No:"))        
                if kimlik_no in sozluk1_musteriler:
                    pass
                else:
                    print("2. kez hatalı giriş yaptınız:İşlem sonlandırılmıştır.")
                    break
        except:
            print("Hatalı bir giriş yaptınız. Lütfen tekrar deneyiniz.")
            continue 
        print("Lütfen kimliğinizi doğrulayabilmemiz için; Ad-Soyad, Doğum tarihi, İkamet edilen il,ilçe ve mahalleyi giriniz. ")
        print("---UYARI---\nLütfen bilgilerinizi doğru giriniz. Hatalı girmeniz durumunda 2. kez deneyebilirsiniz. Tekrar hatalı girerseniz program sonlanacaktır.")
        ad_soyad=input("Lütfen adınızı ve soyadınızı arasında 1 boşluk olacak şekilde giriniz.").title()       
        try:            
            dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
            dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
            dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
            if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
                dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
                else:
                    pass
        except ValueError:
            print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
            try:
                dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
            except ValueError:
                print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                break
        dogum_tarihi=str(str(dogum_tarihi_gun)+"/"+str(dogum_tarihi_ay)+"/"+str(dogum_tarihi_yil))
        il = input("İkamet ettiğiniz il :").title()
        ilce = input("İkamet ettiğiniz ilçe :").title()
        mahalle = input("İkamet ettiğiniz mahalle :")
        if sozluk1_musteriler[kimlik_no]["Ad-Soyad"] == ad_soyad and sozluk1_musteriler[kimlik_no]["Doğum Tarihi"] == dogum_tarihi and sozluk1_musteriler[kimlik_no]["İl"]==il and sozluk1_musteriler[kimlik_no]["İlçe"]==ilce and sozluk1_musteriler[kimlik_no]["Mahalle"==mahalle]:
            try:
                a=int(input("Girdiğiniz bilgiler doğrudur. İşleme devam ederek, tüm hesap bilgilerini ve kredi bilgilerini silerek müşterimiz olmaktan vazgeçeceğinize emin misiniz?\nEvet:1,\nHayır:2\nCevap "))
                if a==1:
                    del sozluk1_musteriler[kimlik_no]
                    del sozluk2_hesap_bilgi[kimlik_no]
                    del sozluk3_kredi_bilgi[kimlik_no]
                    print("Tüm bilgileriniz ve müşteri kaydınız silinmiştir. Gittiğiniz için üzgünüz.")
                else:
                    print("Hatalı bir seçim yaptınız. İşlem sonlandırılmıştır.")
                    break
            except ValueError:
                print("Hatalı gir seçim yaptınız. İşlem sonlandırılmıştır.")
                break
        else:
            print("Girmiş olduğunuz bilgiler hatalır. Lütfen tekrar deneyiniz.")
            ad_soyad=input("Lütfen adınızı ve soyadınızı arasında 1 boşluk olacak şekilde giriniz.").title()       
            try:            
                dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                    print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
                    dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                    dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                    dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                    if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                        print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                        break
                    else:
                        pass
            except ValueError:
                print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
                try:
                    dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                    dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                    dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                    if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                        print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                        break
                except ValueError:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
            dogum_tarihi=str(str(dogum_tarihi_gun)+"/"+str(dogum_tarihi_ay)+"/"+str(dogum_tarihi_yil))
            il = input("İkamet ettiğiniz il :").title()
            ilce = input("İkamet ettiğiniz ilçe :").title()
            mahalle = input("İkamet ettiğiniz mahalle :")
            if sozluk1_musteriler[kimlik_no]["Ad-Soyad"] == ad_soyad and sozluk1_musteriler[kimlik_no]["Doğum Tarihi"] == dogum_tarihi and sozluk1_musteriler[kimlik_no]["İl"]==il and sozluk1_musteriler[kimlik_no]["İlçe"]==ilce and sozluk1_musteriler[kimlik_no]["Mahalle"]==mahalle:
                try:
                    a=int(input("Girdiğiniz bilgiler doğrudur. İşleme devam ederek, tüm hesap bilgilerini ve kredi bilgilerini silerek müşterimiz olmaktan vazgeçeceğinize emin misiniz?\nEvet:1,\nHayır:2\nCevap "))
                    if a==1:
                        del sozluk1_musteriler[kimlik_no]
                        del sozluk2_hesap_bilgi[kimlik_no]
                        del sozluk3_kredi_bilgi[kimlik_no]
                        print("Tüm bilgileriniz ve müşteri kaydınız silinmiştir. Gittiğiniz için üzgünüz.")
                    else:
                        print("Hatalı bir seçim yaptınız. İşlem sonlandırılmıştır.")
                        break
                except ValueError:
                    print("Hatalı gir seçim yaptınız. İşlem sonlandırılmıştır.")
                    break
            else:
                print("2. Kez hatalı giriş yaptınız. İşlem sonlandırılmıştır.")
                break

def kredi_talebi():
    for i in range(1):
        try:
            kimlik_no = int(input("Lütfen T.C. Kimlik Numaranızı 11 haneli olarak giriniz.\nKimlik No:"))        
            if kimlik_no in sozluk1_musteriler:
                pass
            else:
                kimlik_no = int(input("Lütfen T.C. Kimlik Numaranızı 11 haneli olarak giriniz.\nKimlik No:"))        
                if kimlik_no in sozluk1_musteriler:
                    pass
                else:
                    print("2. kez hatalı giriş yaptınız:İşlem sonlandırılmıştır.")
                    break
        except:
            print("Hatalı bir giriş yaptınız. Lütfen tekrar deneyiniz.")
            continue 
        print("Lütfen kimliğinizi doğrulayabilmemiz için; Ad-Soyad, Doğum tarihi, İkamet edilen il,ilçe ve mahalleyi giriniz. ")
        print("---UYARI---\nLütfen bilgilerinizi doğru giriniz. Hatalı girmeniz durumunda 2. kez deneyebilirsiniz. Tekrar hatalı girerseniz program sonlanacaktır.")
        ad_soyad=input("Lütfen adınızı ve soyadınızı arasında 1 boşluk olacak şekilde giriniz.").title()       
        try:            
            dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
            dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
            dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
            if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
                dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
                else:
                    pass
        except ValueError:
            print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
            try:
                dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
            except ValueError:
                print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                break
        dogum_tarihi=str(str(dogum_tarihi_gun)+"/"+str(dogum_tarihi_ay)+"/"+str(dogum_tarihi_yil))
        il = input("İkamet ettiğiniz il :").title()
        ilce = input("İkamet ettiğiniz ilçe :").title()
        mahalle = input("İkamet ettiğiniz mahalle :")
        if sozluk1_musteriler[kimlik_no]["Ad-Soyad"] == ad_soyad and sozluk1_musteriler[kimlik_no]["Doğum Tarihi"] == dogum_tarihi and sozluk1_musteriler[kimlik_no]["İl"]==il and sozluk1_musteriler[kimlik_no]["İlçe"]==ilce and sozluk1_musteriler[kimlik_no]["Mahalle"]==mahalle:
            try:
                a=("Girdiğiniz bilgiler doğrudur. İşleme devam ederek, talep ettiğiniz kredi tutarını giriniz ve onay veriniz.")
                kuraller.update({1:"Kredi talep işlemini sadece mevcut müşterilerimiz yapabilir",2:"Kredi talebinde bulunabilmek için hesabınız olması gerekmektedir.",
                3:"Kredi tutarınız, en fazla hesap bakiyenizin yarısı kadar olabilir.",3:"Kredi tutarınızın para cinsi, hesabınıza tanımlı para cinsi olarak işlecenektir."})
                print(a)
                for x,y in kuraller.items():
                    print(x,y)
                hesaptaki_bakiye_miktari = int(sozluk2_hesap_bilgi[kimlik_no]["Hesap Bakiyesi"])
                hesap_para_cinsi = sozluk2_hesap_bilgi[kimlik_no]["Hesap Para Cinsi"]
                print(f"Hesabınızın bakiyesi:{hesaptaki_bakiye_miktari}\nHesabınızın Para Cinsi: {hesap_para_cinsi}")
                kredi_talep_tutarı = int(input("Lütfen talep ettiğiniz kredi tutarını giriniz. (Not:Kredi miktarınız, hesabınızın para cinsine göre oluşturulacaktır.)"))
                if kredi_talep_tutarı<=hesaptaki_bakiye_miktari/2:
                    sozluk3_kredi_bilgi[kimlik_no]["Kredi Adeti"] = 1
                    sozluk3_kredi_bilgi[kimlik_no]["Kredi Limiti"] = kredi_talep_tutarı
                    print(f"Talep ettiğiniz kredi tutarı tanımlanmıştır.Güncel bilgileriniz aşağıdaki gibidir.")
                    for x,y in sozluk3_kredi_bilgi[kimlik_no].items():
                        print(str(x)+":"+str(y))
                else:
                    print("Talep ettiğiniz tutar, hesap bakiyenizin yarısından fazladır. Kredi talebiniz uygun görülmemiştir.\nİşlem sonlandırılmıştır.")
            except ValueError:
                print("Hatalı gir seçim yaptınız. İşlem sonlandırılmıştır.")
                break
        else:
            print("Girmiş olduğunuz bilgiler hatalır. Lütfen tekrar deneyiniz.")
            ad_soyad=input("Lütfen adınızı ve soyadınızı arasında 1 boşluk olacak şekilde giriniz.").title()       
            try:            
                dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                    print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
                    dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                    dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                    dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                    if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                        print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                        break
                    else:
                        pass
            except ValueError:
                print("Hatalı giriş yaptınız. Lütfen doğum tarihinize ilişkin bilgileri yönergelere göre giriniz.")
                try:
                    dogum_tarihi_gun=int(input("Doğduğunuz günü giriniz. Örnek:20\nCevap:"))
                    dogum_tarihi_ay=int(input("Doğduğunuz ayı giriniz. Örnek:01\nCevap:"))
                    dogum_tarihi_yil=int(input("Doğduğunuz yılı giriniz. Örnek:1997\nCevap:"))
                    if not 12>=dogum_tarihi_ay>0 and 31>=dogum_tarihi_gun>0 and 2004>=dogum_tarihi_yil>1900:
                        print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                        break
                except ValueError:
                    print("2. Kez hatalı giriş yaptınız. Program sonlanmıştır.")
                    break
            dogum_tarihi=str(str(dogum_tarihi_gun)+"/"+str(dogum_tarihi_ay)+"/"+str(dogum_tarihi_yil))
            il = input("İkamet ettiğiniz il :").title()
            ilce = input("İkamet ettiğiniz ilçe :").title()
            mahalle = input("İkamet ettiğiniz mahalle :")
            if sozluk1_musteriler[kimlik_no]["Ad-Soyad"] == ad_soyad and sozluk1_musteriler[kimlik_no]["Doğum Tarihi"] == dogum_tarihi and sozluk1_musteriler[kimlik_no]["İl"]==il and sozluk1_musteriler[kimlik_no]["İlçe"]==ilce and sozluk1_musteriler[kimlik_no]["Mahalle"]==mahalle:
                try:
                    a=("Girdiğiniz bilgiler doğrudur. İşleme devam ederek, talep ettiğiniz kredi tutarını giriniz ve onay veriniz.")
                    kuraller.update({1:"Kredi talep işlemini sadece mevcut müşterilerimiz yapabilir",2:"Kredi talebinde bulunabilmek için hesabınız olması gerekmektedir.",
                3:"Kredi tutarınız, en fazla hesap bakiyenizin yarısı kadar olabilir.",3:"Kredi tutarınızın para cinsi, hesabınıza tanımlı para cinsi olarak işlecenektir."})
                    print(a)
                    for x,y in kuraller.items():
                        print(x,y)
                    hesaptaki_bakiye_miktari = int(sozluk2_hesap_bilgi[kimlik_no]["Hesap Bakiyesi"])
                    hesap_para_cinsi = sozluk2_hesap_bilgi[kimlik_no]["Hesap Para Cinsi"]
                    print(f"Hesabınızın bakiyesi:{hesaptaki_bakiye_miktari}\nHesabınızın Para Cinsi: {hesap_para_cinsi}")
                    kredi_talep_tutarı = int(input("Lütfen talep ettiğiniz kredi tutarını giriniz. (Not:Kredi miktarınız, hesabınızın para cinsine göre oluşturulacaktır.)"))
                    if kredi_talep_tutarı<=hesaptaki_bakiye_miktari/2:
                        sozluk3_kredi_bilgi[kimlik_no]["Kredi Adeti"] = 1
                        sozluk3_kredi_bilgi[kimlik_no]["Kredi Limiti"] = kredi_talep_tutarı
                        print(f"Talep ettiğiniz kredi tutarı tanımlanmıştır.Güncel bilgileriniz aşağıdaki gibidir.")
                        for x,y in sozluk3_kredi_bilgi[kimlik_no].items():
                            print(str(x)+":"+str(y))
                    else:
                        print("Talep ettiğiniz tutar, hesap bakiyenizin yarısından fazladır. Kredi talebiniz uygun görülmemiştir.\nİşlem sonlandırılmıştır.")
                except ValueError:
                    print("Hatalı gir seçim yaptınız. İşlem sonlandırılmıştır.")
                    break
            else:
                print("2. Kez hatalı giriş yaptınız. İşlem sonlandırılmıştır.")
                break



    
print(hosgeldin_mesaji)
islem_listesi= "Yeni müşteri olma işlemi : 1\nMüşteri İptal İşlemi : 2\nhesap açma işlemi(mevcut müşteri) : 3\nKredi Talebi(Mevcut müşteri) : 4"
print(f"Lütfen yapmak istediğiniz işlemi seçiniz.\n{islem_listesi}".title())
while True:
    for i in range(1):
        islem_secimi=input("Cevap :")
        if islem_secimi=="1":
            musteri_olma()
        elif islem_secimi=="2":
            musteri_kayit_silme()
        elif islem_secimi=="3":
            kayitli_musteri_hesap_acma()
        elif islem_secimi=="4":
            kredi_talebi()
        else:
            print("Yanlış bir seçim yaptınız. Program sonlanmıştır")
            break
    islem_devam_durumu=input("Uygulamaya devam etmek istiyor musunuz ?\nEvet:1\nHayır:2\nCevap:")
    if islem_devam_durumu=="1":
        print("Uygulamaya devam edebilirsiniz.")
        print(f"Bankacılık uygulamamıza hoşgeldiniz. Lütfen yapmak istediğiniz işlemi seçiniz.\n{islem_listesi}".title())
        continue
    elif islem_devam_durumu=="2":
        print(cikis_mesaji)
        break
    else:
        print("Yanlış bir seçim yaptınız. Uygulama sonlanmıştır.")
        print(cikis_mesaji)
        break
    
