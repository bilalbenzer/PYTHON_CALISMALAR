from shapely.geometry import Point,MultiPoint
import geopandas
class ayarlar():
    def __init__(self,sesli_komut_acik_kapali):
        self.sesli_komut = sesli_komut_acik_kapali
import speech_recognition
import pyttsx3
class kayit_olustur(ayarlar):
    def __init__(self,ayarlar):
        print(ayarlar.sesli_komut)
        if ayarlar.sesli_komut == "Açık":
            self.ses_tanima_acik_kapali = "Açık"
            print("Sesli Tanıma Açıldı")
        else:
            self.ses_tanima_acik_kapali = "Kapalı"
            print("Sesli Tanıma Kapatıldı.")
        
    def kayit(self):
        if self.ses_tanima_acik_kapali =="Açık":
            with speech_recognition.Microphone() as source:
                self.r = speech_recognition.Recognizer()
                print("Şuan sizi dinliyorum.(5 saniye boyunca..)")
                self.audio_data = self.r.record(source,duration=2)
                self.text = str(self.r.recognize_google(self.audio_data,language="tr-TR")).lower()
        else:
            print("Sesli Tanıma Kapalı")

        
class point_olustur():
    geometry_type=None  #geometri tipi için sınıfa ait bir özellik
    def __init__(self,point_name=None,x_koordinati=None,y_koordinati=None,z_koordinati=None,crs_kod_epsg="4326",geometry=None):    #gelen değişkene atamak için örnek nitelikleri
        if point_name==None:
            self.name = ''
        else:
            self.name = str(point_name)  #gelen değişkenin ismi
        if x_koordinati==None:
            self.x=None
        else:
            try:      #x koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
                self.x = float(x_koordinati)   #gelen değişkenin x koordinatı
                pass
            except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
                print("X Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
                self.x = None   #hatalı girişten dolayı x koordinatına none değeri atıyoruz
                pass
        if y_koordinati==None:
            self.y=None
        else:
            try:      #y koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
                self.y = float(y_koordinati)   #gelen değişkenin y koordinatı
                pass
            except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
                print("Y Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
                self.y = None   #hatalı girişten dolayı y koordinatına none değeri atıyoruz
                pass
        if z_koordinati==None:
            self.z=None
            self.geometry_type = "Point"
        else:
            try:      #z koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
                self.z = float(z_koordinati)   #gelen değişkenin z koordinatı
                self.geometry_type = "Point Z"
                pass
            except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
                print("Z Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
                self.z = None   #hatalı girişten dolayı z koordinatına none değeri atıyoruz
                self.geometry_type = "Point"
                pass
        if crs_kod_epsg=='':
            print("Koordinat sistemi EPSG kodu girmediniz. Varsayılan olarak WGS84 koordinat sistemi tanımlandı.")
            self.crs_system="4326"
            pass
             #koordinat sistemi epsg kodu sayısal bir değer olmalı. bunun için try except yapıyoruz
        else:
            try:
                self.crs_system = int(crs_kod_epsg)  #gelen değşikenin epsg kodu
                pass
            except ValueError:  #koordinat bilgisi, sayısal olmayan bir değer gelirse WGS84 değeri verilecek
                print("Koordinat sistemi EPSG kodu yanlış girildi. Değeri tekrar atamanız gerekmektedir.")
                self.crs_system = "4326"  #hatalı girişten dolayı koordinat sistemi 4326 olarak değişecek
                pass
        # geometri objesi, x,y ve z değerlerinden oluşur. Bunlardan herhangi birinin hatalı girilemsi durumunda point objesi oluşamaz. Bunun için try except bloğu kullanacağız
        if type(self.x)==float and type(self.y)==float:
            if type(self.z) == float:
                self.geometry = Point([self.x,self.y,self.z])
            else:
                self.geometry = Point([self.x,self.y])
        else:
            self.geometry = None
        self.oznitelik_ekleme()
        self.database_olusturma()
        self.show_in_map()
    def oznitelik_ekleme(self,oznitelik=dict):   #geometriye ait öznitelik bilgileri bu kısımda saklanabilir
        self.attibuties = {"AD":[self.name],"TIP":[self.geometry_type],"X":[self.x],"Y":[self.y],"Z":[self.z],"geometry":[self.geometry]}    #ilk olarak dict tipinde bir değişkenimiz olmalı. bu sözlüğe varsayılan kolonları ekliyoruz.
        try:    
            for i,c in oznitelik.items():   #kullanıcının verdiği bilgileri for döngüsü ile dict verimizie veriyoruz.
                self.attibuties.update({i:[c]})
            else:
                pass
        except:
            print("Point özniteliklerine varsayılan değerler atandı.")
    def database_olusturma(self):
        try:
            self.database = geopandas.GeoDataFrame(self.attibuties,crs=self.crs_system)
        except AttributeError as hata:
            print(f"Hata Metni:{hata}\nVeritabanı oluşturmak için, öznitelik bilgilerini oluşturmanız gerekmektedir.")
    def shape_file_olusturma(self,konum=r"dosya.shp"):
        print(r"varsayılan konum ayarlıdır.Konum bilgisi girilemzse eğer programın kurulu olduğu klasöre dosya.shp olarak kaydedilecektir.")
        import fiona
        if konum == r"dosya.shp":
            pass
        else:
            konum = input(":")
        self.konum = r"{}".format(konum)
        try:
            self.database.to_file(self.konum)
        except AttributeError as hata:
            print(f"Hata Metni:{hata}\nShapefile dosyası oluşturmak için, veritabanı oluşturmanız gerekmektedir.")
        except fiona.errors.DriverIOError or fiona.errors.DriverError :
            print("Dosya yolu yanlış belirtildi.")
    def show_in_map(self):
        self.a =self.database.plot()

class coklu_point_olustur(point_olustur):
    geometry_type = "Multi Point"
    point_sayisi = 0
    def __init__(self,point_olustur):
        self.point_sayisi = 1
        self.multi_point = {self.point_sayisi:[point_olustur.name,point_olustur.geometry_type,point_olustur.x,point_olustur.y,point_olustur.z,point_olustur.crs_system,point_olustur.attibuties,point_olustur.database]} 
    def update_point(self,point_olustur):
        self.point_sayisi+=1
        self.multi_point.update({self.point_sayisi:[point_olustur.name,point_olustur.geometry_type,point_olustur.x,point_olustur.y,point_olustur.z,point_olustur.crs_system,point_olustur.attibuties,point_olustur.database,]})
        return self.multi_point
    def cikti_ekrani(self):
        a = 0
        for x,y in self.multi_point.items():
            a+=1
            print(f"""{x}. Nokta:
Nokta Adı:          {y[0]}
Geometri Tipi:      {y[1]}
X Koordinatı:       {y[2]}
Y Koordinatı:       {y[3]}
Z Koordinatı:       {y[4]}
Koordinat Sistemi:  {y[5]}
Öznitelik Bilgileri:{y[6]}
""")
    
point1 = point_olustur(point_name="nokta1",x_koordinati=123,y_koordinati=345,z_koordinati=5,crs_kod_epsg="4326")
point2 = point_olustur(point_name="nokta2",x_koordinati=435,y_koordinati=5345,z_koordinati=5,crs_kod_epsg="4326")
coklu_nokta = coklu_point_olustur(point1)

coklu_nokta.update_point(point2)

coklu_nokta.cikti_ekrani()

        

        
    
