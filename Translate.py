from textblob import TextBlob
import os

def clear():
    os.system('cls||clear')
print("\\\\\\\\\\\\\\\\\\\\")
print("-NOT: Program girilen kelimeyi düzgün bir şekilde çevirdiyse bulunduğu\n dizine bir metin belgesi açarak, çevirilen kelimeleri oraya kaydeder.")
print("-NOT2: Programdan çıkmak için 'exit' , ekranı temizlemek için 'clear' yazınız.'")
print("-Developer: Enes Uysal")
print("//////////\n")
def ceviri():
    print("--------------TÜRKÇE / İNGİLİZCE ÇEVİRİ UYGULAMASI--------------")
    print("-Türkçe'den İngilizce'ye çevirmek için '1' yazınız.")
    print("-İngilizce'den Türkçe'ye çevirmek için '2' yazınız.")
    secenek = input("-Seçim Yapınız: ")
    if secenek == "exit":
        exit()
    elif secenek == "1":
        while secenek == "1":
            try:
                girilen = input('-Metin Giriniz: ')
                if girilen == "exit":
                    break
                elif girilen == "clear":
                    clear()
                    continue
                girilen2 = girilen.capitalize()
                text = TextBlob(girilen2)
                text.detect_language()
                cevirilen = text.translate(to="en")
                yazdir = "{} = {}\n".format(girilen2,cevirilen)
                kaydet = "{} = {}\n".format(cevirilen,girilen2)
                print("\\\\\\\\\\\\\\\\\\\\")
                print(yazdir,end="")
                print("//////////")
                with open("Kelimeler.txt","a", encoding="utf-8") as kelimeler:
                    kelimeler.write(kaydet)
            except:
                print("-Yanlış metin girdiniz tekrar deneyin !")
    elif secenek == "2":
        while secenek == "2":
            try:
                girilen = input('-Metin Giriniz: ')
                if girilen == "exit":
                    break
                elif girilen == "clear":
                    clear()
                    continue
                girilen2 = girilen.capitalize()
                text = TextBlob(girilen2)
                text.detect_language()
                cevirilen = text.translate(to="tr")
                yazdir = "{} = {}\n".format(girilen2,cevirilen)
                kaydet = "{} = {}\n".format(cevirilen,girilen2)
                print("\\\\\\\\\\\\\\\\\\\\")
                print(yazdir,end="")
                print("//////////")
                with open("kelimeler.txt","a", encoding="utf-8") as kelimeler:
                    kelimeler.write(kaydet)
            except:
                print("-Yanlış metin girdiniz tekrar deneyin !")
    else:
        clear()
        print("-Yanlış seçim yaptınız lütfen '1' veya '2' yazınız. !!!") 
        return "return"
while ceviri() == "return":
    ceviri()           
   