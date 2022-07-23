# Global-AI-Hub-Project-1

## Proje Hakkında
 Kullanıcı tarafından verilen öğrencilerin ders notlarını hesaplayan ve sonuçları pandas yardımıyla excel tablosu oluşturan uygulama.
 
## Projede istenenler

Bu projede bir öğrenci not sistemi oluşturacaksınız. Sizden istenilenler:
Kendinize bir ders belirleyiniz. (Matematik,Fizik, Lineer Cebir vb.) Not aralığınızı oluşturunuz (100-80 ⇒ A, 79-70 ⇒ B vb.) Öğrenci Bilgilerini (Ad, Soyad, Okul No, sınav puanı) girebileceğiniz ve bu bilgilerin tutulabileceği bir sistem oluşturunuz. Girilen bilgilerden yola çıkarak öğrencinin dersi geçip geçmediğini göstermesi gerekmektedir. Öğrenci dersi geçti ise öğrencinin bilgilerinin tutulduğu alana “Geçti” yazısı, öğrenci dersi geçemedi ise “kaldı” yazısını göstermesi gerekmektedir. Notları girilen öğrencilerden dersi geçenleri ve geçmeyenleri gösteren bir Dataframe oluşturunuz. Oluşturulan Dataframe’i Excel tablosuna dönüştürünüz.

## Proje içindeki dosyalar
* Student : Öğrenci class'ı öğrencinin adı soyadı , ve sınırsız not değerlerinin ortalamasını tutar.
* Lecture : Öğrencinin aldığı derslerin sınıfı, ders adı(sabit enum) ve notları (sınırsız) tutar.
* Grade : Gerekli fonksiyonların tutulduğu standard py dosyası.
* Main : Kullanıcı tarafından kolayca ulaşılması için ayrıca ayrılmış kısım.


##  Uygulamanın akışı

Kullanıcının verdiği öğrenci listesini okur.
 ![image](https://user-images.githubusercontent.com/93267352/180608235-f76cda1e-7905-4401-aef7-0b114728fa93.png)

Kullanıcı yazılacak dosyanın adını verir.

 ![image](https://user-images.githubusercontent.com/93267352/180608254-73127ec1-1ec7-44c0-984e-4f173cebb23b.png)

grade_students fonksyonuna gerekli değerler girilir : öğrenci listesi , dosya yazma modu , encoding/harf modu
 ![image](https://user-images.githubusercontent.com/93267352/180608260-ca70be02-d7d1-4e16-857e-9346cf930759.png)

Pandas yardımıyla oluşturalacak excel dosyası için Sütun değerli listesi girilir.
 ![image](https://user-images.githubusercontent.com/93267352/180608286-99d6cc85-c096-404b-9d95-84b158f7fd89.png)

create_pandas_dataframe fonksiyonu sayesinde excel dosyası elde edilir.
 ![image](https://user-images.githubusercontent.com/93267352/180608297-234e48c0-9bd6-4ab1-8b9a-35783a015c4d.png)


## Kullanılan paketler/Kütüphaneler

* Pandas
* pythonlangutil
* metaclass
* openpyxl
* enum
* typing

## Kullanılan kaynaklar
* https://globalaihub.com/courses/introduction-to-python/
* https://globalaihub.com/courses/introduction-to-python-the-road-to-machine-learning/
* StackOverFlow
* https://www.geeksforgeeks.org/python-programming-language/?ref=lbp
* https://docs.python.org/3/
* https://pandas.pydata.org/


