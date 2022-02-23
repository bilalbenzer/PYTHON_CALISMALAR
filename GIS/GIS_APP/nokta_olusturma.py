from shapely.geometry import Point   #gerekli kütüphane

"""         OLUŞTURULACAK POİNTLER İÇİN ÖZNİTELİK BİLGİLERİNİ İÇEREN CLASSLARIM         """
class point2d():
    geometri_tip = "Point"
    def __init__(self):
        nokta_adi = str()
        x_koordinati = float()
        y_koordinati = float()
class point3d():
    geometri_tip = "Point Z"
    def __init__(self):
        nokta_adi = str()
        x_koordinati = float()
        y_koordinati = float()
        z_koordinati = float()
"""         NOKTA OLUŞTURMA         """
def nokta_olustur():
    for i in range(1):  #hatalı durumlarda break kullanılması için 1 döngülük for kullanıyoruz.
        ikid_nokta = "" #z bilgisi içermeyen nokta için ön tanımlı değişken
        ucd_nokta = ""  #z bilgisi içeren nokta için ön tanımlı değişken
        print("İşleme devam edebilirsiniz.\nSırasıyla noktalnın x,y ve varsa z değerini giriniz. z değeri yoksa eğer, boş bırakabilir veya 0 girebilirsiniz.")
        try:
            nokta_adi = input("Nokta Adı:")
            x_degeri = float((input("Nokta-x:")).replace(",", ".")) #kullanıcıdan x değeri alma
            y_degeri = float((input("Nokta-y:")).replace(",", ".")) #kullanıcıdan y değeri alma
            z_degeri = input("Nokta-z:")     #kullanıcıdan z değeri alma
            if z_degeri!='':    #kullanıcı z değeri verirse bu blok çalışacak
                z_degeri = float((z_degeri).replace(",", "."))
            else:    #kullanıcı z değerini boş bırakırsa bu blok çalışacak
                z_degeri = 0
        except ValueError as hata:  #hata olması durumunda (float yerine karakter girilmesi vs)
            print(f"Hata metni\n{hata}")
            print(f"Yanlış bir seçim yaptınız. Lütfen bir sayı değeri giriniz.")    #2. kez veri istenecek
            try:
                
                x_degeri = float((input("Nokta-x:")).replace(",", ".")) #kullanıcıdan x değeri alma
                y_degeri = float((input("Nokta-y:")).replace(",", ".")) #kullanıcıdan y değeri alma
                z_degeri = input("Nokta-z:")    #kullanıcıdan z değeri alma
                if z_degeri!='':    #kullanıcı z değeri verirse bu blok çalışacak
                    z_degeri = float((z_degeri).replace(",", "."))  
                else:   #kullanıcı z değerini boş bırakırsa bu blok çalışacak
                    z_degeri = 0
            except ValueError as hata:  #hata olması durumunda (float yerine karakter girilmesi vs)
                print(f"Hata metni\n{hata}")    
                print(f"Yanlış bir seçim yaptınız. İşlem sonlanmıştır.")
                break   #2. kez hatalı giriş olduğu için fonksiyon sonlanacak
        else:
            print("İşleme devam edebilirsiniz.")    #x y z değeri almada bir problem olmaz ise işlem devam edecek
            print("Girmiş olduğunuz koordinatlara göre nokta oluşturulmuştur.Lütfen koordinat bilgilerini kontrol ediniz ve onaylayarak işleme devam ediniz.")
            if z_degeri>0 or z_degeri<0:    
                ucd_nokta = "var"       #kullanıcı z değeri vermiş ise ön tanım olarak yapılan ucd_nokta değişkenine veri atayacak
                nokta1 = point3d()      #z değeri var ise point3d classında bir değişken tanımlıyoruz
                nokta1.nokta_adi, nokta1.x_koordinati,nokta1.y_koordinati,nokta1.z_koordinati = nokta_adi,x_degeri,y_degeri,z_degeri   #değişkenimize kullanıcının verdiği bilgileri giriyoruz.
                print("Gometri Tipi",nokta1.geometri_tip,"\nNokta Adı",nokta1.nokta_adi,"\nX Koordinatı", nokta1.x_koordinati,"\nY Koordinatı",nokta1.y_koordinati,"\nZ Koordinatı",nokta1.z_koordinati)    #ekranda girilen değerleri gösteriyoruz
            elif z_degeri == 0:   #kullanıcı z değeri vermemişse point 2d olarak aktarılacak
                nokta1 = point2d()  # z değeri olmadığı için point2d sınıfnda bir değişken oluşturuyoruz
                nokta1.nokta_adi, nokta1.x_koordinati,nokta1.y_koordinati = nokta_adi ,x_degeri,y_degeri    #kullanıcıdan gelen bilgileri tanımladığımız değişkene veriyoruz
                print("Gometri Tipi",nokta1.geometri_tip,"\nNokta Adı",nokta1.nokta_adi,"\nX Koordinatı", nokta1.x_koordinati,"\nY Koordinatı",nokta1.y_koordinati) #kullanıcıya gösterme
                ikid_nokta = "var"  #z değeri olmadığı için ikid_nokta değişkenine "var" denilecek

        """         POİNT OBJESİ OLUŞTURULDUKTAN SONRA DIŞARI AKTARMA SEÇENEKLERİ       """

        print("Girmiş olduğunuz nokta değerini \"1-SHP,2-TXT,3-XML,4-XLSX,5-PDF,6-CSV,7-DOCX\" formatlarında saklayabilirsiniz.\nBu formatlardan herhangi birisine aktarım yapmak istiyorsanız lütfen ilgili format numarasını tuşlayınız.")
        
        dosya_format_tip = input("Dosya Tipi No:")  #kullanıcdan dosya çıktı için numara alma
        if dosya_format_tip =="1":  #kullanıcı 1 verisiyle cevap verirse shp oluşturma bloğu çalışacak
            if ikid_nokta=="var":   #z değeri olmayan pointler iki d olarak ele alınmıştı ve ikid_nokta değişkenine var atanmıştı. bu durum varsa bu blok çalışacak
                from dosya_formatlarında_kaydetme import shape_olustur2d    #shp aktarımı için oluşturduğum modülün import edilmesi
                shape_olustur2d(ikid_nokta_tuple)   #2d point objelerinin çıktıya gönderimi
            else:   #2d point yok ise pas geçilecek
                pass
            if ucd_nokta=="var":    #3d point var ise bu blok çalışacak
                print("Projenizde koordinat içeren nokta ögesi bulunmakta. Z değeri içeren noktalar farklı bir shape dosyasında saklanmalıdır.")    #z değeri içeren pointler farklı shpde saklanacak
                from dosya_formatlarında_kaydetme import shape_olustur3d    #3d point aktarımı için, oluştturduğum modül ve ilgili fonksiyon import edilecek
                shape_olustur3d(ucd_nokta_tuple)    #point, çıktıya verilecek
            else:   #3d point yok ise pas geçielcek
                pass
        elif dosya_format_tip =="2":    #kullanıcı 2 girişi verirse bu blkok çalışacak
            if ikid_nokta=="var":   #2d nokta için aktaırm
                from dosya_formatlarında_kaydetme import text_olusturma2d
                text_olusturma2d(ikid_nokta_tuple)
            else:
                pass
            if ucd_nokta=="var":    #3d nokta için aktarım
                from dosya_formatlarında_kaydetme import text_olusturma3d
                text_olusturma3d(ucd_nokta_tuple)
            else:
                pass
        elif dosya_format_tip =="3":    #kullanıcı 3 girişi verirse bu blok çalışacak
            if ikid_nokta=="var":   #2d point aktarım
                from dosya_formatlarında_kaydetme import xml_olusturma2d
                xml_olusturma2d(ikid_nokta_tuple)
            else:
                pass
            if ucd_nokta=="var":    #3d nokta aktarım
                from dosya_formatlarında_kaydetme import xml_olusturma3d
                xml_olusturma3d(ucd_nokta_tuple)
            else:
                pass
        elif dosya_format_tip =="4":    #kullanıcı 4 girişi verirse bu blok çalışacak
            if ikid_nokta=="var":   #2d nokta aktarım
                from dosya_formatlarında_kaydetme import xlsx_olusturma2d
                xlsx_olusturma2d(ikid_nokta_tuple)
            else:
                pass
            if ucd_nokta=="var":    #3d nokta aktarım
                from dosya_formatlarında_kaydetme import xlsx_olusturma2d
                xlsx_olusturma2d(ucd_nokta_tuple)
            else:
                pass

        else:
            print("Dosya format tipini yanlış seçtiniz. Program sonlanmıştır.")
            break
    else:
        ikid_nokta_tuple = ()   #aktarım tamamlandıktan sonra tuple nesneleri boşaltılacak
        ucd_nokta_tuple = ()    