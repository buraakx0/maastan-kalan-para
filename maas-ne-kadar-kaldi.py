maas = float(input("Lütfen aldığınız maaş miktarını giriniz: "))
mutfak = float(input("Lütfen market alışveriş tutarını giriniz: "))
tel = float(input("Telefon fatura fiyatını giriniz: "))
tel2 = float(input("Eğer 2. telefon fatura varsa giriniz. (yoksa 0 yazın): "))
su = float(input("Bu ay su faturası ne kadar geldiyse yazın: "))
gaz = float(input("Bu ay doğalgaz faturası ne kadar geldiyse yazın: "))
elektrik = float(input("Bu ay elektrik faturası ne kadar geldiyse yazın: "))
int = float(input("İnternet faturası ne kadarsa yazın: "))
kira = float(input("Kiraya ne kadar ödüyorsanız yazın (eğer ödemiyorsanız 0 yazın): "))
taksit = float(input("Eğer ödemekte olduğunuz herhangi bir taksit varsa onun aylık ödeme miktarını yazın. (yoksa 0 yazın)"))
ekstra = float(input("Eğer ekstradan bir gideriniz varsa buraya yazınız. (eğer yoksa 0 yazın)"))

toplam = tel + tel2 + su + gaz + elektrik + int + kira + taksit + ekstra + mutfak

ed = maas - toplam

print("Bu ayki toplam harcamanız:",toplam)
print("Bütün masraflar çıktıktan sonra maaşınızdan kalan miktar:",ed)

# python maas-ne-kadar-kaldi.py 