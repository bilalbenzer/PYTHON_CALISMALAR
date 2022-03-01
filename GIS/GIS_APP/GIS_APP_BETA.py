welcome_message = """
------------------------------------    -    -------------------------------------
--- CBS UYGULAMAMIZA HOŞGELDİNİZ ---    -    --- WELCOME TO MY GIS APPLICATION ---
------------------------------------    -    -------------------------------------


"""
exit_message = """
-----------------------------------------------------------    -    --------------------------------------
--- CBS UYGULAMAMIZI KULLANDIĞINIZ İÇİN TEŞEKKÜR EDERİZ ---    -    --- THANK YOU FOR USING MY GIS APP ---  
-----------------------------------------------------------    -    --------------------------------------
"""

function_types = """
***SESLİ KONUŞMA ETKİN DEĞİL. SESLİ KONUŞMAYI KULLANMAK İÇİN 1 DİYEBİLİRSİNİZ***
***VOICE TALK IS NOT ACTIVE. YOU CAN SAY 1 TO USE VOICE TALK***

------------------------------------------------------------------------------------------------------------------------------------

1- Nokta Objesi Oluşturma / Create Point Object
2- Çoklu Nokta Objesi Oluşturma / Create Multipoint Object

"""
print(welcome_message)
print(function_types)
ara_satir_cizgi = "\n------------------------------------------------------------------------------------------------------------------------------------\n"

while True:
    try:
        voice__command = input("Sesli Komut Kullanmak İstiyor Musunuz?\nDo You Want to Use Voice Command?\nEvet/Yes:1\nHayır/No:2\nCevap/Answer:")
        print(ara_satir_cizgi)
        if voice__command=="1":
            ###
            try:
                from my_classes import settings, listen_to_voice_command
                voice_command_open_close = "Open"
                b = settings(voice_command_open_close)
                a = listen_to_voice_command(b)
                a.listen()
                ###
                command1=a.text
                words = ["1.1","1.1-","nokta oluşturma","nokta oluşturmak istiyorum","nokta oluştur"]
                print(f"Cevap:{command1}")
                print(ara_satir_cizgi)
                if words.count(command1) >= 1:
                    pass
                else:
                    print("Durdu\nStopped","\n",exit_message)
                    print(ara_satir_cizgi)
                    break
            except AttributeError as error:
                pass
        elif voice__command=="2":
            from my_classes import settings, listen_to_voice_command
            voice_command_open_close = "Close"
            b = settings(voice_command_open_close)
            a = listen_to_voice_command(b)
            print("Lütfen bir işlem türü seçiniz.Çıkış yapmak için 0 diyebilirsiniz.\nPlease select a transaction type. You can select 0 to log out.\nCevap/Answer:")
            print(ara_satir_cizgi)
            selection =input(":")         
            if selection =="1":
                pass
            elif selection=="2":
                pass
            elif selection=="0":
                print("Program Sonlanmıştır.\nProgram Ended\n",exit_message)
                print(ara_satir_cizgi)
                break
    except KeyboardInterrupt as error:
        print("Hata Metni / Error Text",error,"\nİşlem iptal edilmiştir.\n",exit_message)
        print(ara_satir_cizgi)

    
    

