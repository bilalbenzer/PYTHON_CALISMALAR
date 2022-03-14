from shapely.geometry import Point   #gerekli kütüphane
from my_classes import create_point , create_multi_point , settings , listen_to_voice_command
import time
ara_satir_cizgi = "\n------------------------------------------------------------------------------------------------------------------------------------\n"

def listening_you():
    a = settings("Open")
    b = listen_to_voice_command(a)
    b.listen_tr()
    global command1
    command1 = b.text
def listening_you_for_coordinat():
    a = settings("Open")
    b = listen_to_voice_command(a)
    b.listen_tr_coordinate()
    global command1
    command1 = b.coordinate

def create_point_with_voice_tr():
    while True:
        print("Nokta Adını Söyleyiniz.")    #sesli tanıma başlamadan önce kullanıcıya nokta adını söylemesi bildirilir
        print(ara_satir_cizgi)   
        for i in range(2):
            listening_you() #ses tanıma başlar
            if command1 !="":    #
                point_name = str(command1)
                break
            else:
                print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz.")    #sesli tanıma başlamadan önce kullanıcıya nokta adını söylemesi bildirilir
                print(ara_satir_cizgi)
        else:
            print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
            point_name = input("Nokta Adı:")


        print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
        for i in range(1,6):
            time.sleep(1)
            print(f"{i}")

        
        """ X Koordinatının Girileceği Bölüm """
        for i in range(2):
            print("X Koordinatını Söyleyiniz.Daha Doğru Bir Tanıma İçin Rakamları İkişer İkişer Söyleyebilirsiniz.")
            print(ara_satir_cizgi)
            listening_you_for_coordinat()
            if command1 !="":
                x_coordinate = float(str(command1))
                print(f"X Koordinatı: {x_coordinate}")
                break
            else:
                print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz\n X Koordinatını Söyleyiniz.\n")
                print(ara_satir_cizgi)
        else:
            print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
            for i in range(2):
                try:
                    x_coordinate = float(input("X Koordinatını Klavye İle Tuşlayınız.Örnek:7894567.254\n:").replace(",", ","))
                    break
                except ValueError as error:
                    print("Sayı Değeri Girilmelidir.İptal Etmek İçin 0'a Basınız.Devam Etmek İçin 0 Haricinde Bİr Tuşa Basmanız Yeterli.")
                    if input(":") =="0":
                        break
                    else:
                        pass


        print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
        for i in range(1,6):
            time.sleep(1)
            print(f"{i}")


        """ Y Koordinatının Girileceği Bölüm """
        for i in range(2):
            print("Y Koordinatını Söyleyiniz.Daha Doğru Bir Tanıma İçin Rakamları İkişer İkişer Söyleyebilirsiniz.")
            print(ara_satir_cizgi)
            listening_you_for_coordinat()
            if command1 !="":
                y_coordinate = float(str(command1))
                print(f"Y Koordinatı: {y_coordinate}")
                break
            else:
                print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz\n Y Koordinatını Söyleyiniz.\n")
                print(ara_satir_cizgi)
        else:
            print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
            for i in range(2):
                try:
                    y_coordinate = float(input("Y Koordinatını Klavye İle Tuşlayınız.Örnek:7894567.254\n:").replace(",", ","))
                    break
                except ValueError as error:
                    print("Sayı Değeri Girilmelidir.İptal Etmek İçin 0'a Basınız.Devam Etmek İçin 0 Haricinde Bİr Tuşa Basmanız Yeterli.")
                    if input(":") =="0":
                        break
                    else:
                        pass 


        print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
        for i in range(1,6):
            time.sleep(1)
            print(f"{i}")


        """ Z Koordinatının Girileceği Bölüm """
        for i in range(2):
            print("Z Koordinatını Söyleyiniz.Daha Doğru Bir Tanıma İçin Rakamları İkişer İkişer Söyleyebilirsiniz.")
            print(ara_satir_cizgi)
            listening_you_for_coordinat()
            if command1 !="":
                z_coordinate = float(str(command1))
                print(f"Z Koordinatı: {z_coordinate}")
                break
            else:
                print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz\n Z Koordinatını Söyleyiniz.\n")
                print(ara_satir_cizgi)
        else:
            print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
            for i in range(2):
                try:
                    z_coordinate = float(input("Z Koordinatını Klavye İle Tuşlayınız.Örnek:7894567.254\n:").replace(",", ","))
                    break
                except ValueError as error:
                    print("Sayı Değeri Girilmelidir.İptal Etmek İçin 0'a Basınız.Devam Etmek İçin 0 Haricinde Bİr Tuşa Basmanız Yeterli.")
                    if input(":") =="0":
                        break
                    else:
                        pass


        print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
        for i in range(1,6):
            time.sleep(1)
            print(f"{i}")


        """ Koordinat Sisteminin Girileceği Bölüm """
        for i in range(2):
            print("Koordinat Sisteminin EPSG Kodunu Söyleyiniz.Daha Doğru Bir Tanıma İçin Rakamları İkişer İkişer, Teker Teker veya Sayının Kendisini Söyleyebilirsiniz.")
            print(ara_satir_cizgi)
            listening_you_for_coordinat()
            if command1 !="":
                coordinat_system = float(str(command1))
                print(f"Koordinat Sistemi EPSG Kodu: {coordinat_system}")
                break
            else:
                print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nKoordinat Sistemi EPSG Kodunu Söyleyiniz.\n:")
                print(ara_satir_cizgi)
        else:
            print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
            for i in range(2):
                try:
                    coordinat_system = float(input("Koordinat Sistemi EPSG Kodunu Söyleyiniz. Örnek:2320\n:").replace(",", ","))
                    break
                except ValueError as error:
                    print("Sayı Değeri Girilmelidir.İptal Etmek İçin 0'a Basınız.Devam Etmek İçin 0 Haricinde Bİr Tuşa Basmanız Yeterli.")
                    if input(":") =="0":
                        break
                    else:
                        pass

        print(f"""Girilen Değerler Aşağıdaki Gibidir.
Nokta Adı:              {point_name}
X Koordinatı:           {x_coordinate}
Y Koordinatı:           {y_coordinate}
Z Koordinatı:           {z_coordinate}
Koordinat Sistmei:      {coordinat_system}
""")


        print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
        for i in range(1,6):
            time.sleep(1)
            print(f"{i}")


        """ Girilen Değerlerin Kontrolü """
        for i in range(2):
            print("Girilen Bilgiler Doğru İse 1, Yanlış İse 2 Cevabını Veriniz.\n:")
            listening_you()
            true_secenekler = ["1", "doğru", "evet"]
            false_secenekler = ["2","yanlış","hatalı","hayır"]


            print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
            for i in range(1,6):
                time.sleep(1)
                print(f"{i}")


            if true_secenekler.count(command1):
                print("Girdiğiniz Değer İle Nokta Objesi Oluşturuluyor. Lütfen Bekleyin...")
                a = create_point(point_name=point_name,x_coordinate=x_coordinate,y_coordinate=y_coordinate,z_coordinate=z_coordinate,crs_kod_epsg=coordinat_system)
                print(a.attribute)
                break
            else:
                print("Lütfen Hatalı Olan Kısmı Söyleyiniz.Düzeltme İçin 2 Hakkınız Bulunmakta.\n:")


                print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
                for i in range(1,6):
                    time.sleep(1)
                    print(f"{i}")


                for_nokta_adi = ["nokta adı", "nokta ismi", "ad", "isim", "noktanın adı"]
                if for_nokta_adi.count(command1):
                    print("Nokta Adını Söyleyiniz.")    #sesli tanıma başlamadan önce kullanıcıya nokta adını söylemesi bildirilir
                    print(ara_satir_cizgi)   
                    for i in range(2):
                        listening_you() #ses tanıma başlar
                        if command1 !="":    #
                            point_name = str(command1)
                            break
                        else:
                            print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz.")    #sesli tanıma başlamadan önce kullanıcıya nokta adını söylemesi bildirilir
                            print(ara_satir_cizgi)
                    else:
                        print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
                        point_name = input("Nokta Adı:")


                print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
                for i in range(1,6):
                    time.sleep(1)
                    print(f"{i}")


                for_x = ["x koordinatı", "x","x koordinat", "x değeri"]
                if for_x.count(command1):
                    for i in range(2):
                        print("X Koordinatını Söyleyiniz.Daha Doğru Bir Tanıma İçin Rakamları İkişer İkişer Söyleyebilirsiniz.")
                        print(ara_satir_cizgi)
                        listening_you_for_coordinat()
                        if command1 !="":
                            x_coordinate = float(str(command1))
                            print(f"X Koordinatı: {x_coordinate}")
                            break
                        else:
                            print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz\n X Koordinatını Söyleyiniz.\n")
                            print(ara_satir_cizgi)
                    else:
                        print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
                        for i in range(2):
                            try:
                                x_coordinate = float(input("X Koordinatını Klavye İle Tuşlayınız.Örnek:7894567.254\n:").replace(",", ","))
                                break
                            except ValueError as error:
                                print("Sayı Değeri Girilmelidir.İptal Etmek İçin 0'a Basınız.Devam Etmek İçin 0 Haricinde Bİr Tuşa Basmanız Yeterli.")
                                if input(":") =="0":
                                    break
                                else:
                                    pass


                print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
                for i in range(1,6):
                    time.sleep(1)
                    print(f"{i}")


                for_y = ["y koordinatı", "y","y koordinat", "y değeri"]
                if for_y.count(command1):
                    for i in range(2):
                        print("Y Koordinatını Söyleyiniz.Daha Doğru Bir Tanıma İçin Rakamları İkişer İkişer Söyleyebilirsiniz.")
                        print(ara_satir_cizgi)
                        listening_you_for_coordinat()
                        if command1 !="":
                            y_coordinate = float(str(command1))
                            print(f"Y Koordinatı: {y_coordinate}")
                            break
                        else:
                            print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz\n Y Koordinatını Söyleyiniz.\n")
                            print(ara_satir_cizgi)
                    else:
                        print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
                        for i in range(2):
                            try:
                                y_coordinate = float(input("Y Koordinatını Klavye İle Tuşlayınız.Örnek:7894567.254\n:").replace(",", ","))
                                break
                            except ValueError as error:
                                print("Sayı Değeri Girilmelidir.İptal Etmek İçin 0'a Basınız.Devam Etmek İçin 0 Haricinde Bİr Tuşa Basmanız Yeterli.")
                                if input(":") =="0":
                                    break
                                else:
                                    pass 


                print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
                for i in range(1,6):
                    time.sleep(1)
                    print(f"{i}")


                for_z= ["z koordinatı", "z","z koordinat", "z değeri"]
                if for_z.count(command1):
                    for i in range(2):
                        print("Z Koordinatını Söyleyiniz.Daha Doğru Bir Tanıma İçin Rakamları İkişer İkişer Söyleyebilirsiniz.")
                        print(ara_satir_cizgi)
                        listening_you_for_coordinat()
                        if command1 !="":
                            z_coordinate = float(str(command1))
                            print(f"Z Koordinatı: {z_coordinate}")
                            break
                        else:
                            print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz\n Z Koordinatını Söyleyiniz.\n")
                            print(ara_satir_cizgi)
                    else:
                        print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
                        for i in range(2):
                            try:
                                z_coordinate = float(input("Z Koordinatını Klavye İle Tuşlayınız.Örnek:7894567.254\n:").replace(",", ","))
                                break
                            except ValueError as error:
                                print("Sayı Değeri Girilmelidir.İptal Etmek İçin 0'a Basınız.Devam Etmek İçin 0 Haricinde Bİr Tuşa Basmanız Yeterli.")
                                if input(":") =="0":
                                    break
                                else:
                                    pass


                print("5 Saniye Sonra Sonraki Adıma Geçeceksiniz.")
                for i in range(1,6):
                    time.sleep(1)
                    print(f"{i}")


                for_crs = ["koordinat sistemi", "projeslyon sistmei", "epsg kodu", "koordinat"]
                if for_crs.count(command1):
                    for i in range(2):
                        print("Koordinat Sisteminin EPSG Kodunu Söyleyiniz.Daha Doğru Bir Tanıma İçin Rakamları İkişer İkişer, Teker Teker veya Sayının Kendisini Söyleyebilirsiniz.")
                        print(ara_satir_cizgi)
                        listening_you_for_coordinat()
                        if command1 !="":
                            coordinat_system = float(str(command1))
                            print(f"Koordinat Sistemi EPSG Kodu: {coordinat_system}")
                            break
                        else:
                            print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nKoordinat Sistemi EPSG Kodunu Söyleyiniz.\n:")
                            print(ara_satir_cizgi)
                    else:
                        print("Program Sesinizi Algılayamadı. Lütfen Klavye İle Giriş Yapınız.")
                        for i in range(2):
                            try:
                                coordinat_system = float(input("Koordinat Sistemi EPSG Kodunu Söyleyiniz. Örnek:2320\n:").replace(",", ","))
                                break
                            except ValueError as error:
                                print("Sayı Değeri Girilmelidir.İptal Etmek İçin 0'a Basınız.Devam Etmek İçin 0 Haricinde Bİr Tuşa Basmanız Yeterli.")
                                if input(":") =="0":
                                    break
                                else:
                                    pass

create_point_with_voice_tr()