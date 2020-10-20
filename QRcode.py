#Python ile QR code oluşturmak.
#Alperen T.
import qrcode #Öncelikle QR CODE oluşturmak için gerekli kütüphanemizi kuruyoruz.
import time #time işte yani
from colorama import init #Renk kütüphanesi
from colorama import Fore, Back, Style #Renk kütüphanesinin içindeki modüller
init()
# qr code un tipini yani büyüklüğünü,versiyonunu,kutu alanını giriyoruz.
qr = qrcode.QRCode( #qrcode un verilerini giriyoruz
    version = 1, #kütüphanenin versiyonu
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10, #kaplama alanı boyutu
    border = 4,
)
#Karde kodu oluştururken içine bişey giremiliyiz o yüzden veri değişkenini kulanıcaz.
print(Fore.WHITE) #Beyaz rengi seçiyoruz.
veri = input("Lütfen Kare Kodun içine girecek veriyi yazın ->") #İstediğimiz veriyi soru şeklinde koyuyoruz.
print(Fore.GREEN) #Yeşil renk
print("Veri qrcode a yazıldı!") #Herşey düzgün gittiğini göstermek için bir yazı
time.sleep(0.5) #Kullanıcının yazıyı okuması için süre.
print(Fore.WHITE) #Tekrardan Beyaz renge geçiş
# Veriyi kare kodun içine ekliyoruz.
qr.add_data(veri) #add_data komutunu kullanarak veri değişkenini qr coda ekliyorz.
qr.make(fit=True) #QRcode kütüphanesini kullanarak aldığımız verileri qrcoda dönüştürüyoruz.

# QR code u görüntü dosyasına dönüştürlemiyiz.
görüntü = qr.make_image() #Görüntü değişkeninin içine oluşturduğumuz resmi atıyoruz.

#Şimdi oluşturduğumuz görüntü dosyası için mantıken bir kayıt biçimi lazım.
#Çünkü programın olduğu klasöre bu qrcode u resim olarak kaydedecez.

kayitbicim = input("Lütfen kayıt biçimini yazın -> -Örn : .png- ->") #Hangi kayıt biçimini istediğini kullanıcıya soruyoruz.
print(Fore.GREEN) #Yeşil renk
print("Kayıt biçimi Başarılı") #Herşey düzgün gittiğini göstermek için bir yazı
time.sleep(0.5) #Kullanıcının yazıyı okuması için süre.
print(Fore.WHITE) #Tekrardan Beyaz renge geçiş
#Ve onu bir değişkene atıyoruzki daha rahat kullanalım.
isim = input("QR code ismi ne olsun -->") #Burda ise hangi isim ile kaydetmesini istediğini soruyoruz ki böylece birden
print(Fore.GREEN) #Yeşil renk
print("İsim koyma başarılı!") #Herşey düzgün gittiğini göstermek için bir yazı
time.sleep(0.5) #Kullanıcının yazıyı okuması için süre.
print(Fore.WHITE) #Tekrardan Beyaz renge geçiş
#fazla dosyada sorun çıkmasın. Bu qrcode ları ayrıştırabilsin.
görüntü.save(isim+kayitbicim) #Burda ise kullanıcının istediği veriler ile qr code muzu oluşturuyoruz.
print(Fore.CYAN)
print(Style.DIM)
print("QR CODE OLUŞTURULDU!")
time.sleep(5)
print("Görüsürüz")
time.sleep(1) #Alperen T.