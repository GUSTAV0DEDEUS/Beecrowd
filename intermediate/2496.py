def is_possible_to_sort(sequence):
    sorted_sequence = sorted(sequence)
    
    diff_count = 0
    for i in range(len(sequence)):
        if sequence[i] != sorted_sequence[i]:
            diff_count += 1
    
    return diff_count == 2

N = int(input())

for _ in range(N):
    M = int(input())
    sequence = input().strip()
    
    if is_possible_to_sort(sequence):
        print("There are the chance.")
    else:
        print("There aren't the chance.")