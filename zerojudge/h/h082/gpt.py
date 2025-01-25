def tournament(n, m, S, T, x):
    # 初始每个人的失败次数
    losses = [0] * n
    
    # 当前参赛者的顺序
    contestants = x[:]
    
    while len(contestants) > 1:
        # 记录新的胜利者和失败者
        winners = []
        losers = []
        
        # 处理两两配对
        i = 0
        while i < len(contestants) - 1:
            a_idx = contestants[i] - 1  # 编号转为索引
            b_idx = contestants[i + 1] - 1
            
            a, b = S[a_idx], T[a_idx]
            c, d = S[b_idx], T[b_idx]
            
            if a * b >= c * d:  # 第一个人获胜
                S[a_idx] = a + (c * d) // (2 * b)
                T[a_idx] = b + (c * d) // (2 * a)
                S[b_idx] = (3 * c) // 2
                T[b_idx] = (3 * d) // 2
                winners.append(contestants[i])
                losers.append(contestants[i + 1])
            else:  # 第二个人获胜
                S[b_idx] = c + (a * b) // (2 * d)
                T[b_idx] = d + (a * b) // (2 * c)
                S[a_idx] = (3 * a) // 2
                T[a_idx] = (3 * b) // 2
                winners.append(contestants[i + 1])
                losers.append(contestants[i])
            
            i += 2
        
        # 如果有奇数人，最后一个人自动晋级
        if len(contestants) % 2 == 1:
            winners.append(contestants[-1])
        
        # 更新失败次数
        for loser in losers:
            loser_idx = loser - 1
            losses[loser_idx] += 1
        
        # 下一轮参赛者：胜者 + 未淘汰的失败者
        next_round = winners + [loser for loser in losers if losses[loser - 1] < m]
        
        # 重新生成参赛者列表
        contestants = next_round
    
    # 返回最后剩下的人的编号
    return contestants[0]

# 读取输入
n, m = map(int, input().split())
S = list(map(int, input().split()))  # 战力
T = list(map(int, input().split()))  # 应变力
x = list(map(int, input().split()))  # 初始排列顺序

# 输出最终获胜者的编号
print(tournament(n, m, S, T, x))