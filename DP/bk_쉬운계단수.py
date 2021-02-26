'''
https://www.acmicpc.net/problem/10844

문제
45656이란 수를 보자.

이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.

세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

입력 
1
출력 
9
입력 2 
2
출력 2 
17
'''
dp = []
dp.append([1 for _ in range(10)])
for _ in range(99):
    dp.append([0 for _ in range(10)])

n = int(input())

for i in range(n):
    for j in range(10):
        if j >= 1:
            dp[i+1][j-1] += dp[i][j]
        if j <= 8:
            dp[i+1][j+1] += dp[i][j]

print((sum(dp[n-1])-dp[n-1][0]) % 1000000000)



'''n = int(input())

dp = [0]*100

dp[1] = 9
dp[2] = 17

for i in range(3, n+1):
    dp[i] = (dp[i-1]-(i-2))*2 + (i-2)

print(dp[n] % 1000000000)'''