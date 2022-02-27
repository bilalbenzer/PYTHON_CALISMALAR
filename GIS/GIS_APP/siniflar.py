from shapely.geometry import Point

class point2d():
    geometry_type="Point "  #geometri tipi için sınıfa ait bir özellik
    def __init__(self,point_name=str(),x_koordinati=float(),y_koordinati=float(),crs_kod_epsg="4326"):    #gelen değişkene atamak için örnek nitelikleri
        self.name = str(point_name)  #gelen değişkenin ismi
        try:      #x koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
            self.x = float(x_koordinati)   #gelen değişkenin x koordinatı
        except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
            print("X Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
            self.x = None   #hatalı girişten dolayı x koordinatına none değeri atıyoruz
        try:    #y koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
            self.y = float(y_koordinati)     #gelen değişkenin y koordinatı
        except ValueError:   #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
            print("Y Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
            self.y = None     #hatalı girişten dolayı y koordinatına none değeri atıyoruz
           
        if crs_kod_epsg=='':
            print("Koordinat sistemi EPSG kodu girmediniz. Varsayılan olarak WGS84 koordinat sistemi tanımlandı.")
            self.crs_system="4326"
             #koordinat sistemi epsg kodu sayısal bir değer olmalı. bunun için try except yapıyoruz
        else:
            try:
                self.crs_system = int(crs_kod_epsg)  #gelen değşikenin epsg kodu
            except ValueError:  #koordinat bilgisi, sayısal olmayan bir değer gelirse WGS84 değeri verilecek
                print("Koordinat sistemi EPSG kodu yanlış girildi. Değeri tekrar atamanız gerekmektedir.")
                self.crs_system = "4326"  #hatalı girişten dolayı koordinat sistemi 4326 olarak değişecek
        # geometri objesi, x,y ve z değerlerinden oluşur. Bunlardan herhangi birinin hatalı girilemsi durumunda point objesi oluşamaz. Bunun için try except bloğu kullanacağız
        try:   
            if (self.x == None) or (self.y == None):    #point objesi temelde x ve y den oluşur. x veya yden birisi yanlış verilirse eğer obje none olarak değişr
                self.geometry = None
            else:   #x ve y doğru ise bu sefer z değerinin sorgusu yapılır
                self.geometry = Point(self.x,self.y)    #gelen değişkenin geometri objesi
        except :    #herhangi bir hata olması durumunda geomtry objesi none değere dönüşür.
            self.geometry = None    #gelen değişkenin geometri objesi   
            return
    def oznitelik_ekleme(self,oznitelik=dict()):   #geometriye ait öznitelik bilgileri bu kısımda saklanabilir
        self.attibuties = {"AD":[self.name],"TIP":["Point"],"X":[self.x],"Y":[self.y],"geometry":[self.geometry]}    #ilk olarak dict tipinde bir değişkenimiz olmalı. bu sözlüğe varsayılan kolonları ekliyoruz.
        for i,c in oznitelik.items():   #kullanıcının verdiği bilgileri for döngüsü ile dict verimizie veriyoruz.
            self.attibuties.update({i:[c]})
    def database_olusturma(self):
        import geopandas
        try:
            self.database = geopandas.GeoDataFrame(self.attibuties,crs=self.crs_system)
            print(self.database)
        except AttributeError as hata:
            print(f"Hata Metni:{hata}\nVeritabanı oluşturmak için, öznitelik bilgilerini oluşturmanız gerekmektedir.")
    def shape_file_olusturma(self,konum=r"dosya.shp"):
        import geopandas as gpd
        import fiona as fio
        self.konum = r"{}".format(konum)
        try:
            self.database.to_file(self.konum)
        except AttributeError as hata:
            print(f"Hata Metni:{hata}\nShapefile dosyası oluşturmak için, veritabanı oluşturmanız gerekmektedir.")

class point3d():
    geometry_type="Point Z"  #geometri tipi için sınıfa ait bir özellik
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
        else:
            try:      #z koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz
                self.z = float(z_koordinati)   #gelen değişkenin z koordinatı
                pass
            except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
                print("Z Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
                self.z = None   #hatalı girişten dolayı z koordinatına none değeri atıyoruz
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
    def oznitelik_ekleme(self,oznitelik=dict):   #geometriye ait öznitelik bilgileri bu kısımda saklanabilir
        self.attibuties = {"AD":[self.name],"TIP":["Point"],"X":[self.x],"Y":[self.y],"Z":[self.z],"geometry":[self.geometry]}    #ilk olarak dict tipinde bir değişkenimiz olmalı. bu sözlüğe varsayılan kolonları ekliyoruz.
        try:    
            for i,c in oznitelik.items():   #kullanıcının verdiği bilgileri for döngüsü ile dict verimizie veriyoruz.
                self.attibuties.update({i:[c]})
            else:
                pass
        except:
            print("Point özniteliklerine varsayılan değerler atandı.")
    def database_olusturma(self):
        import geopandas
        self.oznitelik_ekleme()
        try:
            self.database = geopandas.GeoDataFrame(self.attibuties,crs=self.crs_system)
        except AttributeError as hata:
            print(f"Hata Metni:{hata}\nVeritabanı oluşturmak için, öznitelik bilgilerini oluşturmanız gerekmektedir.")
    def shape_file_olusturma(self,konum="Konum giriniz."):
        import geopandas as gpd
        import fiona as fio
        konum = input(r"Dosya Konumunu Giriniz. Örnek: C:\Users\...\dosyaadi.shp")
        self.database_olusturma()
        self.konum = r"{}".format(konum)
        try:
            self.database.to_file(self.konum)
        except AttributeError as hata:
            print(f"Hata Metni:{hata}\nShapefile dosyası oluşturmak için, veritabanı oluşturmanız gerekmektedir.")
    def show_in_map(self):
        import geopandas
        self.database_olusturma()
        print(self.database.plot())

a=point3d(point_name="asd",x_koordinati=3123,y_koordinati=5456,crs_kod_epsg=4326)

print(a.show_in_map())
