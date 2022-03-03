from shapely.geometry import Point   #gerekli kütüphane
from my_classes import create_point , create_multi_point , settings , listen_to_voice_command
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
        for i in range(2):
            print("X Koordinatını Söyleyiniz.Daha Doğru Bir Tanıma İçin Rakamları Teker Teker Söyleyebilirsiniz.")
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
    
create_point_with_voice_tr()