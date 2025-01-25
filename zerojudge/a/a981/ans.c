#include <stdio.h>
int n, m, arr[31], step[31] = {}, check[31] = {}, no_solution = 1;
void dfs(int now, int sum) {
    if (now == n) {
        if (sum == m) {
            int test = 0;
            for (int i = 0; i < n; i++) {
                if (check[i] != 0) {
                    if (test == 1)
                        printf(" ");
                    printf("%d", arr[i]);
                    test = 1;
                }
            }
            printf("\n");
            no_solution = 0;
        }
        return;
    }
    if (sum > m) /*若sum已經大於m，為不合法的可能，可以直接返回*/
        return;
    check[now] = 1; /*選取該數字*/
    dfs(now + 1, sum + arr[now]); /*將sum加上該數字後進入下一項的討論*/
    check[now] = 0; /*不選該數字*/
    dfs(now + 1, sum); /*直接進入下一項的討論*/
}
int main() {
    while (scanf("%d%d", &n, &m) != EOF) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &arr[i]);
            sum += arr[i];
        }
        if (sum < m) {
            printf("-1\n");
            continue;
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] > arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        dfs(0, 0);
        if (no_solution == 1)
            printf("-1\n");
        no_solution = 1;
    }
    return 0;
}