a , b = map(int,input().split())
start = min(a , b);
end = max(a , b);
start += start % 2;
even = (end - start) / 2 + 1;
print(int(even))