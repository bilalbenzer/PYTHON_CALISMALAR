
hosgeldin_mesaji="""
----------------------------
--- PROGRAMA HOŞGELDİNİZ ---
----------------------------
"""

cikis_mesaji="""
-------------------------------------------------------
--- PROGRAMIMIZI KULLANDIĞINIZ İÇİN TEŞEKKÜR EDERİZ ---
-------------------------------------------------------
"""
print(hosgeldin_mesaji)
bolum_listesi=[]    #asal olmayan sayılar için bolum listesi çıkarmak için boş bir liste
asal_sayi_mi=""     #asal sayı değilse bölüm listesi bulmak için tanımlanan boş değişken. 
while True:   #döngünün başlangıcı. kullanıcı sonlandırıncaya kadar devam eder
    try:
        uyari1="NOT: 0,1 ve 2 dışında sayı girmeniz gerekmektedir." 
        a=len(uyari1)*"-"
        print(a+"\n"+uyari1+"\n") #yasaklı kelimelerin gösterilmesi
        a=len("Sorgulamak istediğiniz sayıyı giriniz.")*"-"+"\n"
        sayi= int(input(a+"Sorgulamak istediğiniz sayıyı giriniz.\n"+"Sayi="))      #kullanıcıdan sayı alma bölümü
    except ValueError as hata:  #kullanıcıdan yanlış bir değer gelmesi halinde hata bloğu
        yazi1="Orjinal Hata Metni:"
        a=len((yazi1))*"-"
        hata=str(hata)
        print(a+"\n"+yazi1+"\n:"+hata+"\n")   #valuerror hatasının verilmesi
        uyari1="Yanlış bir değer girdiniz. Lütfen sayı değeri giriniz."
        a=len(uyari1)*"-"
        print(a+"\n"+uyari1+"\n") #girilecek değere ait açıklama
        #aşağıdaki bölüm, hatalı giriş olduğu için tekrar deneneceğine dair kullanıcıya soru sorar
        uyari1="İşleme Devam Etmek İstiyor Musunuz?\nEvet:+\nHayır:-\nCevap:"
        x=input(len("İşleme Devam Etmek İstiyor Musunuz?")*"-"+"\n"+uyari1)
        if x=="+":
            uyari1="İşleme devam edebilirsiniz."
            a=len(uyari1)*"-"
            print(a+"\n"+uyari1)
            continue
        elif x=="-":
            print(cikis_mesaji)
            break
        else:
            uyari1="Yanlış bir cevap girdiniz. Lütfen Tekrar deneyin."
            a=len(uyari1)*"-"
            print(a+"\n"+uyari1)
            uyari1="İşleme Devam Etmek İstiyor Musunuz?\nEvet:+\nHayır:-\nCevap:"
            x=input(len("İşleme Devam Etmek İstiyor Musunuz?")*"-"+"\n"+uyari1)
            if x=="+":
                uyari11="İşleme devam edebilirsiniz."
                a=len(uyari1)*"-"
                print(a+"\n"+uyari1)
                continue
            elif x=="-":
                print(cikis_mesaji)
                break
            else:
                uyari1="Yanlış bir cevap girdiniz.İşlem sonlanmıştır."
                a=len(uyari1)*"-"
                print(a+"\n"+cikis_mesaji)
                break
    if sayi == 1 or sayi==0 or sayi == 2:   #kullanıcı, yasaklı kelimeleri girerse bu blok devreye girecek.
        uyari1="Girilen değerlerin bu programda kullanılmaması gerekmektedir. Lütfen tekrar deneyiniz."
        a=len(uyari1)*"-"
        print(a+"\n"+uyari1+"\n") #uyarı mesajı
        #aşağıdaki bölüm, hatalı giriş olduğu için tekrar deneneceğine dair kullanıcıya soru sorar

        uyari1="İşleme Devam Etmek İstiyor Musunuz?\nEvet:+\nHayır:-\nCevap:"
        x=input(len("İşleme Devam Etmek İstiyor Musunuz?")*"-"+"\n"+uyari1)
        if x=="+":
            uyari1="İşleme devam edebilirsiniz."
            a=len(uyari1)*"-"
            print(a+"\n"+uyari1)
            continue
        elif x=="-":
            print(cikis_mesaji)
            break
        else:
            uyari1="Yanlış bir cevap girdiniz. Lütfen Tekrar deneyin."
            a=len(uyari1)*"-"
            print(a+"\n"+uyari1)
            uyari1="İşleme Devam Etmek İstiyor Musunuz?\nEvet:+\nHayır:-\nCevap:"
            x=input(len("İşleme Devam Etmek İstiyor Musunuz?")*"-"+"\n"+uyari1)
            if x=="+":
                uyari11="İşleme devam edebilirsiniz."
                a=len(uyari1)*"-"
                print(a+"\n"+uyari1)
                continue
            elif x=="-":
                print(cikis_mesaji)
                break
            else:
                uyari1="Yanlış bir cevap girdiniz.İşlem sonlanmıştır."
                a=len(uyari1)*"-"
                print(a+"\n"+cikis_mesaji)
                break
    
    for i in range(2,sayi): #kullanıcının verdiği sayıyı for döngüsüne sokarak asal olup olamdığını tespit ediyoruz.
        kalan=sayi%i        #sayının her dönen sayıya kalanı hesaplanıyor
        asal_sayi_mi=""    
        if kalan==0:   #kalan 0 çıkarsa bu blok devreye girer.            
            asal_sayi_mi="hayır"
            bolum_listesi.append(i)
        #kalan 0 haricinde olursa bu bloktaki değişkrn boş string olacak 
        elif kalan!=0:
            asal_sayi_mi="" 
    #yukarıdaki for döngüsünde, kalan 0 gelmezse hiç, bu liste boş kalır. eüer listeye eleman girerse aşağıdaki if bloğu devreye girer.
    #kalanın 0 gelmesi, sayının asal olmadığına işarettir. ilgili cevap bu if bloğunda verilir.
    if bolum_listesi!=[]:
        uyari1=f"{sayi} değeri bir asal sayı değildir."
        a=len(uyari1)*"-"
        print(a+"\n"+uyari1+"\n")
        uyari1="Girdiğiniz sayıya dair, bölüm listesini görmek istiyor musunuz?\nEvet:+\nHayır:-\nCevap:"
        a=len("Girdiğiniz sayıya dair, bölüm listesini görmek istiyor musunuz?")*"-"
        x=(str(a)+"\n"+uyari1)
        #sayı eğer asal değilse, başka sayılara da bölünebilir. kalan 0 geldikçe, for döngüsünde, sayının böldüğü her elemanı listeye ekliyor
        #bu sayede bölüm listemiz oluşmuş oluyor.
        bolum_isteniyor_mu=input(x)
        #kullanıcı bölüm isteniyor mu sorusuna verdiği cevaba göre aşağıdaki bloklar devreye girer. for döngüsünde sayının kendisini ve
        #1 sayısını dahil etmediğimiz için bu bölümde 1 ve sayının kendisini listeye dahil ediyoruz.
        if bolum_isteniyor_mu=="+": #kullanıcı + verirse bu blok devreye girer.
            bolum_listesi.append(1) #1 tüm sayıların böleni olduğu için burada listeye ekleniyor.
            bolum_listesi.append(sayi)  #sayının kendisi de bir bölen olduğu için listeye ekleniyor
            bolum_listesi.sort()    #listedeki sayıları küçükten büyüğe sıralamak için bu methotu kullanırız
            uyari1=f"{sayi} değerinin bölenleri:"   
            a=len(uyari1)*"-"    
            print(a+"\n")
            print(bolum_listesi)
        else:   #kullanıcı + dışında cevap girerse işlem pas geçer
            pass
    
    #sayı eğer bir asal sayı ise, aşağıdaki blok devreye girecek.
    else:
        uyari1=f"\n{sayi} değeri bir asal sayıdır.\n"
        a=len(uyari1)*"-"
        print(a+"\n"+uyari1)
    
    uyari1="İşleme Devam Etmek İstiyor Musunuz?\nEvet:+\nHayır:-\nCevap:"
    x=input(len("İşleme Devam Etmek İstiyor Musunuz?")*"-"+"\n"+uyari1)
    if x=="+":
        uyari1="İşleme devam edebilirsiniz."
        bolum_listesi=[]    #bir sonraki işlem için bolum listesi ni boşaltmamız gerekmekte. 
        a=len(uyari1)*"-"
        print(a+"\n"+uyari1)
        continue
    elif x=="-":
        print(cikis_mesaji)
        break
    else:
        uyari1="Yanlış bir cevap girdiniz. Lütfen Tekrar deneyin."
        a=len(uyari1)*"-"
        print(a+"\n"+uyari1)
        uyari1="İşleme Devam Etmek İstiyor Musunuz?\nEvet:+\nHayır:-\nCevap:"
        x=input(len("İşleme Devam Etmek İstiyor Musunuz?")*"-"+"\n"+uyari1)
        if x=="+":
            bolum_listesi=[]    #bir sonraki işlem için bolum listesi ni boşaltmamız gerekmekte. 
            uyari11="İşleme devam edebilirsiniz."
            a=len(uyari1)*"-"
            print(a+"\n"+uyari1)
            continue
        elif x=="-":
            print(cikis_mesaji)
            break
        else:
            uyari1="Yanlış bir cevap girdiniz.İşlem sonlanmıştır."
            a=len(uyari1)*"-"
            print(a+"\n"+cikis_mesaji)
            break


