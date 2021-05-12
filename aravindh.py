N = int(input())
input_array = []
for i in range(0,N):
    num = int(input())
    input_array.append(num)
print("Answer=", len(set(input_array)))