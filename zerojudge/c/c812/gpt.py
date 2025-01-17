def count_related_sites(n, vk, q, edges):
    from collections import defaultdict, deque

    # 构建邻接表
    graph = defaultdict(list)
    for i, j, r in edges:
        graph[i].append((j, r))
        graph[j].append((i, r))

    # 使用 BFS 遍历
    visited = [False] * (n + 1)
    queue = deque([vk])
    visited[vk] = True
    count = 0

    while queue:
        node = queue.popleft()
        for neighbor, weight in graph[node]:
            if not visited[neighbor] and weight >= q:
                count += 1
                visited[neighbor] = True
                queue.append(neighbor)

    return count

# 主程序
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # 解析第一行
    n, vk, q = map(int, data[0].split())
    
    # 解析后续行
    edges = [tuple(map(int, line.split())) for line in data[1:]]
    
    # 特殊情况处理
    if n == 1:
        # 只有一个点，不会有其他相关点
        print(0)
    else:
        # 调用函数并输出结果
        print(count_related_sites(n, vk, q, edges))