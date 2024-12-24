while True:
    N = int(input())
    if N == 0:
        break
    
    numbers = list(map(int, input().split()))
    
    unique_number = 0
    for num in numbers:
        unique_number ^= num
    
    print(unique_number)