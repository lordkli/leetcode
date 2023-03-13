def replaceElements(arr: list[int]) -> list[int]:
    
    #! explain the approach
    # arr = [17,18,5,4,6,1]
    # soldan gelmek maliyetli olur ondan dolayi sagdan yaklasim daha verimli
    # 1. bir tane array olustur -1 value icinde
    # 2. bir tane dummy max value olustur
    # 3. her bir degeri dummy max value ile kiyasla, hangisi buyukse onu max value'ye ata
    # 4. max value'yu array'e append et.
    # 4.2 son degeri sil
    # 5. arrayi ters cevir
    
    #! code in increments
    
    rvrs_arr = [-1]
    max_val = 0
    
    for num in arr[::-1]:
        if max_val < num:
            max_val = num
        rvrs_arr.append(max_val)
    rvrs_arr.pop()
    return rvrs_arr[::-1]


#! check for possible optimizations

print(replaceElements([17,18,5,4,6,1]))