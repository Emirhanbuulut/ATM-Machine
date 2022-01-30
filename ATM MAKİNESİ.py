print("""*****************************
ATM MAKİNESİNE HOŞGELDİNİZ

İŞLEMLER:

1.BAKİYE SORGLAMA

2.PARA YATIRMA

3.PARA ÇEKME

Programdan çıkmak için 'q' ya yasınız
***********************************""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz")
    if(işlem == "q"):
        print("Yine bekleriz")
        break
    elif(işlem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktarı giriniz:"))
        bakiye += miktar


    elif (işlem == "3"):
        miktar = int(input("Miktarı giriniz:"))
        if(bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsiniz...")
            continue #Bundan sonra döngümü sonlandırıp en başa götürmek istiyorum bunu da continiue ile yapabiliriz
        bakiye -= miktar

    else:
        print("geçersiz işlem...")











