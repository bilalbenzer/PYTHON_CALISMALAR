from shapely.geometry import Point   #gerekli kütüphane

def nokta_olustur():
    for i in range(1):  #hatalı durumlarda break kullanılması için 1 döngülük for kullanıyoruz.
        nokta_no = 0    #1den fazla nokta girilmesi durumunda 1. nokta, 2. nokta ifadesi için yardımcı bir değişken
        try:            #kullanıcıya kaç tane nokta gireceğini soruyoruz
            adet = int(input("Kaç adet nokta oluşturmak istiyorsunuz ?\nAdet: "))
        except ValueError as hata:  #kullanıcı str bir ifade veya sayı dışında giriş yapmaması için hata yakalama çalıştıroyruz
            print(f"Hata metni\n{hata}")    #hata metni
            print(f"Yanlış bir seçim yaptınız. Lütfen bir sayı değeri giriniz.")
            try:    #1. hatadan sonra 2. kez giriş hakkı
                adet = int(input("Kaç adet nokta oluşturmak istiyorsunuz ?\nAdet: "))
            except ValueError as hata:
                print(f"Hata metni\n{hata}")
                print(f"Yanlış bir seçim yaptınız. İşlem sonlanmıştır.")
                break
        else:   #kullanıcı adet bilgisini doğru girmişse else ile devam sağlıyoruz
            print("İşleme devam edebilirsiniz.\nSırasıyla noktaların x,y ve varsa z değerini giriniz. z değeri yoksa eğer, boş bırakabilir veya 0 girebilirsiniz.")
            nokta_listesi2d = 0 
            nokta_listesi3d = 0
            nokta_listesi2d = []
            nokta_listesi3d = []
            for i in range(adet):
                nokta_no+=1
                try:
                    x_degeri = float(input(f"{nokta_no}. Nokta-x:"))
                    y_degeri = float(input(f"{nokta_no}. Nokta-y:"))
                    z_degeri = input(f"{nokta_no}. Nokta-z:")
                    if z_degeri!='':
                        z_degeri = float(z_degeri)
                    else:
                        z_degeri = 0
                except ValueError as hata:
                    print(f"Hata metni\n{hata}")
                    print(f"Yanlış bir seçim yaptınız. Lütfen bir sayı değeri giriniz.")
                    try:
                        x_degeri = float(input(f"{nokta_no}. Nokta-x:"))
                        y_degeri = float(input(f"{nokta_no}. Nokta-y:"))
                        z_degeri = input(f"{nokta_no}. Nokta-z:")
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
                        nokta3d= Point([x_degeri,y_degeri,z_degeri])
                        nokta_listesi3d.append(nokta3d)
                    else:
                        nokta2d=Point([x_degeri,y_degeri])
                        nokta_listesi2d.append(nokta2d)
            else:
                print("Girmiş olduğunuz noktalara göre koordinatlar oluşturulmuştur.Lütfen koordinat bilgilerini kontrol ediniz ve onaylayarak işleme devam ediniz.")
                if nokta_listesi2d !=[]:
                    for i in nokta_listesi2d:
                        print(i)
                if nokta_listesi3d != []:
                    for i in nokta_listesi3d:
                        print(i)
        noktalar2d = tuple(nokta_listesi2d)
        noktalar3d = tuple(nokta_listesi3d)
    else:
        print("Girmiş olduğunuz nokta değerlerini \"1-SHP,2-TXT,3-XML,4-XLSX,5-PDF,6-CSV,7-DOCX\" formatlarında saklayabilirsiniz.\nBu formatlardan herhangi birisine aktarım yapmak istiyorsanız lütfen ilgili format numarasını tuşlayınız.")
        dosya_format_tip = input("Dosya Tipi No:")
        if dosya_format_tip =="1":
            if nokta_listesi2d!=[]:
                from dosya_formatlarında_kaydetme import shape_olustur2d
                shape_olustur2d(noktalar2d)
            else:
                pass
            if nokta_listesi3d !=[]:
                print("Projenizde koordinat içeren nokta ögesi bulunmakta. Z değeri içeren noktalar farklı bir shape dosyasında saklanmalıdır.")
                from dosya_formatlarında_kaydetme import shape_olustur3d
                shape_olustur3d(noktalar3d)
            else:
                pass
        elif dosya_format_tip =="2":
            if nokta_listesi2d!=[]:
                from dosya_formatlarında_kaydetme import text_olusturma2d
                text_olusturma2d(noktalar2d)
            else:
                pass
            if nokta_listesi3d !=[]:
                from dosya_formatlarında_kaydetme import text_olusturma3d
                text_olusturma3d(noktalar3d)
            else:
                pass
        elif dosya_format_tip =="3":
            if nokta_listesi2d!=[]:
                from dosya_formatlarında_kaydetme import xml_olusturma2d
                xml_olusturma2d(noktalar2d)
            else:
                pass
            if nokta_listesi3d !=[]:
                from dosya_formatlarında_kaydetme import xml_olusturma3d
                xml_olusturma3d(noktalar3d)
            else:
                pass
        elif dosya_format_tip =="4":
            if nokta_listesi2d!=[]:
                from dosya_formatlarında_kaydetme import xlsx_olusturma2d
                xlsx_olusturma2d(noktalar2d)
            else:
                pass
            if nokta_listesi3d !=[]:
                from dosya_formatlarında_kaydetme import xlsx_olusturma2d
                xlsx_olusturma3d(noktalar3d)
            else:
                pass

        else:
            print("Dosya format tipini yanlış seçtiniz. Program sonlanmıştır.")
            break



