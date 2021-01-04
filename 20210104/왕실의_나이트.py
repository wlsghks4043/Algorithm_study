# 현재 나이트의 위치 입력 받기
input_data = input()
row = input_data[1]
column = int(ord(input_data[0])) - int(ord('a')) + 1


# 나이트가 이동할 수 있는 경우의 수
steps= [(-2,1), (-2,-1), (2, 1), (2, -1), (1, 2), (1,-2), (-1, 2), (1, -2)]

# 조건에 맞는 경우의 수 이동
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    # 조건에 맞는지 확인
    if next_row >=1 and next_column >=1 and next_row <=8 and next_column <=8:
        result += 1
        
print(result)
