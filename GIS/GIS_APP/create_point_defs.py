from shapely.geometry import Point   #gerekli kütüphane
from my_classes import create_point , create_multi_point , settings , listen_to_voice_command
ara_satir_cizgi = "\n------------------------------------------------------------------------------------------------------------------------------------\n"

def listening_you():
            a = settings("Open")
            b = listen_to_voice_command(a)
            b.listen_tr()
            global command1
            command1 = b.text

def create_point_with_voice_tr():
    while True:
        print("Nokta Adını Söyleyiniz.")    #sesli tanıma başlamadan önce kullanıcıya nokta adını söylemesi bildirilir
        print(ara_satir_cizgi)
        donus1 = ""
        listening_you() #ses tanıma başlar
        if command1 !="":    #
            point_name = str(command1)
        else:
            print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz.")    #sesli tanıma başlamadan önce kullanıcıya nokta adını söylemesi bildirilir
            print(ara_satir_cizgi)
            listening_you() #ses tanıma başlar
            if command1 !="":
                print(f"Nokta Adı: {command1}")
                point_name = str(command1)
            else:
                print("Sesinizi yine algılayamadım. Nokta adı:Nokta olarak girildi. Daha Sonra Düzenleyebilirsiniz.")
                print(ara_satir_cizgi)
                print(f"Nokta Adı: {point_name}")
                point_name="Nokta"
        try:
            print("X Koordinatını Söyleyiniz.Lütfen koordinat bilgisindeki rakamları teker teker söyleyiniz.")
            print(ara_satir_cizgi)
            listening_you()
            if command1 !="":
                str(command1.replace(" ", ""))
                x_coordinate = float(str(command1).replace(",", "."))
                print(f"X Koordinatı: {x_coordinate}")
            else:
                print("Sesinizi Algılayamadım. Tekrar Deneyiniz.\nNokta Adını Söyleyiniz\n X Koordinatını Söyleyiniz.")
                print(ara_satir_cizgi)
                listening_you()
                if command1 !="":
                    x_coordinate = float(str(command1).replace(",", "."))
                    print(f"X Koordinatı: {x_coordinate}")
                else:
                    print("Sesizini yine algılayamadım. X Koordinatı:0 olarak girildi. Daha Sonra Düzenleyebilirsiniz.")
                    x_coordinate = 0
                    print(f"X Koordinatı: {x_coordinate}")
        except ValueError as error:
            print(f"Hata Metni:{error}\nX koordinatı sayı olmalıdır.")
            return x_coordinate
        try:
            print("Y Koordinatını Söyleyiniz.")
            listening_you()
            y_coordinate = float(str(command1).replace(",", "."))
        except ValueError as error:
            print(f"Hata Metni:{error}\nX koordinatı sayı olmalıdır.")
            return y_coordinate 
        try:
            print("Z Koordinatını Söyleyiniz.")
            listening_you()
            z_coordinate = float(str(command1).replace(",", "."))
        except ValueError as error:
            print(f"Hata Metni:{error}\nX koordinatı sayı olmalıdır.")
            return z_coordinate
        print("Koordinat Sistemini Boş Bırakırsanız Veya Yanlış Girerseniz 4326 EPSG Kodu Varsayılan Olarak Atanacak.\n Koordinat Sistemini Söyleyiniz.") 
        listening_you()
        coordinat_system = (str(command1))

        print(f"""Girilen Değerler Aşağıdaki Gibidir.
Nokta Adı:              {point_name}
X Koordinatı:           {x_coordinate}
Y Koordinatı:           {y_coordinate}
Z Koordinatı:           {z_coordinate}
Koordinat Sistmei:      {coordinat_system}
""")
        print("Girilen Bilgiler Doğru İse 1, Yanlış İse 2 Cevabını Veriniz.\n:")
        listening_you()
        true_false = str(command1)
        if true_false=="1":
            print("Girdiğiniz Değer İle Nokta Objesi Oluşturuluyor. Lütfen Bekleyin...")
            a = create_point(point_name=point_name,x_coordinate=x_coordinate,y_coordinate=y_coordinate,z_coordinate=z_coordinate,crs_kod_epsg=coordinat_system)
            print(a.attribute)

listening_you()