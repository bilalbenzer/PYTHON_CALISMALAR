from shapely.geometry import Point   #gerekli kütüphane

def nokta_olustur():
    for i in range(1):  #hatalı durumlarda break kullanılması için 1 döngülük for kullanıyoruz.
        ikid_nokta_tuple = ()
        ucd_nokta_tuple = ()
        ikid_nokta = ""
        ucd_nokta = ""
        print("İşleme devam edebilirsiniz.\nSırasıyla noktalnın x,y ve varsa z değerini giriniz. z değeri yoksa eğer, boş bırakabilir veya 0 girebilirsiniz.")
        try:
            x_degeri = float(input("Nokta-x:"))
            y_degeri = float(input("Nokta-y:"))
            z_degeri = input("Nokta-z:")
            if z_degeri!='':
                z_degeri = float(z_degeri)
            else:
                z_degeri = 0
        except ValueError as hata:
            print(f"Hata metni\n{hata}")
            print(f"Yanlış bir seçim yaptınız. Lütfen bir sayı değeri giriniz.")
            try:
                x_degeri = float(input("Nokta-x:"))
                y_degeri = float(input("Nokta-y:"))
                z_degeri = input("Nokta-z:")
                if z_degeri!='':
                    z_degeri = float(z_degeri)
                else:
                    z_degeri = 0
                    
            except ValueError as hata:
                print(f"Hata metni\n{hata}")
                print(f"Yanlış bir seçim yaptınız. İşlem sonlanmıştır.")
                break
        else:
            print("İşleme devam edebilirsiniz.")
            if z_degeri>0 or z_degeri<0:
                ucd_nokta = "var"
                nokta3d= Point([x_degeri,y_degeri,z_degeri])
            else:
                ikid_nokta = "var"
                nokta2d=Point([x_degeri,y_degeri])
            print("Girmiş olduğunuz koordinatlara göre nokta oluşturulmuştur.Lütfen koordinat bilgilerini kontrol ediniz ve onaylayarak işleme devam ediniz.")
            if ucd_nokta=="var":
                print(ucd_nokta)
                ucd_nokta_tuple=(nokta3d)
            elif ikid_nokta=="var":
                print(ikid_nokta)
                ikid_nokta_tuple=(nokta2d)
        print("Girmiş olduğunuz nokta değerini \"1-SHP,2-TXT,3-XML,4-XLSX,5-PDF,6-CSV,7-DOCX\" formatlarında saklayabilirsiniz.\nBu formatlardan herhangi birisine aktarım yapmak istiyorsanız lütfen ilgili format numarasını tuşlayınız.")
        dosya_format_tip = input("Dosya Tipi No:")
        if dosya_format_tip =="1":
            if ikid_nokta=="var":
                from dosya_formatlarında_kaydetme import shape_olustur2d
                shape_olustur2d(ikid_nokta_tuple)
            else:
                pass
            if ucd_nokta=="var":
                print("Projenizde koordinat içeren nokta ögesi bulunmakta. Z değeri içeren noktalar farklı bir shape dosyasında saklanmalıdır.")
                from dosya_formatlarında_kaydetme import shape_olustur3d
                shape_olustur3d(ucd_nokta_tuple)
            else:
                pass
        if dosya_format_tip =="2":
            if ikid_nokta=="var":
                from dosya_formatlarında_kaydetme import text_olusturma2d
                text_olusturma2d(ikid_nokta_tuple)
            else:
                pass
            if ucd_nokta=="var":
                from dosya_formatlarında_kaydetme import text_olusturma3d
                text_olusturma3d(ucd_nokta_tuple)
            else:
                pass
        if dosya_format_tip =="3":
            if ikid_nokta=="var":
                from dosya_formatlarında_kaydetme import xml_olusturma2d
                xml_olusturma2d(ikid_nokta_tuple)
            else:
                pass
            if ucd_nokta=="var":
                from dosya_formatlarında_kaydetme import xml_olusturma3d
                xml_olusturma3d(ucd_nokta_tuple)
            else:
                pass