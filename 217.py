def containsDuplicate(nums: list[int]) -> bool:
    setim = set()
    for i in nums:
        if i in setim:
            return True
        setim.add(i)
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))


def tekrarli_mi(liste):
    for eleman in liste:
        if liste.count(eleman) > 1:
            return True
    return False

print(tekrarli_mi([1,2,3,1]))
print(tekrarli_mi([1,2,3,4]))

def tekrarli_mi2(liste):
    sıralı_liste = sorted(liste)
    for i in range(len(sıralı_liste)-1):
        if sıralı_liste[i] == sıralı_liste[i+1]:
            return True
    return False

print(tekrarli_mi2([1,2,3,1]))
print(tekrarli_mi2([1,2,3,4]))