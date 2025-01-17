n = int(input())
books = []
for i in range(n):
    x_num, y_day = map(int, input().split())
    books.append((x_num , y_day))

overdue_books = []
total_penalty = 0
for book in books:
    x_num, y_day = book
    if y_day > 100:
        penalty = (y_day - 100) * 5
        overdue_books.append(x_num)
        total_penalty += penalty

if len(overdue_books) > 0:
    sorted_books = sorted(overdue_books)
    str_books = map(str, sorted_books)
    overdue_books_str = " ".join(str_books)
    print(overdue_books_str)
    print(total_penalty)
else:
    print(0)