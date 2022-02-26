"""SHP,TXT,XML,XLSX,PDF,CSV,DOCX"""
import geopandas
import fiona
import shapely
from shapely.geometry import Point,MultiPoint
from siniflar import point2d,point3d

def shape_olustur2d(args,tip):
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
        args.oznitelik_ekleme()
        obje_oznitelik = args.attibuties

        aaa = -1
        if tip =="nokta":
            print(args.crs_system)
            bos_veri_tabanı1 = geopandas.GeoDataFrame(obje_oznitelik,crs="EPSG:"+str(args.crs_system))
            print(bos_veri_tabanı1)
            bos_veri_tabanı1.to_file(konum)          
        
    else:
        bos_veri_tabanı = 0
def shape_olustur3d(args,tip):
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
        if tip =="nokta":
            veri = {'AD': [args.point_ad],'TIP' : [args.geometri_tip], 'X' : [args.x_koordinati], 'Y' : [args.y_koordinati],'Z' : [args.z_koordinati], 'geometry' : [args.geometri]}
            veritabani = geopandas.GeoDataFrame(veri,crs =f"EPSG:{args.koordinat_sistemi}")
            print(veritabani)
            veritabani.to_file(konum) 
    else:
        bos_veri_tabanı = 0
def text_olusturma2d(args,tip):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt\nDosya Yolu:")
            konum = r"{}".format(konum)             
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt\nDosya Yolu:")
                    konum = r"{}".format(konum)          
                except :
                        print("Konum Bilgisini Yanlış Girdiniz. Program Sonlanmıştır.")
                        break
        if tip =="nokta":
            verii=f"""AD-TIP-X-Y-GEOMETRY
{args.point_ad},{args.geometri_tip},{args.x_koordinati},{args.y_koordinati},{args.geometri}"""
            with open(konum,"w+") as dosya:
                dosya.write(str(verii)+"\n")
def text_olusturma3d(args,tip):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt\nDosya Yolu:")
            konum = r"{}".format(konum)             
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.txt\nDosya Yolu:")
                    konum = r"{}".format(konum)          
                except :
                        print("Konum Bilgisini Yanlış Girdiniz. Program Sonlanmıştır.")
                        break
        if tip =="nokta":
            verii=f"""AD-TIP-X-Y-Z-GEOMETRY
{args.point_ad},{args.geometri_tip},{args.x_koordinati},{args.y_koordinati},{args.z_koordinati},{args.geometri}"""
            with open(konum,"w+") as dosya:
                dosya.write(str(verii)+"\n")
def xml_olusturma2d(args,tip):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml\nDosya Yolu:")
            konum = r"{}".format(konum)             
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml\nDosya Yolu:")
                    konum = r"{}".format(konum)          
                except :
                        print("Konum Bilgisini Yanlış Girdiniz. Program Sonlanmıştır.")
                        break
        if tip =="nokta":
            verii=f"""AD-TIP-X-Y-GEOMETRY
{args.point_ad},{args.geometri_tip},{args.x_koordinati},{args.y_koordinati},{args.geometri}"""
            with open(konum,"w+") as dosya:
                dosya.write(str(verii)+"\n")    
def xml_olusturma3d(args,tip):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml\nDosya Yolu:")
            konum = r"{}".format(konum)             
        except :
                print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
                try:
                    konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xml\nDosya Yolu:")
                    konum = r"{}".format(konum)          
                except :
                        print("Konum Bilgisini Yanlış Girdiniz. Program Sonlanmıştır.")
                        break
        if tip =="nokta":
            verii=f"""AD-TIP-X-Y-Z-GEOMETRY
{args.point_ad},{args.geometri_tip},{args.x_koordinati},{args.y_koordinati},{args.z_koordinati},{args.geometri}"""
            with open(konum,"w+") as dosya:
                dosya.write(str(verii)+"\n")        
def xlsx_olusturma2d(args,tip):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xlsx\nDosya Yolu:")
            konum = r"{}".format(konum)
        except :
            print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
            try:
                konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xlsx\nDosya Yolu:")
                konum = r"{}".format(konum)
            except:
                print("Konum Bilgisini Yanlış Girdiniz.Program sonlanmıştır.")
                break
        if tip =="nokta":
            veri = {'AD': [args.point_ad],'TIP' : [args.geometri_tip], 'X' : [args.x_koordinati], 'Y' : [args.y_koordinati], 'geometry' : [args.geometri]}
            veritabani = geopandas.GeoDataFrame(veri,crs = "EPSG:4326")
            print(veritabani)
            veritabani.to_excel(konum)
        
def xlsx_olusturma3d(args,tip):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xlsx\nDosya Yolu:")
            konum = r"{}".format(konum)
        except :
            print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
            try:
                konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.xlsx\nDosya Yolu:")
                konum = r"{}".format(konum)
            except:
                print("Konum Bilgisini Yanlış Girdiniz.Program sonlanmıştır.")
                break
        if tip =="nokta":
            veri = {'AD': [args.point_ad],'TIP' : [args.geometri_tip], 'X' : [args.x_koordinati], 'Y' : [args.y_koordinati],"Z" : [args.z_koordinati], 'geometry' : [args.geometri]}
            veritabani = geopandas.GeoDataFrame(veri,crs = "EPSG:4326")
            print(veritabani)
            veritabani.to_excel(konum)
def pdf_olusturma2d(args,tip):
    import fpdf
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.pdf\nDosya Yolu:")
            konum = r"{}".format(konum)
        except :
            print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
            try:
                konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.pdf\nDosya Yolu:")
                konum = r"{}".format(konum)
            except:
                print("Konum Bilgisini Yanlış Girdiniz.Program sonlanmıştır.")
                break
        if tip =="nokta":
            verii=f"""
AD              :{args.point_ad}
TIP             :{args.geometri_tip}
X               :{args.x_koordinati}
Y               :{args.y_koordinati}
GEOMETRY        :{args.geometri}
"""
            b = fpdf.FPDF()
            b.add_page()
            b.set_font("Arial","B",15)
            b.write(8,verii)
            b.output(konum,"F")


def pdf_olusturma3d(args,tip):
    import fpdf
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.pdf\nDosya Yolu:")
            konum = r"{}".format(konum)
        except :
            print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
            try:
                konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.pdf\nDosya Yolu:")
                konum = r"{}".format(konum)
            except:
                print("Konum Bilgisini Yanlış Girdiniz.Program sonlanmıştır.")
                break
        if tip =="nokta":
            verii=f"""
AD              :{args.point_ad}
TIP             :{args.geometri_tip}
X               :{args.x_koordinati}
Y               :{args.y_koordinati}
Z               :{args.z_koordinati}
GEOMETRY        :{args.geometri}
"""
            b = fpdf.FPDF()
            b.add_page()
            b.set_font("Arial","B",15)
            b.write(8,verii)
            b.output(konum,"F")
def csv_olusturma2d(args,tip):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.csv\nDosya Yolu:")
            konum = r"{}".format(konum)
        except :
            print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
            try:
                konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.csv\nDosya Yolu:")
                konum = r"{}".format(konum)
            except:
                print("Konum Bilgisini Yanlış Girdiniz.Program sonlanmıştır.")
                break
        if tip =="nokta":
            veri = {'AD': [args.point_ad],'TIP' : [args.geometri_tip], 'X' : [args.x_koordinati], 'Y' : [args.y_koordinati], 'geometry' : [args.geometri]}
            veritabani = geopandas.GeoDataFrame(veri,crs = "EPSG:4326")
            print(veritabani)
            veritabani.csv(konum)
def csv_olusturma3d(args,tip):
    for i in range(1):
        try:
            konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.csv\nDosya Yolu:")
            konum = r"{}".format(konum)
        except :
            print("Konum Bilgisini Yanlış Girdiniz. Lütfen Tekrar Deneyiniz.")
            try:
                konum=input("Dosyayı kaydetmek istediğiniz konumu giriniz. Örnek:C:/Users/.../name.csv\nDosya Yolu:")
                konum = r"{}".format(konum)
            except:
                print("Konum Bilgisini Yanlış Girdiniz.Program sonlanmıştır.")
                break
        if tip =="nokta":
            veri = {'AD': [args.point_ad],'TIP' : [args.geometri_tip], 'X' : [args.x_koordinati], 'Y' : [args.y_koordinati],'Z' : [args.z_koordinati], 'geometry' : [args.geometri]}
            veritabani = geopandas.GeoDataFrame(veri,crs = "EPSG:4326")
            print(veritabani)
            veritabani.csv(konum)

