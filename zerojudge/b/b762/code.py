n = int(input())
K = D = A = kc = 0
for _ in range(n):
    act = input().strip()
    if act == "Get_Kill":
        K += 1
        kc += 1
        if kc == 3:
            print("KILLING SPREE!")
        elif kc == 4:
            print("RAMPAGE~")
        elif kc == 5:
            print("UNSTOPPABLE!")
        elif kc == 6:
            print("DOMINATING!")
        elif kc == 7:
            print("GUALIKE!")
        elif kc >= 8:
            print("LEGENDARY!")
        else:
            print("You have slain an enemie.")
    elif act == "Get_Assist":
        A += 1
    elif act == "Die":
        D += 1
        if kc >= 3:
            print("SHUTDOWN.")
        else:
            print("You have been slained.")
        kc = 0
print(f"{K}/{D}/{A}")