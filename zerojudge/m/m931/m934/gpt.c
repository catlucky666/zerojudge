#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAXN 100

int a[MAXN];
int dp[MAXN][MAXN];
int sum[MAXN];

// 计算区间 [i, j] 的元素和
int range_sum(int i, int j) {
    return sum[j] - (i > 0 ? sum[i - 1] : 0);
}

int min(int x, int y) {
    return x < y ? x : y;
}

int main() {
    int n;
    scanf("%d", &n);

    // 读取数组 a
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    // 预处理前缀和
    sum[0] = a[0];
    for (int i = 1; i < n; i++) {
        sum[i] = sum[i - 1] + a[i];
    }

    // 初始化 dp 数组
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dp[i][j] = (i == j) ? 0 : INT_MAX;  // 自己和自己合并没有花费
        }
    }

    // 枚举区间长度 len，从 2 到 n
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            for (int k = i; k < j; k++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + abs(range_sum(i, k) - range_sum(k + 1, j)));
            }
        }
    }

    // 输出结果
    printf("%d\n", dp[0][n - 1]);

    return 0;
}
