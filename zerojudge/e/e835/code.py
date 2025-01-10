def seat_loc(seat_num):
    if seat_num <= 2500:
        a = 1
        row = (seat_num - 1) // 25 + 1
        loc = (seat_num - 1) % 25 + 1
    elif seat_num <= 7500:
        a = 2
        row = (seat_num - 2501) // 50 + 1
        loc = (seat_num - 2501) % 50 + 1
    else:
        a = 3
        row = (seat_num - 7501) // 25 + 1
        loc = (seat_num - 7501) % 25 + 1
    return a , row , loc
seat_num = int(input())
a , row, loc = seat_loc(seat_num)
print(a, row, loc)