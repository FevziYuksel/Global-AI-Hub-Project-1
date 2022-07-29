# Global AI Hub Project 1

## 📖 Hakkında

Kullanıcı tarafından verilen öğrencilerin ders notlarını hesaplayan ve sonuçları pandas yardımıyla excel tablosu oluşturan uygulama.
 
## ☑️ İstenenler
Bu projede bir öğrenci not sistemi oluşturacaksınız. Sizden istenilenler:
Kendinize bir ders belirleyiniz. (Matematik,Fizik, Lineer Cebir vb.) Not aralığınızı oluşturunuz (100-80 ⇒ A, 79-70 ⇒ B vb.) Öğrenci Bilgilerini (Ad, Soyad, Okul No, sınav puanı) girebileceğiniz ve bu bilgilerin tutulabileceği bir sistem oluşturunuz. Girilen bilgilerden yola çıkarak öğrencinin dersi geçip geçmediğini göstermesi gerekmektedir. Öğrenci dersi geçti ise öğrencinin bilgilerinin tutulduğu alana “Geçti” yazısı, öğrenci dersi geçemedi ise “kaldı” yazısını göstermesi gerekmektedir. Notları girilen öğrencilerden dersi geçenleri ve geçmeyenleri gösteren bir Dataframe oluşturunuz. Oluşturulan Dataframe’i Excel tablosuna dönüştürünüz.

## 📂 Dosyalar/Dizinler
* Student : Öğrenci class'ı öğrencinin adı soyadı , ve sınırsız not değerlerinin ortalamasını tutar.
* Lecture : Öğrencinin aldığı derslerin sınıfı, ders adı(sabit enum) ve notları (sınırsız) tutar.
* Grade : Gerekli fonksiyonların tutulduğu standard py dosyası.
* Main : Kullanıcı tarafından kolayca ulaşılması için ayrıca ayrılmış kısım.

## ⤵️ Workflow
> Kullanıcının verdiği öğrenci listesini okur.
```python
student_list = 
[
  Student("Fevzi Yüksel", 723, Lecture(1, 70, 80), Lecture(2, 55, 100), Lecture(3, 54, 63)),
  Student("İrfan Bayrak", 547, Lecture(1, 90, 20), Lecture(2, 57, 87), Lecture(3, 47, 65)),
  Student("Tuğbanur Balcı", 848, Lecture(1, 100, 100), Lecture(2, 90, 60), Lecture(3, 40, 30)),
  Student("Efsane Kaplan", 800, Lecture(1, 70, 60), Lecture(2, 66, 65), Lecture(3, 48, 70)),
]
```

> Kullanıcı yazılacak dosyanın adını verir.
```python
# Assigning global/static variables from another file
With_Classes.Grade.file_address = "grades.txt"
```

> grade_students fonksyonuna gerekli değerler girilir : öğrenci listesi , dosya yazma modu , encoding/harf modu
Pandas yardımıyla oluşturalacak excel dosyası için Sütun değerli listesi girilir.
```python
columns = ["Student Name", "Student Surname", "Student Number", "Lecture Name", "Numeric Grade", "Letter Grade", "Status"]
```

> create_pandas_dataframe fonksiyonu sayesinde excel dosyası elde edilir.
```python
# python support default and random order parameters
create_pandas_dataframe(header=None, sep=",", columns=columns, excel_address="Grades.xlsx")
```

## 📚 Paketler/Kütüphaneler
* Pandas
* pythonlangutil
* metaclass
* openpyxl
* enum
* typing

## 💽 Kaynaklar
* Global AI Hub [^1] [^2]
* StackOverflow [^3] [^4]
* GeeksforGeeks [^5]
* Python Docs [^6]
* Pandas [^7]

[^1]: [Introduction to python](https://globalaihub.com/courses/introduction-to-python/)
[^2]: [The road to machine learning](https://globalaihub.com/courses/introduction-to-python-the-road-to-machine-learning/)
[^3]: [How can I represent an 'Enum' in Python?](https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python)
[^4]: [What's the pythonic way to use getters and setters?](https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters)
[^5]: [Python Programming Language](https://www.geeksforgeeks.org/python-programming-language/?ref=lbp)
[^6]: [Python3 Documentation](https://docs.python.org/3)
[^7]: [Pandas Library](https://pandas.pydata.org/)
