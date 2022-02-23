"""SHP,TXT,XML,XLSX,PDF,CSV,DOCX"""
import geopandas
import fiona
import shapely
from shapely.geometry import Point
import xlsxwriter
def shape_olustur2d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.shp\nDosya Yolu:")
            konum = r"{}".format(konum)
        except fiona._err.CPLE_AppDefinedError and fiona.errors.DriverError:
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.shp\nDosya Yolu:")
                    konum = r"{}".format(konum)
                except fiona._err.CPLE_AppDefinedError and fiona.errors.DriverError:
                    print("Dosya Yolunu 2. kez yanlış girdiniz. Program sonlanmıştır.")
        bos_veri_tabanı1 = geopandas.GeoDataFrame()
        aaa = -1
        bos_veri_tabanı1 ["geometry"] = None
        if type(args) == tuple:
            for i in args:
                aaa +=1
                try:                
                    print(i)
                    bos_veri_tabanı1.loc[aaa,"geometry"] = i
                except TypeError:
                    print("Shp Formatına çevirilecek Veride Sorun Var. Lütfen Tekrar Deneyiniz.")
                    break
            else:
                bos_veri_tabanı1.to_file(konum)
        elif type(args) == shapely.geometry.point.Point:
            try:                
                print(args)
                bos_veri_tabanı1.loc[aaa,"geometry"] = args
            except TypeError:
                print("Shp Formatına çevirilecek Veride Sorun Var. Lütfen Tekrar Deneyiniz.")
                break
            else:
                bos_veri_tabanı1.to_file(konum)
def shape_olustur3d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.shp\nDosya Yolu:")
            konum = r"{}".format(konum)
        except fiona._err.CPLE_AppDefinedError and fiona.errors.DriverError:
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.shp\nDosya Yolu:")
                    konum = r"{}".format(konum)
                except fiona._err.CPLE_AppDefinedError and fiona.errors.DriverError:
                    print("Dosya Yolunu 2. kez yanlış girdiniz. Program sonlanmıştır.")
                    break
        bos_veri_tabanı = geopandas.GeoDataFrame()
        aaa = -1
        bos_veri_tabanı ["geometry"] = None
        if type(args) == tuple:
            for i in args:
                aaa +=1
                try:                
                    print(i)
                    bos_veri_tabanı.loc[aaa,"geometry"] = i
                except TypeError:
                    print("Shp Formatına çevirilecek Veride Sorun Var. Lütfen Tekrar Deneyiniz.")
                    try:                
                        print(i)
                        bos_veri_tabanı.loc[aaa,"geometry"] = i
                    except TypeError:
                        print("Shp Formatına çevirilecek Veride Sorun Var. Program sonlanmıştır.")
                        break
            else:
                bos_veri_tabanı.to_file(konum)
        elif type(args) == shapely.geometry.point.Point:
            try:                
                print(args)
                bos_veri_tabanı.loc[aaa,"geometry"] = args
            except TypeError:
                print("Shp Formatına çevirilecek Veride Sorun Var. Lütfen Tekrar Deneyiniz.")
                try:                
                    print(i)
                    bos_veri_tabanı.loc[aaa,"geometry"] = i
                except TypeError:
                    print("Shp Formatına çevirilecek Veride Sorun Var. Program sonlanmıştır.")
                    break
            else:
                bos_veri_tabanı.to_file(konum)
def text_olusturma2d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt\nDosya Yolu:")
            konum = r"{}".format(konum)
            with open(konum,"w+") as dosya:
                for i in args:
                    print(i)
                    dosya.write(str(i)+"\n")              
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt\nDosya Yolu:")
                    konum = r"{}".format(konum)
                    with open(konum,"w+") as dosya:
                        for i in args:
                            print(i)
                            dosya.write(str(i)+"\n")              
                except :
                        print("Konum Bilgisini Yanlış Girdiniz. Program Sonlanmıştır.")
                        break
def text_olusturma3d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt\nDosya Yolu:")
            konum = r"{}".format(konum)
            with open(konum,"w+") as dosya:
                for i in args:
                    print(i)
                    dosya.write(str(i)+"\n")              
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt\nDosya Yolu:")
                    konum = r"{}".format(konum)
                    with open(konum,"w+") as dosya:
                        for i in args:
                            print(i)
                            dosya.write(str(i)+"\n")              
                except :
                        print("Konum Bilgisini Yanlış Girdiniz. Program Sonlanmıştır.")
                        break
def xml_olusturma2d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml\nDosya Yolu:")
            konum = r"{}".format(konum)
            with open(konum,"w+") as dosya:
                for i in args:
                    print(i)
                    dosya.write(str(i)+"\n")              
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml\nDosya Yolu:")
                    konum = r"{}".format(konum)
                    with open(konum,"w+") as dosya:
                        for i in args:
                            print(i)
                            dosya.write(str(i)+"\n")              
                except :
                        print("Konum Bilgisini Yanlış Girdiniz. Program sonlanmıştır.") 
                        break          
def xml_olusturma3d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml\nDosya Yolu:")
            konum = r"{}".format(konum)
            with open(konum,"w+") as dosya:
                for i in args:
                    print(i)
                    dosya.write(str(i)+"\n")              
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml\nDosya Yolu:")
                    konum = r"{}".format(konum)
                    with open(konum,"w+") as dosya:
                        for i in args:
                            print(i)
                            dosya.write(str(i)+"\n")              
                except :
                        print("Konum Bilgisini Yanlış Girdiniz.Program sonlanmıştır.")
                        break           
def xlsx_olusturma2d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xlsx\nDosya Yolu:")
            konum = r"{}".format(konum)
            xlsx_file = xlsxwriter.Workbook(konum)
            dosya = xlsx_file.add_worksheet()
            sutun_ad="A"
            sutun_no=0
            for i in args:
                sutun_no+=1
                dosya.write(sutun_ad+str(sutun_no),str(i))
            else:
                xlsx_file.close()
        except :
            print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
            try:
                konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xlsx\nDosya Yolu:")
                konum = r"{}".format(konum)
                xlsx_file = xlsxwriter.Workbook(konum)
                dosya = xlsx_file.add_worksheet()
                sutun_ad="A"
                sutun_no=0
                for i in args:
                    sutun_no+=1
                    dosya.write(sutun_ad+str(sutun_no),str(i))
                else:
                    xlsx_file.close()
            except:
                print("Konum Bilgisini Yanlış Girdiniz.Program sonlanmıştır.")
                break
def xlsx_olusturma3d(args):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xlsx\nDosya Yolu:")
            konum = r"{}".format(konum)
            xlsx_file = xlsxwriter.Workbook(konum)
            dosya = xlsx_file.add_worksheet()
            sutun_ad="A"
            sutun_no=0
            for i in args:
                sutun_no+=1
                dosya.write(sutun_ad+str(sutun_no),str(i))
            else:
                xlsx_file.close()
        except :
            print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
            try:
                konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xlsx\nDosya Yolu:")
                konum = r"{}".format(konum)
                xlsx_file = xlsxwriter.Workbook(konum)
                dosya = xlsx_file.add_worksheet()
                sutun_ad="A"
                sutun_no=0
                for i in args:
                    sutun_no+=1
                    dosya.write(sutun_ad+str(sutun_no),str(i))
                else:
                    xlsx_file.close()
            except:
                print("Konum Bilgisini Yanlış Girdiniz.Program sonlanmıştır.")
                break



