from shapely.geometry import Point,MultiPoint
import geopandas

ara_satir_cizgi = "\n------------------------------------------------------------------------------------------------------------------------------------\n"

class settings():
    def __init__(self,voice_command_open_close):
        self.voice_command = voice_command_open_close
import speech_recognition
import pyttsx3
class listen_to_voice_command(settings):
    def __init__(self,settings,language_choice=None):
        self.language_choice = language_choice
        if settings.voice_command == "Open":
            self.voice_command = "Open"
            if language_choice=="tr":
                print("Sesli komut açıldı.")
            elif language_choice=="en":
                print("Voice command turned on")
            print(ara_satir_cizgi)
        else:
            self.voice_command = "Close"
            if self.language_choice=="tr":
                print("Sesli komut kapatıldı.")
            elif self.language_choice=="en":
                print("Voice command turned off")
            print(ara_satir_cizgi)

    def listen_tr(self):
        if self.voice_command =="Open":
            with speech_recognition.Microphone() as source:
                try:
                    self.r = speech_recognition.Recognizer()
                    print("Şuan sizi dinliyorum.(3 saniye boyunca..)")
                    print(ara_satir_cizgi)
                    self.audio_data = self.r.record(source,duration=3)
                    self.text = str(self.r.recognize_google(self.audio_data,language="tr-TR")).lower()
                    print("Cevap:",self.text)
                except speech_recognition.UnknownValueError as error:
                    print("Hata Metni",error)
                    print("Sizi anlayamadım.")
                    print(ara_satir_cizgi)
                    self.text = ""
                    print(self.text)
        else:
            if self.language_choice=="tr":
                print("Sesli komut kapatıldı.")
            elif self.language_choice=="en":
                print("Voice command turned açıldı")
            print(ara_satir_cizgi)
    def listen_tr_coordinate(self):
        if self.voice_command =="Open":
            with speech_recognition.Microphone() as source:
                try:
                    self.r = speech_recognition.Recognizer()
                    print("Şuan sizi dinliyorum.(5 saniye boyunca..)")
                    print(ara_satir_cizgi)
                    self.audio_data = self.r.record(source,duration=8)
                    self.text = str(self.r.recognize_google(self.audio_data,language="tr-TR")).lower()
                    print(self.text)
                    self.coordinate = str()
                    self.text = (self.text).replace("nokta", ".")
                    self.text = (self.text).replace("virgül", ".")
                    self.text = (self.text).replace(",", ".")
                    liste1 = [".",",","1","2","3","4","5","6","7","8","9","0"]
                    print(self.text)
                    for i in str(self.text):
                        try:
                            if liste1.count(i):
                                self.coordinate+=str(i)
                            else:
                                pass
                        except ValueError:
                            pass
                    else:   
                        print(self.coordinate)
                except speech_recognition.UnknownValueError as error:
                    print("Hata Metni",error)
                    print("Sizi anlayamadım.")
                    print(ara_satir_cizgi)
                    self.text = ""
                    print(self.text)
        else:
            if self.language_choice=="tr":
                print("Sesli komut kapatıldı.")
            elif self.language_choice=="en":
                print("Voice command turned açıldı")
            print(ara_satir_cizgi)
    def listen_en(self):
        if self.voice_command =="Open":
            with speech_recognition.Microphone() as source:
                try:
                    self.r = speech_recognition.Recognizer()
                    print("I'm listening to you right now (for 5 seconds..)")
                    print(ara_satir_cizgi)
                    self.audio_data = self.r.record(source,duration=2)
                    self.text = str(self.r.recognize_google(self.audio_data,language="en-US")).lower()
                except speech_recognition.UnknownValueError as error:
                    print("Text Error",error)
                    print("I couldn't understand you. Please continue by typing with the keyboard")
                    print(ara_satir_cizgi)
        else:
            if self.language_choice=="tr":
                print("Sesli komut kapatıldı.")
            elif self.language_choice=="en":
                print("Voice command turned açıldı")
            print(ara_satir_cizgi)
        
class create_point():
    geometry_type=None  #geometri tipi için sınıfa ait bir özellik
    def with_keyboard(self,point_name=input("Nokta Adını Giriniz.\n:"),x_coordinate=input("X Koordinatını Giriniz. \n"),y_coordinate=input("Y Koordinatını Giriniz. \n:"),
    z_coordinate=input("Z Koordinatını Giriniz.\n:"),crs_kod_epsg=input("Koordinat Sistemi EPSG Kodunu Giriniz.\n:"),geometry=None):    #gelen değişkene atamak için örnek nitelikleri
        if point_name==None:
            self.name = "Point"
        else:
            self.name = str(point_name)  #gelen değişkenin ismi

        try:      #x koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
            self.x = float(x_coordinate)   #gelen değişkenin x koordinatı
            pass
        except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
            print("X Koordinatı yanlış girildiği için 0 değeri verildi. Değeri tekrar atamanız gerekmektedir.\nThe X Coordinate was entered incorrectly. You need to reassign the value.")
            print(ara_satir_cizgi)
            self.x = 0   #hatalı girişten dolayı x koordinatına none değeri atıyoruz
            pass

        try:      #y koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
            self.y = float(y_coordinate)   #gelen değişkenin y koordinatı
            pass
        except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
            print("Y Koordinatı yanlış girildiği için 0 değeri verildi. Değeri tekrar atamanız gerekmektedir.\nThe Y Coordinate was entered incorrectly. You need to reassign the value.")
            print(ara_satir_cizgi)
            self.y = 0   #hatalı girişten dolayı y koordinatına none değeri atıyoruz
            pass

        try:      #z koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
            self.z = float(z_coordinate)   #gelen değişkenin z koordinatı
            self.geometry_type = "Point Z"
            pass
        except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
            print("Z Koordinatı yanlış girildiği için 0 değeri verildi. Değeri tekrar atamanız gerekmektedir.\nThe Z Coordinate was entered incorrectly. You need to reassign the value.")
            print(ara_satir_cizgi)
            self.z = 0   #hatalı girişten dolayı z koordinatına none değeri atıyoruz
            self.geometry_type = "Point"
            pass
        if crs_kod_epsg=='':
            print("Koordinat sistemi EPSG kodu girmediniz. Varsayılan olarak WGS84(EPSG:4326) koordinat sistemi tanımlandı.\nYou have not entered a coordinate system EPSG code. WGS84 coordinate system is defined by default.")
            print(ara_satir_cizgi)
            self.crs_system="EPSG:4326"
            pass
             #koordinat sistemi epsg kodu sayısal bir değer olmalı. bunun için try except yapıyoruz
        else:
            try:
                self.crs_system = "EPSG:"+str(int(crs_kod_epsg))  #gelen değşikenin epsg kodu
                pass
            except ValueError:  #koordinat bilgisi, sayısal olmayan bir değer gelirse WGS84 değeri verilecek
                print("Koordinat sistemi EPSG kodu yanlış girildiği için WGS84(EPSG:4326) değeri atandı. Değeri tekrar atamanız gerekmektedir.\nCoordinate system EPSG code was entered incorrectly. You need to reassign the value.")
                print(ara_satir_cizgi)
                self.crs_system = "EPSG:4326"  #hatalı girişten dolayı koordinat sistemi 4326 olarak değişecek
                pass
        # geometri objesi, x,y ve z değerlerinden oluşur. Bunlardan herhangi birinin hatalı girilemsi durumunda point objesi oluşamaz. Bunun için try except bloğu kullanacağız
        if type(self.x)==float and type(self.y)==float:
            if type(self.z) == float:
                self.geometry = Point([self.x,self.y,self.z])
            else:
                self.geometry = Point([self.x,self.y])
        else:
            self.geometry = Point([self.x,self.y])
        self.add_attribute()
        print(f"""
_________________________________________________________________
-    Nokta Adı / Point Name:-------------------------{self.name}      
-    Geometri Tipi / Geometry Type:------------------{self.geometry_type}      
-    X :---------------------------------------------{self.x}      
-    Y :---------------------------------------------{self.y}      
-    Z :---------------------------------------------{self.z}      
-    Koordinat Sistemi / Coordinate System:----------{self.crs_system}      
-    Öznitelik Bilgileri / Attribute Informations:---{self.attribute}      
__________________________________________________________________
""")
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
            print(ara_satir_cizgi)
    def create_GeoDataFrame(self):
        try:
            self.geo_data_frame = geopandas.GeoDataFrame(self.attribute,crs=self.crs_system)
        except AttributeError as error:
            print(f"Hata Metni/Error Text:{error}\nVeritabanı oluşturmak için, öznitelik bilgilerini oluşturmanız gerekmektedir.\nTo create a database, you must create an attribute.\n")
            print(ara_satir_cizgi)
    def create_shape_file(self,location=r"file.shp"):
        print(r"varsayılan konum ayarlıdır.Konum bilgisi girilemzse eğer programın kurulu olduğu klasöre dosya.shp olarak kaydedilecektir.\nThe default location is set. If the location information is not entered, it will be saved as file.shp in the folder where the program is installed.")
        print(ara_satir_cizgi)
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
            print(ara_satir_cizgi)
        except fiona.errors.DriverIOError or fiona.errors.DriverError :
            print("Dosya yolu yanlış belirtildi.\nThe file path was specified incorrectly.")
            print(ara_satir_cizgi)
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
            print(ara_satir_cizgi)


