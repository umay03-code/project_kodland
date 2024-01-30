from flask import Flask
from main import pas
import random
import os

#Şifre oluşturucu
#Rastgele bir resim gösterme

app = Flask(__name__)

facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar."
              , "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor."
              , "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."
              , "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."
              , "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır."
              , "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor."
              , "Elon Musk sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor."
              , "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]

head_tail = ["yazı","tura"]

dice = ["1","2","3","4","5","6"]

#listede resim sayısı kadar sayı olmasını nasıl sağlarım?
images_list= ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png","11.png","12.png","13.png"]
img_name = random.choice(os.listdir('images3'))

image_path = os.path.join("images3", random.choice(img_name))

#@app.route("/")
#def addiction():
#    return f"<h1>Teknoloji Bağımlılığı</h1> \n <p>{random.choice(facts_list)}</p>"


#yazıların görünüşleri ve sitenin görünüşünü değiştir, linklerin renkleri ve linkler arası boşluklar nasıl ayarlanacak?
@app.route("/")
def index():
    return f"<h1>MERHABA! Bu sayfada, teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!</h1> <br> <a href='/rastgele_gercek'>Rastgele bir gerçeği görüntüle!</a> <br> <a href='/yazi_tura'>yazı tura makinesi.</a> <br> <a href='/zar'>zar at.</a> <br> <a href='/rastgele_resim'>teknoloji bağımlılığı hakkında rastgele bir resim görmek istiyorum!</a> <br> <a href='/sifre'>rastgele şifre oluşturucu.</a>" 

@app.route("/rastgele_gercek")
def facts():
    return f"<p>{random.choice(facts_list)}</p>"

@app.route("/yazi_tura")
def ht():
    return f"<p>{random.choice(head_tail)}</p>"
#zar veya madeni para animasyonuyla beraber bir işlemi nasıl yaratabilirim?
@app.route("/zar")
def dc():
    return f"<p>{random.choice(dice)}</p>"

#dosyadan rastgele resimleri nasıl sitede göstertirim? (images3 klasöründen)
@app.route("/rastgele_resim")
def imgs():
    return f"<img src={image_path}>"
    #return f"<img src='vscodeprojects1/images3/{str(random.choice(img_name))}'>" 

#kullanıcıdan şifre uzunluğu veya kullanılacak karakterleri nasıl isterim? 
#şifrenin art arda aynı karakterler kullanmasının önüne geçilebilir mi?
#nasıl eşsiz şifreler oluşturulabilir? (kullanılamayacaklar listesi oluşturup her üretilen şifreyi listeye ekleyip gerektiğinde şifrenin karakter sayısını arttırmak gibi bir şeyi nasıl yapacağım?)
@app.route("/sifre")
def pasw():
    #number = int(input("şifre kaç karakter olsun?"))
    return f"<p>{pas(12)}</p>"

app.run(debug=True)