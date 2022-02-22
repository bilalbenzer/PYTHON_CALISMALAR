hosgeldin_mesaji="""
----------------------------------------------------------
---- KASA İÇİN FİŞ DÜZENLEME UYGULAMAMIZA HOŞGELDİNİZ ----
----------------------------------------------------------
"""
cikis_mesaji="""
-------------------------------------------------------------------
---- UYGULAMA SONLANMIŞTUR. KULLANDIĞINIZ İÇİN TEŞEKKÜR EDERİZ ----
-------------------------------------------------------------------
"""
while True:
    while True:     #döngü başlayacak burada
        print(hosgeldin_mesaji)
        degisken=[1]
        degisken2=[1]
        urun_fiyat_listesi={"kitap":45,"çikolata":2,"kalem":3,"mendil":4,"telefon":1500}    #mağazada yer alan ürünler burada listelenmiştir.
        adet = "s"
        def urun_listesi_ekleme():      #ürün eklenecekse eğer bu def çalışacak
            global degisken #kullanıcı girişlerinde hata olabieceği için boş bir liste tanımlandı. hatalı girişlerde listeye eleman
                            #eklenecek ve hataya göre tepki verilecek
            degisken=[]
            try:    #adet miktarı girilirken hata olabileceği için bu blok çalışacak
                global adet
                print(len("Kaç adet ürün ekleyeceksiniz ?")*"-")
                adet = int(input("Kaç adet ürün ekleyeceksiniz ?\nCevap:")) #kullanıcıdan adet bilgisi istenecek. for döngüsü olması için inte çevrilecek
            except ValueError:  #hata gelmesi durumunda bu blok çalışacak ve kullanıcıdan tekrar giriş istenecek
                print(len("Ürün adetini yanlış girdiniz. Lütfen bir sayı verisi giriniz.")*"-")
                print("Ürün adetini yanlış girdiniz. Lütfen bir sayı verisi giriniz.\nCevap:")
                try:               #tekrar hatalı giriş yapılması ihtimaline karşı 2. bir hata yakalama bloğu olacak
                    print(len("Kaç adet ürün ekleyeceksiniz ?")*"-")
                    adet = int(input("Kaç adet ürün ekleyeceksiniz ?\nCevap"))
                except ValueError:  #kullanıcı 2. kez hatalı giriş yaparsa bu blok çalışacak
                    print(len("Ürün adetini 2. kez yanlış girdiniz. Program sonlanmıştır.")*"-")
                    print("Ürün adetini 2. kez yanlış girdiniz. Program sonlanmıştır.") 
                    degisken.append(3)  #2. kez hata olduğu için degisken listesine 3 eklenecek. bunun amacı,
                                        #fonksiyon çalıştıktan sonra bu listede 3 varsa while döngüsü kırılacak
                    pass
                pass
            if degisken==[]:    #yukarıdaki işlemlerde hata gelemzse degisken listesi boş liste olacak. bu durumda işlemde hata olmadığı
                                #için bu blok çalışacak.
                for i in range((adet)): #kullanıcı girdiği adet kadar ürün eklemesi için for döngüsü kurulacak.
                    print(len("Ürün adını giriniz.")*"-")
                    eklenecek_urun_adi = input("Ürün adını giriniz.\nCevap:").lower()   #kullanıcının girdiği her ürün, küçük harfe çevrilecek
                    try:    #fiyat eklenirken sayısal karakter girilmeli. str girilemsine karşın hata yakalama çalışacak.
                        print(len("Ürün fiyatını giriniz.")*"-")
                        eklenecek_urun_fiyati = int(input("Ürün fiyatını giriniz.\nCevap:"))    
                    except ValueError:  #hatalı girilmesi durumunda bu blok 2. kez kullanıcıdan veri isteyecek
                        print("Ürün fiyatını yanlış girdiniz. LÜtfen sayı olarak giriniz.")  
                        try:    #kullanıcı 2. kez hatalı giriş yapması durumu için hata yakalama çalışacak
                            print(len("Ürün fiyatını giriniz.")*"-")
                            eklenecek_urun_fiyati = int(input("Ürün fiyatını giriniz.\nCevap:"))
                        except ValueError:
                            print(len("Ürün fiyatını 2. kez yanlış girdiniz. Program sonlanmıştır")*"-")
                            print("Ürün fiyatını 2. kez yanlış girdiniz. Program sonlanmıştır")
                            degisken.append(3)  #kullanıcı 2. kez hatalı giriş yaparsa degisken listesine 3 eklenecek
                            break   #for döngüsü 2. kez hatalı giriş yapılması durumuna karşın kırılacak
                    if degisken==[]:    #for döngüsünde ürün-fiyat için hatalı giriş yapılmazsa bu blok çalışacak ve urun fiyat listesi
                                        #güncellenecek
                        urun_fiyat_listesi.update({eklenecek_urun_adi:eklenecek_urun_fiyati})
                else:
                    pass
            else:
                pass  
        def urun_silme():   #ürün silinecekse eğer bu def çalışacak
            aaa=len("Marketimizde yer alan ürünler aşağıdaki gibidir.")*"-"+"\n"+"Marketimizde yer alan ürünler aşağıdaki gibidir."
            print(aaa)  #mevcut ürünleri burada kullanıcıya gösteriyoruz.
            for key,value in urun_fiyat_listesi.items():
                print(key+" : "+str(value)+"TL")
            global degisken2
            degisken2=[]
            try:    #adet miktarı girilirken hata olabileceği için bu blok çalışacak
                global adet
                print(len("Kaç adet ürün sileceksiniz ?")*"-")
                adet = int(input("Kaç adet ürün sileceksiniz ?\nCevap:")) #kullanıcıdan adet bilgisi istenecek. for döngüsü olması için inte çevrilecek
            except ValueError:  #hata gelmesi durumunda bu blok çalışacak ve kullanıcıdan tekrar giriş istenecek
                print(len("Ürün adetini yanlış girdiniz. Lütfen bir sayı verisi giriniz.")*"-")
                print("Ürün adetini yanlış girdiniz. Lütfen bir sayı verisi giriniz.\nCevap:")
                try:               #tekrar hatalı giriş yapılması ihtimaline karşı 2. bir hata yakalama bloğu olacak
                    print(len("Kaç adet ürün sileceksiniz ?")*"-")
                    adet = int(input("Kaç adet ürün sileceksiniz ?\nCevap"))
                except ValueError:  #kullanıcı 2. kez hatalı giriş yaparsa bu blok çalışacak
                    print(len("Ürün adetini 2. kez yanlış girdiniz. Program sonlanmıştır.")*"-")
                    print("Ürün adetini 2. kez yanlış girdiniz. Program sonlanmıştır.") 
                    degisken2.append(3)  #2. kez hata olduğu için degisken listesine 3 eklenecek. bunun amacı,
                                        #fonksiyon çalıştıktan sonra bu listede 3 varsa while döngüsü kırılacak
                    pass
                pass
            if degisken2==[]:    #yukarıdaki işlemlerde hata gelemzse degisken listesi boş liste olacak. bu durumda işlemde hata olmadığı
                                #için bu blok çalışacak.
                for i in range((adet)): #kullanıcı girdiği adet kadar ürün eklemesi için for döngüsü kurulacak.
                    print(len("Ürün adını giriniz.")*"-")
                    silinecek_urun_adi = input("Ürün adını giriniz.\nCevap:").lower()   #kullanıcının girdiği her ürün, küçük harfe çevrilecek
                    try:    #fiyat eklenirken sayısal karakter girilmeli. str girilemsine karşın hata yakalama çalışacak.
                        print(len("Ürün fiyatını giriniz.")*"-")
                        silinecek_urun_fiyati = int(input("Ürün fiyatını giriniz.\nCevap:"))    
                    except ValueError:  #hatalı girilmesi durumunda bu blok 2. kez kullanıcıdan veri isteyecek
                        print("Ürün fiyatını yanlış girdiniz. LÜtfen sayı olarak giriniz.")  
                        try:    #kullanıcı 2. kez hatalı giriş yapması durumu için hata yakalama çalışacak
                            print(len("Ürün fiyatını giriniz.")*"-")
                            silinecek_urun_fiyati = int(input("Ürün fiyatını giriniz.\nCevap:"))
                        except ValueError:
                            print(len("Ürün fiyatını 2. kez yanlış girdiniz. Program sonlanmıştır")*"-")
                            print("Ürün fiyatını 2. kez yanlış girdiniz. Program sonlanmıştır")
                            degisken2.append(3)  #kullanıcı 2. kez hatalı giriş yaparsa degisken listesine 3 eklenecek
                            break   #for döngüsü 2. kez hatalı giriş yapılması durumuna karşın kırılacak
                    if degisken2==[]:    #for döngüsünde ürün-fiyat için hatalı giriş yapılmazsa bu blok çalışacak ve urun fiyat listesi
                                        #güncellenecek
                        del urun_fiyat_listesi[silinecek_urun_adi]  #ilgili ürün silinir.
                else:
                    pass
            else:
                pass  

        yazi1="Fiş çıkarmadan önce, ürün eklemek veya silmek istiyor musunuz?"     #kullanıcıya ürün-fiyat eklemesi veya silmesi yapıp yapmayacağı soruluyor.
        uzunluk_metni=len(yazi1)*"-"+"\n"+yazi1
        urun_ekleencek_mi=input(uzunluk_metni+"\nÜrün eklemek isiyorum:1\nÜrün silmek istiyorum:2\nFiş çıkarmak istiyorum:3\nCevap:")
        if urun_ekleencek_mi=="1":  #kullanıcı 1 cevabını verirse bu blok çalışacak
            urun_listesi_ekleme()   #ürün ekleme fonksiyonu çalıaşcak
            if degisken==[3]:   #hatalı girişlerde degisken e 3 eklemiştik. bu durumlar varsa bu blok çalışacak ve döngüyü kıracak
                break
            elif degisken==[]:  #degisken listesine herhangi veri girmemişse yani işlemlerde hata yoksa program devam edecek
                print(len("Girmiş olduğunuz ürünler, ürün fiyat listesine dahil edilmiştir.Ürün fiyat listesindeki son durum aşağıdaki gibidir.")*"-")
                print("Girmiş olduğunuz ürünler, ürün fiyat listesine dahil edilmiştir.Ürün fiyat listesindeki son durum aşağıdaki gibidir.")
                for a,b in urun_fiyat_listesi.items():
                    print(a,b)    #ekrana ürün-fiyat bilgisi yazılacak
        elif urun_ekleencek_mi=="2":
            urun_silme()
            if degisken2==[3]:
                break
            elif degisken2==[]:
                print(len("Girmiş olduğunuz ürünler, ürün fiyat listesinden silinmiştir..Ürün fiyat listesindeki son durum aşağıdaki gibidir.")*"-")
                print("Girmiş olduğunuz ürünler, ürün fiyat listesinden silinmiştir.Ürün fiyat listesindeki son durum aşağıdaki gibidir.")
                for a,b in urun_fiyat_listesi.items():
                    print(a,b)    #ekrana ürün-fiyat bilgisi yazılacak

        elif urun_ekleencek_mi=="3":    #kullanıcı 2 cevabı verirse işlem devam edecek.
            yazi1="İşleme devam edebilirsiniz."
            uzunluk_metni=len(yazi1)*"-"+"\n"+yazi1
            print(uzunluk_metni)
            pass        
        else:   #kullanıcı 1 veya 2 dışında bir cevap verirse uyarı verilecek ve 2. kez kullanıcıya ürün ekleyip eklemyeecği sorulacak
            yazi1="Yanlış bir seçim yaptınız.Tekrar deneyiniz."
            uzunluk_metni=len(yazi1)*"-"+"\n"+yazi1
            print(uzunluk_metni)

            yazi1="Fiş çıkarmadan önce, ürün eklemek veya silmek istiyor musunuz?"     #kullanıcıya ürün-fiyat eklemesi veya silmesi yapıp yapmayacağı soruluyor.
            uzunluk_metni=len(yazi1)*"-"+"\n"+yazi1
            urun_ekleencek_mi=input(uzunluk_metni+"\nÜrün eklemek isiyorum:1\nÜrün silmek istiyorum:2\nFiş çıkarmak istiyorum:3\nCevap:")
            if urun_ekleencek_mi=="1":  #kullanıcı 1 derse aynı ürün ekleme fonksiyonu çalışacak
                urun_listesi_ekleme()
                if degisken==[3]:   #hatalı girişlerde degisken e 3 eklemiştik. bu durumlar varsa bu blok çalışacak ve döngüyü kıracak
                    break
                elif degisken==[]:  #degisken listesine herhangi veri girmemişse yani işlemlerde hata yoksa program devam edecek
                    pass
            elif urun_ekleencek_mi=="2":
                urun_silme()
                if degisken2==[3]:
                    break
                elif degisken2==[]:
                    print(len("Girmiş olduğunuz ürünler, ürün fiyat listesinden silinmiştir..Ürün fiyat listesindeki son durum aşağıdaki gibidir.")*"-")
                    print("Girmiş olduğunuz ürünler, ürün fiyat listesinden silinmiştir.Ürün fiyat listesindeki son durum aşağıdaki gibidir.")
                    for a,b in urun_fiyat_listesi.items():
                        print(a,b)    #ekrana ürün-fiyat bilgisi yazılacak
            elif urun_ekleencek_mi=="3":    #kullanıcı 2 derse işlem devam edecek.
                yazi1="İşleme devam edebilirsiniz."
                uzunluk_metni=len(yazi1)*"-"+"\n"+yazi1
                print(uzunluk_metni)
                pass        
            else:
                yazi1="2. Kez Hatalı Seçim Yaptınız.Program Sonlanmıştır."  #kullanıcı 2. kez yanlış cevap verirse program sonlanacak
                uzunluk_metni=len(yazi1)*"-"+"\n"+yazi1
                print(uzunluk_metni)
                break
        #kasa işlemleri
        alinan_urun_listesi=[]  #alınan ürünlerin eklenmesi için boş bir liste tanımladım
        urun_listesi=urun_fiyat_listesi.keys()  #mevcutta bulunan ürünleri kullanıcıya gösterebilmek için urun fiyat listesinden keyleri alıyorum
        urun_adi=str    #aşağıda kullanıcıdan urun adı isteyeceğiz. bunun için urun adında boş değişken tanımladım
        urun_fiyatlari=[]   #ürün fiyatlarının eklenmesi için boş bir ürün fiyatları listesi tanımladım.
        aaa=len("Marketimizde yer alan ürünler aşağıdaki gibidir.")*"-"+"\n"+"Marketimizde yer alan ürünler aşağıdaki gibidir."
        print(aaa)  #mevcut ürünleri burada kullanıcıya gösteriyoruz.
        for key,value in urun_fiyat_listesi.items():
            print(key+" : "+str(value)+"TL")
        alinan_urunler=list()#alınan ürünleri kullanıcıya göstermek için boş bir liste tanımladım
        toplam_tutar=0  #son adımda toplam tutar hesaplanacağı için boş bir toplam tutar değişkeni tanımladım
        try:    ##kullanıcıdan kaç tane ürün aldığını soruyoruz.
            print(len("Kaç tane ürün aldınız?")*"-")
            for i in range(int(input("Kaç tane ürün aldınız?"))):
                print(len("Ürün adını giriniz.")*"-")   
                urun_adi=input("Ürün adını giriniz.")   #kullanıcı adet bilgisi verdikten sonra ilk önce ürün adını giriyoruz.
                
                urun_fiyatlari.append((urun_fiyat_listesi[urun_adi]))   #kullanıcın aldığı ürünün fiyatını urun fiyat listesi dict inden
                                                            #çekerek fiyatını urun fiyatları listesine ekliyoruz.
                alinan_urun_listesi.append(urun_adi)        #alınan ürün listesine kullanıcının aldığı ürünü ekliyoruz.
            else:       #for döngüsü sorunsuz şekilde biterse bu blok ile toplam tutar miktarını hesaplıyoruz.
                for i in urun_fiyatlari:
                    toplam_tutar+=int(i)
                print(f"Almış olduğunuz ürün listesi:\n{alinan_urun_listesi}\nÖdemeniz gereken toplam tutar:\n{toplam_tutar}")
        except: #kullanıcı ürün fiyatı veya ürün adını hatalı girerse bu blok çalışıyor ve tekrardan kullanıcıdan girmesini istiyoruz.

            try:    #kullanıcı tekrar hatalı seçim yapabilir diye tekrardan hata yakalama açıyoruz
                print(len("Marketimizde yer alan ürünler aşağıdaki gibidir.")*"-")
                print(f"Marketimizde yer alan ürünler aşağıdaki gibidir.\n{urun_listesi}")  #mevcut ürünleri burada kullanıcıya gösteriyoruz.
                print(len("Hatalı bir seçim yaptınız. Lütfen tekrar deneyiniz.")*"-")
                print("Hatalı bir seçim yaptınız.Lütfen tekrar deneyiniz.")
                print(len("Kaç tane ürün aldınız?")*"-")
                for i in range(int(input("Kaç tane ürün aldınız?"))):   #kullanıcıdan tekrar adet bilgisi istiyoruz.
                    print(len("Ürün adını giriniz.")*"-")
                    urun_adi=input("Ürün adını giriniz.")   
                    urun_fiyatlari.append((urun_fiyat_listesi[urun_adi]))
                    alinan_urun_listesi.append(urun_adi)
                else:
                    for i in urun_fiyatlari:
                        toplam_tutar+=int(i)
                    print(f"Almış olduğunuz ürün listesi:\n{alinan_urun_listesi}\nÖdemeniz gereken toplam tutar:\n{toplam_tutar}")
            except: #kullanıcı 2. kez hatalı giriş yaparsa program sonlanıyor.
                print(len("2. Kez hatalı giriş yaptınız. Program sonlamıştır.")*"-")
                print("2. Kez hatalı giriş yaptınız. Program sonlamıştır.")
                break
    print(len("Programa devam etmek istiyor musunuz?")*"-")        
    programa_devam_edilecek_mi=input("Programa devam etmek istiyor musunuz?\nEvet:1\nHayır:2\nCevap:")
    if programa_devam_edilecek_mi=="1":
        pass
    elif programa_devam_edilecek_mi=="2":
        print(cikis_mesaji)
        break
    else:
        print(len("Hatalı bir seçim yaptınız")*"-")
        print("Hatalı bir seçim yaptınız.\n"+cikis_mesaji)          
        
    
    

