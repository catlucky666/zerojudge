def counts(n , m , list1 , list2):
    count = 0
    i = j = 0
    while i < m and j < m:
        if list1[i] == list2[j]:
            count = count + 1
            i = i + 1
            j = j + 1
        elif list1[i] < list2[j]:
            i = i + 1
        else:
            j = j + 1       
    return count
n, m = map(int , input().split())
for k in range(n):
    list1 = list(map(int , input().split()))
    list2 = list(map(int , input().split()))
    result = counts(n , m , list1 , list2)
    print(result)