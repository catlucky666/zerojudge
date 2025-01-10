def dis_price(price, stra):
    if stra == 0:  
        dis = (price // 2000) * 200
    else:  
        dis = (price // 1000) * 100
    return price - dis
def store(price):
    dis_prices = [dis_price(price, 0), dis_price(price, 1)]
    min_price = min(dis_prices)
    if dis_prices[0] == dis_prices[1]:
        return min_price, 0
    else:
        return min_price, dis_prices.index(min_price)
price = int(input().strip())
dis_price, store_choice = store(price)
print(dis_price, store_choice)