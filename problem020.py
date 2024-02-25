#(def fac(n):
    # 재귀함수 recursive function
    #if n != 0:
        #return(n * fac(n - 1))
    #return 1)


def fac2(n):
    result = 1
    for number in range(1, n+1):
        result *= number
    return result

answer = fac2(100)

def each_num(num):
    a = []
    for each_num in str(num):
        a.append(int(each_num))
    return(a)

a = each_num(answer)
rresult = sum(a)
print(rresult)