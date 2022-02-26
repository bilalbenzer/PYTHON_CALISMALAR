from shapely.geometry import Point

class point2d():
    geometry_type="Point "  #geometri tipi için sınıfa ait bir özellik
    def __init__(self,point_name,x_koordinati,y_koordinati,crs_kod_epsg):    #gelen değişkene atamak için örnek nitelikleri
        self.name = point_name  #gelen değişkenin ismi
        self.x = x_koordinati   #gelen değişkenin x koordinatı
        self.y = y_koordinati   #gelen değişkenin y koordinatı
        try:
            self.crs_system = float(crs_kod_epsg)  #gelen değşikenin epsg kodu
        except ValueError:
            print("EPSG kodu yanlış formatta girildi. Sayısal bir değer giriniz.")
            pass
        self.geometry = Point(x_koordinati,y_koordinati)    #gelen değişkenin geometri objesi
    def oznitelik_ekleme(self,oznitelik):
        self.attibuties = dict()
        for i,c in oznitelik.items():
            self.attibuties.update({i:c})

class point3d():
    geometry_type="Point Z"  #geometri tipi için sınıfa ait bir özellik
    def __init__(self,point_name=str(),x_koordinati=float(),y_koordinati=float(),z_koordinati=float(),crs_kod_epsg=float()):    #gelen değişkene atamak için örnek nitelikleri
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
        try:    #z koordinatı sayısal bir değer olmalı. bunun için try except yapıyoruz        
            self.z = float(z_koordinati)   #gelen değişkenin z koordinatı
        except ValueError:  #kullanıcı, str bir değer verirse eğer, uyarı verilecek ve tekrar girmesi istenecek
            print("Z Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
            self.z = None   #hatalı girişten dolayı z koordinatına none değeri atıyoruz
        try:    #koordinat sistemi epsg kodu sayısal bir değer olmalı. bunun için try except yapıyoruz
            self.crs_system = float(crs_kod_epsg)  #gelen değşikenin epsg kodu
        except ValueError:  #koordinat bilgisi, sayısal olmayan bir değer gelirse none değeri verilecek
            print("Koordinat sistemi EPSG kodu yanlış girildi. Değeri tekrar atamanız gerekmektedir.")
            self.crs_system = None  #hatalı girişten dolayı koordinat sistemi none olarak değişecek
        # geometri objesi, x,y ve z değerlerinden oluşur. Bunlardan herhangi birinin hatalı girilemsi durumunda point objesi oluşamaz. Bunun için try except bloğu kullanacağız
        try:   
            if (self.x == None) or (self.y == None):    #point objesi temelde x ve y den oluşur. z değeri isteğe bağlıdır. x veya yden birisi yanlış verilirse eğer obje none olarak değişr
                self.geometry = None
            else:   #x ve y doğru ise bu sefer z değerinin sorgusu yapılır
                if self.z == None:  #z değeri yanlış girilmiş ve none değerini almış ise, geometri objesine z değeri dahil edilmez.
                    self.geometry = Point(self.x,self.y)    #gelen değişkenin geometri objesi
                elif self.z ==float():  #z değerinde sorun yoksa eğer geometri objesine dahil edilir.
                    self.geometry = Point(self.x,self.y,self.z)
        except :    #herhangi bir hata olması durumunda geomtry objesi none değere dönüşür.
            self.geometry = None    #gelen değişkenin geometri objesi   
            return
    def oznitelik_ekleme(self,oznitelik=dict()):   #geometriye ait öznitelik bilgileri bu kısımda saklanabilir
        self.attibuties = {"AD":self.name,"TIP":"Point","X":self.x,"Y":self.y,"Z":self.z}    #ilk olarak dict tipinde bir değişkenimiz olmalı. bu sözlüğe varsayılan kolonları ekliyoruz.
        for i,c in oznitelik.items():   #kullanıcının verdiği bilgileri for döngüsü ile dict verimizie veriyoruz.
            self.attibuties.update({i:c})

