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
        try:      
            self.x = float(x_koordinati)   #gelen değişkenin x koordinatı
        except ValueError:
            print("X Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
            self.x = None   #gelen değişkenin x koordinatı
        try:
            self.y = float(y_koordinati)     #gelen değişkenin y koordinatı
        except ValueError:
            print("Y Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
            self.y = None     #gelen değişkenin y koordinatı
        try:            
            self.z = float(z_koordinati)   #gelen değişkenin z koordinatı
        except ValueError:
            print("Z Koordinatı yanlış girildi. Değeri tekrar atamnız gerekmektedir.")
            self.z = None   #gelen değişkenin z koordinatı
        try:
            self.crs_system = float(crs_kod_epsg)  #gelen değşikenin epsg kodu
        except ValueError:
            print("Koordinat sistemi EPSG kodu yanlış girildi. Değeri tekrar atamanız gerekmektedir.")
            self.crs_system = None  #gelen değşikenin epsg kodu
        try:
            if (self.x == None) or (self.y == None):
                self.geometry = None
            else:
                if self.z == None:
                    self.geometry = Point(self.x,self.y)    #gelen değişkenin geometri objesi
                elif self.z ==float():
                    self.geometry = Point(self.x,self.y,self.z)
        except ValueError:
            self.geometry = None    #gelen değişkenin geometri objesi   
            return
    def oznitelik_ekleme(self,oznitelik=dict()):   #geometriye ait öznitelik bilgileri bu kısımda saklanabilir
        self.attibuties = {"AD":self.name,"TIP":"Point","X":self.x,"Y":self.y,"Z":self.z}    #ilk olarak dict tipinde bir değişkenimiz olmalı
        for i,c in oznitelik.items():   #kullanıcının verdiği bilgileri for döngüsü ile dict verimizie veriyoruz.
            self.attibuties.update({i:c})

a = point3d()
a.oznitelik_ekleme()
print(a.attibuties)