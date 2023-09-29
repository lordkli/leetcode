# örnek 1
#! 1
from collections import defaultdict

# tanimlamadigin seye 0 i atar ve dicteki gibi .keys() .values() var
names_dict = defaultdict(int)
names_dict["Bob"] = 1
names_dict["Katie"] = 2
names_dict["Sara"]
print(names_dict)
# defaultdict(<class 'int'>, {'Bob': 1, 'Katie': 2, 'Sara': 0})

#! 2
# soru
files = {"Input.txt": "Mert", "Code.py": "Cansu", "Output.txt": "Mert"}

list_dict = defaultdict(list)
list_dict["Mert"].append("Input.txt")
list_dict["Cansu"].append("Code.py")
list_dict["Mert"].append("Output.txt")

print(
    list_dict
)  # defaultdict(<class 'list'>, {'Mert': ['Input.txt', 'Output.txt'], 'Cansu': ['Code.py']})

#! 3
from collections import Counter

# for döngüsüyle saydirmak yerine
lst = [1, 1, 1, 2, 2, 3, 3, 3, 4]
counter = Counter(lst)
print(counter)  # Counter({1: 3, 3: 3, 2: 2, 4: 1})
print(counter.most_common(2))  # [(1, 3), (3, 3)]


#! 4
# sanki bir class olusturmusum gibi özellikleri falan alabiliyoruz
from collections import namedtuple

Person = namedtuple("Kisiler", "isim, yas, meslek")

mert = Person("Mert", 24, "Data Scientist") 
cansu = Person("Cansu", 25, "Project Manager")

print(mert)  # Kisiler(isim='Mert', yas=24, meslek='Data Scientist')
print(cansu)  # Kisiler(isim='Cansu', yas=25, meslek='Project Manager')
print(mert.isim)
print(mert.yas)
print(mert.meslek)

koordinat = namedtuple("Koordinatlar", "x, y")
baslangic_kordinati = koordinat(0, 0)
sonraki_bir_nokta = koordinat(23, 56)
print(baslangic_kordinati)
