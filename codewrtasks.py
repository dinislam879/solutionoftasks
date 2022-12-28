def find_sum(num, x):
    total = 0
    res = num
    for i in range(2,x+1):
        res = res * num
    res = str(res)
    for i in res:
        total += int(i)
    
    return total

print(find_sum(2, 1000))



