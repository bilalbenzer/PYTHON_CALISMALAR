"""SHP,TXT,XML,XLSX,PDF,CSV,DOCX"""
import geopandas
import fiona
from shapely.geometry import Point
def shape_olustur2d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.shp")
            konum = r"{}".format(konum)
        except fiona._err.CPLE_AppDefinedError and fiona.errors.DriverError:
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                break
        bos_veri_tabanı = geopandas.GeoDataFrame()
        aaa = -1
        bos_veri_tabanı ["geometry"] = None
        if args == tuple:
            for i in args:
                aaa +=1
                try:                
                    print(i)
                    bos_veri_tabanı.loc[aaa,"geometry"] = i
                except TypeError:
                    print("Shp Formatına çevirilecek Veride Sorun Var. Lütfen Tekrar Deneyiniz.")
                    break
            else:
                bos_veri_tabanı.to_file(konum)
        elif args != tuple:
            try:                
                print(args)
                bos_veri_tabanı.loc[aaa,"geometry"] = args
            except TypeError:
                print("Shp Formatına çevirilecek Veride Sorun Var. Lütfen Tekrar Deneyiniz.")
                break
            else:
                bos_veri_tabanı.to_file(konum)
def shape_olustur3d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.shp")
            konum = r"{}".format(konum)
        except fiona._err.CPLE_AppDefinedError and fiona.errors.DriverError:
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                break
        bos_veri_tabanı = geopandas.GeoDataFrame()
        aaa = -1
        bos_veri_tabanı ["geometry"] = None
        if args == tuple:
            for i in args:
                aaa +=1
                try:                
                    print(i)
                    bos_veri_tabanı.loc[aaa,"geometry"] = i
                except TypeError:
                    print("Shp Formatına çevirilecek Veride Sorun Var. Lütfen Tekrar Deneyiniz.")
                    break
            else:
                bos_veri_tabanı.to_file(konum)
        elif args != tuple:
            try:                
                print(args)
                bos_veri_tabanı.loc[aaa,"geometry"] = args
            except TypeError:
                print("Shp Formatına çevirilecek Veride Sorun Var. Lütfen Tekrar Deneyiniz.")
                break
            else:
                bos_veri_tabanı.to_file(konum)

def text_olusturma2d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt")
            konum = r"{}".format(konum)
            with open(konum,"w+") as dosya:
                for i in args:
                    print(i)
                    dosya.write(str(i)+"\n")              
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                break
def text_olusturma3d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt")
            konum = r"{}".format(konum)
            with open(konum,"w+") as dosya:
                for i in args:
                    print(i)
                    dosya.write(str(i)+"\n")              
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                break
def xml_olusturma2d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml")
            konum = r"{}".format(konum)
            with open(konum,"w+") as dosya:
                for i in args:
                    print(i)
                    dosya.write(str(i)+"\n")              
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                break           
def xml_olusturma3d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml")
            konum = r"{}".format(konum)
            with open(konum,"w+") as dosya:
                for i in args:
                    print(i)
                    dosya.write(str(i)+"\n")              
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                break           
