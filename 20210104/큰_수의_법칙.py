# N, M, K 공백으로 구분해서 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분해서 리스트로 입력받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 데이터 리스트 정렬
first = data[n-1] # 가장 큰 수 
second = data[n-2] # 두 번째로 큰수

count = int(m // k)*k # 가장 큰 수가 더해지는 횟수

result = 0
result += count*first # 가장 큰 수 더하기

result += (m-count)*second #두 번째로 큰 수 더하기

print(result)
