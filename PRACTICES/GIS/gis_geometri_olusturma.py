from shapely.geometry import Point,LineString,Polygon
##############                          nokta oluşturma                              ##############
point1 = Point(2.2,4.2) #1. nokta # parametrede 3. parametre z değeri. 1. parametre x 2. parametre y
point2 = Point(7.2,-25.1)
point3 = Point(9.26,-2.456)
point3D = Point(9.26,-2.456,0.57)

print(point1,point2,point3,point3D)

#koordinat alma
point_coords = point1.coords
#tipi
print(type(point_coords))
#gerçek koordinatları alma
xy = point_coords.xy    #xy toplu koordinat alma
x = point1.x            #x koordinat       
y = point1.y            #y koordinat
print(xy,"\n",x,"\n",y)

#2 nokta arası uzaklık ölçme (wgs de derece ile, utm de metre ile)
point_dist = point1.distance(point2)
print(f"2 nokta arası uzaklık {point_dist}")

##############                          çizgi oluşturma                              ##############
line = LineString([point1,point2,point3])
line2 = LineString([(2.2,4.2),(1.3,4.6)])
print(line,line2)
#çizgilerin ağırlık noktası, uzunluğu, çizgi boyunca belli mesafede nokta oluşturma, en yakın mesafe hesaplama, geometriyi basitleştirme gibi fonksiyonlar vardır
#çizgi koordinatları çıkarma
xy1 = line.xy   #tüm koordinatlar gelir
print(xy1)
x1 = xy1[0]     #x koordinatı
y1 = xy1[1]     #y koordinatı
print(x1,y1)

#çizgi uzunluğu hesabı
line_uzunluk = line.length  #çizgi uzunluğu hesaplama
line_agirlik_nokta = line.centroid  #çizgi ağırlık merkezi koordinatı görme
agirlik_merkez_tip = type(line_agirlik_nokta)   #ağırlık merkezi noktası tipi
print(line_uzunluk)
print(line_agirlik_nokta)
print(agirlik_merkez_tip)

##############                          poligon oluşturma                              ##############
#koordinatlardan poligon oluşturma
poli = Polygon([(2.2,4.2), (7.2,-25.1), (9.26,-2.456)])     #koordinatlar yerine pointleri de verebiliriz. aynı şey
poli2 = Polygon([[p.x,p.y] for p in [point1,point2,point3]])    #noktalardan koordinatları bu şekilde de alabiliriz
poli_tip = poli.geom_type       #geometri tipinin 1. yolu
poli_tip2 = type(poli)          #2. yolu
print(poli , "\n" , poli2 , "\n" , poli_tip , "\n" , poli_tip2)

#UYARU
#poligonların içinde boşluk olabilir. ilk başta poligon tanımlarken 2 tırnak olmasının sebebi o yüzdendir.örnek aşağıda
dis_alan = [(-180,90),(-180,-90),(180,-90),(180,90)]        #dış alan koordinatlarını bu şekilde tanımladık
ic_alan = [[(-170,80),(-170,-80),(170,-80),(170,80)]]       #iç alan koordinatları da bu şekilde. çift tırnağa dikkat
ic_alanli_dis_alan = Polygon(shell=dis_alan)                #ilk önce tüm alanı gösterdik
delikli_dis_alan = Polygon(shell=dis_alan,holes=ic_alan)    #iç alanın dış alandan çıkarılmış hali de bu şekilde
print(dis_alan)
print(ic_alan)
print(delikli_dis_alan) #çıktıdaki ilk parantezli yer dış alan koordinatını, 2. parantezli yer iç alan koordinatını gösterir
#çokgende ağırlık merkezi, alan miktarı, dış ve dış uzunluk gibi nitelikleri görebiliriz.
#ağırlık merkezi
alan1_agirlik_merkezi = ic_alanli_dis_alan.centroid
#alan miktarı
alan1_alani = ic_alanli_dis_alan.area
#çokgenin sınırlayıcı kutusu (sınırları)
alan1_sinirlari = ic_alanli_dis_alan.bounds
#çokgenin dışı
alan1_cokgenin_disi = ic_alanli_dis_alan.exterior
#dış uzunluğu
alan1_dis_uzunluk = alan1_cokgenin_disi.length
print(alan1_agirlik_merkezi)
print(alan1_alani)
print(alan1_sinirlari)
print(alan1_cokgenin_disi)
print(alan1_dis_uzunluk)


##############                          çoklu nesne oluşturma                              ##############
#bu özelliği, arvgisteki bir katman altında birden fazla geometri olması şeklinde tanımlayabiliriz. mesela bir plandaki adalar veya kaldırımlar vs vs
from shapely.geometry import MultiPoint, MultiPolygon, MultiLineString,box
#multi point çoklu nokta oluşturma
coklu_nokta =  MultiPoint([point1,point2,point3])
#aynı şekilde koordinat vererek yapılabilir. 
#multiline çoklu çizgi oluşturma
coklu_cizgi = MultiLineString([line,line2])
#multipolygon çoklu çokgen oluşturma
coklu_poliigon = MultiPolygon([poli,poli2])
print(coklu_nokta)
print(coklu_cizgi)
print(coklu_poliigon)

#geometrik araçlar, hemen hemen arcgiste bulunan fonksiyonlarla aynı mantıktadır. burada sadece çizerek değil de el ile kendimiz değer vererek oluşturmaktayız

