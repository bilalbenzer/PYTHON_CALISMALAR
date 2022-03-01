from shapely.geometry import Point,MultiPoint
import geopandas
class settings():
    def __init__(self,voice_command_open_close):
        self.voice_command = voice_command_open_close
import speech_recognition
import pyttsx3
class listen_to_voice_command(settings):
    def __init__(self,settings):
        print(settings.voice_command)
        if settings.voice_command == "Open":
            self.voice_command = "Open"
            print("voice command turned on")
        else:
            self.voice_command = "Close"
            print("voice command turned on")
        
    def listen(self):
        if self.voice_command =="Open":
            with speech_recognition.Microphone() as source:
                self.r = speech_recognition.Recognizer()
                print("Şuan sizi dinliyorum.(5 saniye boyunca..)\nI'm listening to you right now (for 5 seconds..)")
                self.audio_data = self.r.record(source,duration=2)
                self.text = str(self.r.recognize_google(self.audio_data,language="tr-TR")).lower()
        else:
            print("voice command turned on")
        
class create_point():
    geometry_type=None  #geometri tipi için sınıfa ait bir özellik
    def __init__(self,point_name=None,x_coordinate=None,y_coordinate=None,z_coordinate=None,crs_kod_epsg="4326",geometry=None):    #gelen değişkene atamak için örnek nitelikleri
        if point_name==None:
            self.name = ''
        else:
            self.name = str(point_name)  #gelen değişkenin ismi
        if x_coordinate==None:
            self.x=None
        else:
            try:      #x koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
                self.x = float(x_coordinate)   #gelen değişkenin x koordinatı
                pass
            except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
                print("X Koordinatı yanlış girildi. Değeri tekrar atamanız gerekmektedir.\nThe X Coordinate was entered incorrectly. You need to reassign the value.")
                self.x = None   #hatalı girişten dolayı x koordinatına none değeri atıyoruz
                pass
        if y_coordinate==None:
            self.y=None
        else:
            try:      #y koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
                self.y = float(y_coordinate)   #gelen değişkenin y koordinatı
                pass
            except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
                print("Y Koordinatı yanlış girildi. Değeri tekrar atamanız gerekmektedir.\nThe Y Coordinate was entered incorrectly. You need to reassign the value.")
                self.y = None   #hatalı girişten dolayı y koordinatına none değeri atıyoruz
                pass
        if z_coordinate==None:
            self.z=None
            self.geometry_type = "Point"
        else:
            try:      #z koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
                self.z = float(z_coordinate)   #gelen değişkenin z koordinatı
                self.geometry_type = "Point Z"
                pass
            except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
                print("Z Koordinatı yanlış girildi. Değeri tekrar atamanız gerekmektedir.\nThe Z Coordinate was entered incorrectly. You need to reassign the value.")
                self.z = None   #hatalı girişten dolayı z koordinatına none değeri atıyoruz
                self.geometry_type = "Point"
                pass
        if crs_kod_epsg=='':
            print("Koordinat sistemi EPSG kodu girmediniz. Varsayılan olarak WGS84 koordinat sistemi tanımlandı.\nYou have not entered a coordinate system EPSG code. WGS84 coordinate system is defined by default.")
            self.crs_system="4326"
            pass
             #koordinat sistemi epsg kodu sayısal bir değer olmalı. bunun için try except yapıyoruz
        else:
            try:
                self.crs_system = int(crs_kod_epsg)  #gelen değşikenin epsg kodu
                pass
            except ValueError:  #koordinat bilgisi, sayısal olmayan bir değer gelirse WGS84 değeri verilecek
                print("Koordinat sistemi EPSG kodu yanlış girildi. Değeri tekrar atamanız gerekmektedir.\nCoordinate system EPSG code was entered incorrectly. You need to reassign the value.")
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
        self.add_attribute()
        self.create_GeoDataFrame()
        self.show_in_map()
    def add_attribute(self,attribute=dict):   #geometriye ait öznitelik bilgileri bu kısımda saklanabilir
        self.attribute = {"AD/NAME":[self.name],"TIP/TYPE":[self.geometry_type],"X":[self.x],"Y":[self.y],"Z":[self.z],"geometry":[self.geometry]}    #ilk olarak dict tipinde bir değişkenimiz olmalı. bu sözlüğe varsayılan kolonları ekliyoruz.
        try:    
            for i,c in attribute.items():   #kullanıcının verdiği bilgileri for döngüsü ile dict verimizie veriyoruz.
                self.attribute.update({i:[c]})
            else:
                pass
        except:
            print("Point özniteliklerine varsayılan değerler atandı.\nPoint attributes are assigned default values.")
    def create_GeoDataFrame(self):
        try:
            self.geo_data_frame = geopandas.GeoDataFrame(self.attribute,crs=self.crs_system)
        except AttributeError as error:
            print(f"Hata Metni/Error Text:{error}\nVeritabanı oluşturmak için, öznitelik bilgilerini oluşturmanız gerekmektedir.\nTo create a database, you must create an attribute.\n")
    def create_shape_file(self,location=r"file.shp"):
        print(r"varsayılan konum ayarlıdır.Konum bilgisi girilemzse eğer programın kurulu olduğu klasöre dosya.shp olarak kaydedilecektir.\nThe default location is set. If the location information is not entered, it will be saved as file.shp in the folder where the program is installed.")
        import fiona
        if location == r"file.shp":
            pass
        else:
            location = input(":")
        self.save_location = r"{}".format(location)
        try:
            self.geo_data_frame.to_file(self.save_location)
        except AttributeError as error:
            print(f"Hata Metni/Error Text:{error}\nShapefile dosyası oluşturmak için, veritabanı oluşturmanız gerekmektedir.\nTo create a shapefile file, you need to create a database")
        except fiona.errors.DriverIOError or fiona.errors.DriverError :
            print("Dosya yolu yanlış belirtildi.\nThe file path was specified incorrectly.")
    def show_in_map(self):
        self.a =self.geo_data_frame.plot()

class create_multi_point(create_point):
    geometry_type = "Multi Point"
    number_of_point = 0
    def __init__(self,create_point):
        self.number_of_point = 1
        self.multi_point_dict= {self.number_of_point:[create_point.name,create_point.geometry_type,create_point.x,create_point.y,create_point.z,create_point.crs_system,create_point.attribute,create_point.geo_data_frame]} 
    def add_point(self,create_point):
        self.number_of_point+=1
        self.multi_point_dict.update({self.number_of_point:[create_point.name,create_point.geometry_type,create_point.x,create_point.y,create_point.z,create_point.crs_system,create_point.attribute,create_point.geo_data_frame]})
        return self.multi_point_dict
    def output_multi_point(self):
        a = 0
        for x,y in self.multi_point_dict.items():
            a+=1
            print(f"""{x}. Nokta/Point:
_________________________________________________________________
-    Nokta Adı / Point Name:-------------------------{y[0]}      
-    Geometri Tipi / Geometry Type:------------------{y[1]}      
-    X :---------------------------------------------{y[2]}      
-    Y :---------------------------------------------{y[3]}      
-    Z :---------------------------------------------{y[4]}      
-    Koordinat Sistemi / Coordinate System:----------{y[5]}      
-    Öznitelik Bilgileri / Attribute Informations:---{y[6]}      
__________________________________________________________________
""")