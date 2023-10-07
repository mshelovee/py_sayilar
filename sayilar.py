#KLAVYEDEN GİRİLEN İKİ SAYININ ARASINDAKİ SAYILARI TOPLAMAK
sayi1=int(input("birinci sayıyı giriniz: "))
sayi2=int(input("ikinci sayıyı giriniz: "))
toplam=0 #toplamda etkisiz 0
for sayi in range(sayi1 , (sayi2+1)):
    toplam=toplam+sayi
print("TOPLAM= ", toplam)