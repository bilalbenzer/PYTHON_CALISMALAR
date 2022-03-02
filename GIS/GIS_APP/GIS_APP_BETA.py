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

while True:
    language_choice = input("Lütfen Dil Seçiniz.\nPlease Select Language.\nTürkçe: tr\nEnglish: en\nProgram Çıkış Yapmak İçin 0'ı Tuşlayabilirsiniz.\nYou can press 0 to exit the program.\n:")
    if language_choice=="0":
        print("Program Sonlandı.\nProgram Terminated",exit_message_tr,ara_satir_cizgi,exit_message_en)
        print(ara_satir_cizgi)
        break
    while True:
        try:
            if language_choice == "tr":
                print("Program dili Türkçe olarak ayarlandı.")
                print(welcome_message_tr)
                voice__command = input("Sesli Komut Kullanmak İstiyor Musunuz?\nEvet:1\nHayır:2\nCevap:")
                print(ara_satir_cizgi)
                if voice__command=="1":
                    try:
                        from my_classes import settings, listen_to_voice_command
                        voice_command_open_close = "Open"
                        b = settings(voice_command_open_close)
                        a = listen_to_voice_command(b)
                        a.listen_tr()
                        ###
                        command1=a.text
                        words = ["1.1","1.1-","nokta oluşturma","nokta oluşturmak istiyorum","nokta oluştur"]
                        print(f"Cevap:{command1}")
                        print(ara_satir_cizgi)
                        if words.count(command1) >= 1:
                            pass
                        else:
                            print("Durdu\nStopped","\n",exit_message_tr)
                            print(ara_satir_cizgi)
                            voice__command="2"
                            pass
                    except AttributeError as error:
                        pass
                elif voice__command=="2":
                    from my_classes import settings, listen_to_voice_command
                    voice_command_open_close = "Close"
                    b = settings(voice_command_open_close)
                    a = listen_to_voice_command(b)
                    print("Lütfen bir işlem türü seçiniz.Çıkış yapmak için 0 diyebilirsiniz.\nCevap:")
                    print(ara_satir_cizgi)
                    selection =input(":")         
                    if selection =="1":
                        pass
                    elif selection=="2":
                        pass
                    elif selection=="0":
                        print("Program Sonlanmıştır.\n",exit_message_tr)
                        print(ara_satir_cizgi)
                        break


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

    

