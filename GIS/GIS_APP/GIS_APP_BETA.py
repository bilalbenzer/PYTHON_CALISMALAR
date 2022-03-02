welcome_message_tr = """
------------------------------------    -
--- CBS UYGULAMAMIZA HOŞGELDİNİZ ---    -
------------------------------------    -
"""
welcome_message_en = """
-------------------------------------   -
--- WELCOME TO MY GIS APPLICATION ---   -
-------------------------------------   -
"""

exit_message_tr = """
-----------------------------------------------------------    -
--- CBS UYGULAMAMIZI KULLANDIĞINIZ İÇİN TEŞEKKÜR EDERİZ ---    -
-----------------------------------------------------------    -
"""
exit_message_en = """
--------------------------------------    -
--- THANK YOU FOR USING MY GIS APP ---    -
--------------------------------------    -
"""
function_types_tr = """
***SESLİ KONUŞMA ETKİN DEĞİL. SESLİ KONUŞMAYI KULLANMAK İÇİN 1 DİYEBİLİRSİNİZ***

------------------------------------------------------------------------------------------------------------------------------------

1- Nokta Objesi Oluşturma
2- Çoklu Nokta Objesi Oluşturma

"""
function_types_en = """
***VOICE TALK IS NOT ACTIVE. YOU CAN SAY 1 TO USE VOICE TALK***

------------------------------------------------------------------------------------------------------------------------------------

1- Create Point Object
2- Create Multipoint Object

"""
ara_satir_cizgi = "\n------------------------------------------------------------------------------------------------------------------------------------\n"
command1 = ""
while True:
    try:
    #Program başlangıcında dil seçimi yapılacak #Language will be selected at the start of the program
        language_choice = input("Lütfen Dil Seçiniz.\nPlease Select Language.\nTürkçe: tr\nEnglish: en\nProgram Çıkış Yapmak İçin 0'ı Tuşlayabilirsiniz.\nYou can press 0 to exit the program.\n:")
        if language_choice=="0":    #0 girişi yapıldığı zaman program sonlanacak #The program will terminate when 0 is input
            print("Program Sonlandı.\nProgram Terminated",exit_message_tr,ara_satir_cizgi,exit_message_en)
            print(ara_satir_cizgi)
            break
        elif language_choice=="tr" or language_choice=="en":    #tr veya en girişi yapılırsa program başlayacak #If tr ır en are entered, the program will start.
            while True:
                try:
                    if language_choice == "tr": #Çıktılar vs Türkçe olarak program bu blokta çalışacak
                        selected_language = "tr"
                        print("Program dili Türkçe olarak ayarlandı.")
                        print(welcome_message_tr)
                        voice__command = input("Sesli Komut Kullanmak İstiyor Musunuz?\nEvet:1\nHayır:2\nCevap:")   #sesli komutun kullanılıp kullanılmayacağına dair kullanıcıdan giriş istenecek
                        print(ara_satir_cizgi)
                        while True:
                            if voice__command=="1": #kullanıcı 1 cevabını verirse sesli komut aktif edilecek
                                while True:
                                    try:
                                        from create_point_defs import voice_command_use
                                        a=voice_command_use("Open")
                                        words = ["1","bir","1. seçenek","nokta oluşturma","nokta oluşturmak istiyorum","nokta oluştur","nokta oluştu"]   #sesli tanımadan gelen komutun bu listede olup olmadığı kontrol edilecek.
                                                                                                                                    #olası kelimeler bu liste içinde güncellenecek 
                                        print(f"Cevap:{a.command1}")  
                                        print(ara_satir_cizgi)
                                        if words.count(command1) >= 1:  #cevap burada varsa eğer nokta oluşturma modülü çalışacak
                                            from create_point_defs import create_point_with_voice
                                            create_point_with_voice()
                                        else:                           #cevap yoksa eğer kullanıcıya sesli komuta devam edilip edilmeyeceği sorulur
                                            print("Verdiğiniz komut, işlevlerimiz arasında yok. Tekrar deneyiniz.Sesli komutu kapatmak için aşağıda 2 cevabını verebilir veya devam etmek için 1e basabilirsiniz.")
                                            print(ara_satir_cizgi)
                                            voice__command=input(":")   #kullanıcıdan gelen cevaba göre sesli komut kapatılacak ya da açık kalacak. açık kalırsa tekrar denenecek
                                            if voice__command=="1":
                                                continue    #döngü başa saracak ve kullanıcıdan sesli komut istecenek
                                            elif voice__command=="2":   #döngü kırılacak ve klavyeden giriş seçeneğine gidilecek
                                                break
                                            else:
                                                print("Yanlış seçim yapıldı.")  #yanlış seçim yapılırsa döngü kırılacak
                                                print(ara_satir_cizgi)
                                                break
                                    except AttributeError as error: #herhangi bir attribute error da döngü başa saracak
                                        pass
                            elif voice__command=="2":   #If the user answers 1, the voice command will be activated.
                                while True:
                                    try:
                                        from my_classes import settings, listen_to_voice_command    #sesli komut classının import edilmesi
                                        voice_command_open_close = "Close"      #sesli komuta 1 cevabı verdilği için class içinde açık veya kapalı olduğunu belirtiyoruz
                                        b = settings(voice_command_open_close)      #aynı şekilde settings classına da bilgiyi gönderiyoruz
                                        a = listen_to_voice_command(b)      #kapalı veya açık bilgisini sesli komut dinle classına da gönderiyoruz
                                        print("Lütfen bir işlem türü seçiniz.Çıkış yapmak için 0 diyebilirsiniz.\nCevap:")
                                        print(ara_satir_cizgi)
                                        selection =input(":")           #kullanıcıdan seçim alıyoruz
                                        if selection =="1":             
                                            pass
                                        elif selection=="2":
                                            pass
                                        elif selection=="0":
                                            print("Program Sonlanmıştır.\n",exit_message_tr)
                                            print(ara_satir_cizgi)
                                            break
                                        else:
                                            print("Yanlış seçim yapıldı.")  #yanlış seçim yapılırsa döngü kırılacak
                                            print(ara_satir_cizgi)
                                            break
                                    except AttributeError as error: #herhangi bir attribute error da döngü başa saracak
                                        pass

                    elif language_choice=="en":
                        print("Program Language Is Set To English")
                        print(welcome_message_en)
                        try:
                            voice__command = input("Do You Want to Use Voice Command?\nYes:1\nNo:2\nnswer:")
                            print(ara_satir_cizgi)
                            if voice__command=="1":
                                ###
                                try:
                                    from my_classes import settings, listen_to_voice_command
                                    voice_command_open_close = "Open"
                                    b = settings(voice_command_open_close)
                                    a = listen_to_voice_command(b)
                                    a.listen_en()
                                    ###
                                    command1=a.text
                                    words = ["1","create point","make a point","i want to create a point","one"]
                                    print(f"Cevap:{command1}")
                                    print(ara_satir_cizgi)
                                    if words.count(command1) >= 1:
                                        pass
                                    else:
                                        print("Stopped","\n",exit_message_en)
                                        print(ara_satir_cizgi)
                                        break
                                except AttributeError as error:
                                    break
                            elif voice__command=="2":
                                from my_classes import settings, listen_to_voice_command
                                voice_command_open_close = "Close"
                                b = settings(voice_command_open_close)
                                a = listen_to_voice_command(b)
                                print("Please select a transaction type. You can select 0 to log out.\nAnswer:")
                                print(ara_satir_cizgi)
                                selection =input(":")         
                                if selection =="1":
                                    pass
                                elif selection=="2":
                                    pass
                                elif selection=="0":
                                    print("Program Ended\n",exit_message_en)
                                    print(ara_satir_cizgi)
                                    break
                        except KeyboardInterrupt as error:
                            print("Error Text",error,"\nThe program has been canceled.\n",exit_message_en)
                            print(ara_satir_cizgi)
                    else:
                        print("Program Sonlandı.\nProgram Terminated",exit_message_tr,exit_message_en)
                        break
                except KeyboardInterrupt as error:
                    print("Hata Metni/Error Text",error,"\nİşlem iptal edilmiştir./The program has been canceled\n",exit_message_tr,exit_message_en)
                    print(ara_satir_cizgi)
                    break
    except KeyboardInterrupt as error:
        print("Hata Metni/Error Text",error,"\nİşlem iptal edilmiştir./The program has been canceled\n",exit_message_tr,exit_message_en)
        print(ara_satir_cizgi)
        break


