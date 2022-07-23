# Global-AI-Hub-Project-1

## Proje Hakkında
 Kullanıcı tarafından verilen öğrencilerin ders notlarını hesaplayan ve sonuçları pandas yardımıyla excel tablosu oluşturan uygulama.

## Proje içindeki dosyalar
* Student : Öğrenci class'ı öğrencinin adı soyadı , ve sınırsız not değerlerinin ortalamasını tutar.
* Lecture : Öğrencinin aldığı derslerin sınıfı, ders adı(sabit enum) ve notları (sınırsız) tutar.
* Grade : Gerekli fonksiyonların tutulduğu standard py dosyası.
* Main : Kullanıcı tarafından kolayca ulaşılması için ayrıca ayrılmış kısım.

##  Uygulamanın akışı

* Kullanıcının verdiği öğrenci listesini okur.
* Kullanıcı yazılacak dosyanın adını verir.
* grade_students fonksyonuna gerekli değerler girilir : öğrenci listesi , dosya yazma modu , encoding/harf modu
* Pandas yardımıyla oluşturalacak excel dosyası için Sütun değerli listesi girilir.
create_pandas_dataframe fonksiyonu sayesinde excel dosyası elde edilir.

