from shapely.geometry import Point   #gerekli kütüphane
from siniflar import point2d,point3d
"""         OLUŞTURULACAK POİNTLER İÇİN ÖZNİTELİK BİLGİLERİNİ İÇEREN CLASSLARIM         """

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
            koordinat_sistemi = input("Koordinat Sistemi (EPSG Kodu):")
            try:
                koordinat_sistemi = int(koordinat_sistemi)
                pass
            except:
                print("Koordinat Sistemi EPSG Kodunu Yanlış Girdiniz. Lütfen Tekrar denemek için 1, çıkmak için 2'yi tuşlayınız.")
                if input(":") =="1":
                    return nokta_olustur()
                if input(":") =="2":
                    break
            if z_degeri!='':    #kullanıcı z değeri verirse bu blok çalışacak
                z_degeri = float((z_degeri).replace(",", "."))
            else:    #kullanıcı z değerini boş bırakırsa bu blok çalışacak
                z_degeri = 0
        except ValueError as hata:  #hata olması durumunda (float yerine karakter girilmesi vs)
            print(f"Hata metni\n{hata}")
            print(f"Yanlış bir seçim yaptınız. Lütfen bir sayı değeri giriniz.")    #2. kez veri istenecek
            try:
                nokta_adi = input("Nokta Adı:")
                x_degeri = float((input("Nokta-x:")).replace(",", ".")) #kullanıcıdan x değeri alma
                y_degeri = float((input("Nokta-y:")).replace(",", ".")) #kullanıcıdan y değeri alma
                z_degeri = input("Nokta-z:")     #kullanıcıdan z değeri alma
                koordinat_sistemi = input("Koordinat Sistemi (EPSG Kodu):")
                try:
                    koordinat_sistemi = int(koordinat_sistemi)
                    pass
                except:
                    print("Koordinat Sistemi EPSG Kodunu Yanlış Girdiniz. Lütfen Tekrar denemek için 1, çıkmak için 2'yi tuşlayınız.")
                    if input(":") =="1":
                        return nokta_olustur()
                    if input(":") =="2":
                        break
                if z_degeri!='':    #kullanıcı z değeri verirse bu blok çalışacak
                    z_degeri = float((z_degeri).replace(",", "."))
                else:    #kullanıcı z değerini boş bırakırsa bu blok çalışacak
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
                nokta1 = point3d(point_name=nokta_adi,x_koordinati=x_degeri,y_koordinati=y_degeri,z_koordinati=z_degeri,crs_kod_epsg=koordinat_sistemi)      #z değeri var ise point3d classında bir değişken tanımlıyoruz
                #kullanıcıdan gelen bilgileri nokta2d sınıfında oluşan değişkene veriyoruz
                print(f"""
Nokta Adı   :       {nokta1.name}
X Koordinatı:       {nokta1.x}
Y Koordinatı:       {nokta1.y}
Z Koordinatı:       {nokta1.z}
Koordinat Sistemi:  {nokta1.crs_system}
                """)
            elif z_degeri == 0:   #kullanıcı z değeri vermemişse point 2d olarak aktarılacak
                ikid_nokta = "var"  #z değeri olmadığı için ikid_nokta değişkenine "var" denilecek
                nokta1 = point2d(point_name=nokta_adi,x_koordinati=x_degeri,y_koordinati=y_degeri,crs_kod_epsg=koordinat_sistemi)  # z değeri olmadığı için point2d sınıfnda bir değişken oluşturuyoruz                        
                print(f"""
Nokta Adı   :       {nokta1.name}
X Koordinatı:       {nokta1.x}
Y Koordinatı:       {nokta1.y}
Koordinat Sistemi:  {nokta1.crs_system}
                """)
        girilen_bilgiler_dogru_mu = input("Girilen bilgilerde sorun var ise lütfen 1'i tuşlayınız.Devam etmek için 'enter' a basınız.")
        if girilen_bilgiler_dogru_mu =="1":
            nokta_olustur()
        else:
            pass

        """         POİNT OBJESİ OLUŞTURULDUKTAN SONRA DIŞARI AKTARMA SEÇENEKLERİ       """
        print("Girmiş olduğunuz nokta değerini \"1-SHP,2-TXT,3-XML,4-XLSX,5-PDF,6-CSV,7-DOCX\" formatlarında saklayabilirsiniz.\nBu formatlardan herhangi birisine aktarım yapmak istiyorsanız lütfen ilgili format numarasını tuşlayınız.")
        geometri_tipi = "nokta"
        dosya_format_tip = input("Dosya Tipi No:")  #kullanıcdan dosya çıktı için numara alma
        if dosya_format_tip =="1":  #kullanıcı 1 verisiyle cevap verirse shp oluşturma bloğu çalışacak
            if ikid_nokta=="var":   #z değeri olmayan pointler iki d olarak ele alınmıştı ve ikid_nokta değişkenine var atanmıştı. bu durum varsa bu blok çalışacak
                from dosya_formatlarında_kaydetme import shape_olustur2d    #shp aktarımı için oluşturduğum modülün import edilmesi
                shape_olustur2d(nokta1,geometri_tipi)   #2d point objelerinin çıktıya gönderimi
            else:   #2d point yok ise pas geçilecek
                pass
            if ucd_nokta=="var":    #3d point var ise bu blok çalışacak
                print("Projenizde koordinat içeren nokta ögesi bulunmakta. Z değeri içeren noktalar farklı bir shape dosyasında saklanmalıdır.")    #z değeri içeren pointler farklı shpde saklanacak
                from dosya_formatlarında_kaydetme import shape_olustur3d    #3d point aktarımı için, oluştturduğum modül ve ilgili fonksiyon import edilecek
                shape_olustur3d(nokta1,geometri_tipi)    #point, çıktıya verilecek
            else:   #3d point yok ise pas geçielcek
                pass
        elif dosya_format_tip =="2":    #kullanıcı 2 girişi verirse bu blkok çalışacak
            if ikid_nokta=="var":   #2d nokta için aktaırm
                from dosya_formatlarında_kaydetme import text_olusturma2d
                text_olusturma2d(nokta1,geometri_tipi)
            else:
                pass
            if ucd_nokta=="var":    #3d nokta için aktarım
                from dosya_formatlarında_kaydetme import text_olusturma3d
                text_olusturma3d(nokta1,geometri_tipi)
            else:
                pass
        elif dosya_format_tip =="3":    #kullanıcı 3 girişi verirse bu blok çalışacak
            if ikid_nokta=="var":   #2d point aktarım
                from dosya_formatlarında_kaydetme import xml_olusturma2d
                xml_olusturma2d(nokta1,geometri_tipi)
            else:
                pass
            if ucd_nokta=="var":    #3d nokta aktarım
                from dosya_formatlarında_kaydetme import xml_olusturma3d
                xml_olusturma3d(nokta1,geometri_tipi)
            else:
                pass
        elif dosya_format_tip =="4":    #kullanıcı 4 girişi verirse bu blok çalışacak
            if ikid_nokta=="var":   #2d nokta aktarım
                from dosya_formatlarında_kaydetme import xlsx_olusturma2d
                xlsx_olusturma2d(nokta1,geometri_tipi)
            else:
                pass
            if ucd_nokta=="var":    #3d nokta aktarım
                from dosya_formatlarında_kaydetme import xlsx_olusturma3d
                xlsx_olusturma3d(nokta1,geometri_tipi)
            else:
                pass
        elif dosya_format_tip =="5":    #kullanıcı 4 girişi verirse bu blok çalışacak
            if ikid_nokta=="var":   #2d nokta aktarım
                from dosya_formatlarında_kaydetme import pdf_olusturma2d
                pdf_olusturma2d(nokta1,geometri_tipi)
            else:
                pass
            if ucd_nokta=="var":    #3d nokta aktarım
                from dosya_formatlarında_kaydetme import pdf_olusturma3d
                pdf_olusturma3d(nokta1,geometri_tipi)
            else:
                pass
        elif dosya_format_tip =="6":    #kullanıcı 4 girişi verirse bu blok çalışacak
            if ikid_nokta=="var":   #2d nokta aktarım
                from dosya_formatlarında_kaydetme import csv_olusturma2d
                csv_olusturma2d(args, tip)(nokta1,geometri_tipi)
            else:
                pass
            if ucd_nokta=="var":    #3d nokta aktarım
                from dosya_formatlarında_kaydetme import csv_olusturma3d
                csv_olusturma3d(args, tip)(nokta1,geometri_tipi)
            else:
                pass
        else:
            print("Dosya format tipini yanlış seçtiniz. Program sonlanmıştır.")
            break