import heapq

while True:
    try:
        n = int(input())
        operations = []
        for _ in range(n):
            cmd, *args = map(int, input().split())
            operations.append((cmd, *args))

        is_stack = True
        is_queue = True
        is_priority_queue = True

        stack_data = []
        queue_data = []
        priority_queue_data = []

        for operation in operations:
            cmd, *args = operation
            if cmd == 1:
                x = args[0]
                stack_data.append(x)
                queue_data.append(x)
                heapq.heappush(priority_queue_data, -x)
            elif cmd == 2:
                x = args[0]
                if len(stack_data) == 0 or stack_data.pop() != x:
                    is_stack = False
                if len(queue_data) == 0 or queue_data.pop(0) != x:
                    is_queue = False
                if len(priority_queue_data) == 0 or -heapq.heappop(priority_queue_data) != x:
                    is_priority_queue = False

        if is_stack and not is_queue and not is_priority_queue:
            print("stack")
        elif not is_stack and is_queue and not is_priority_queue:
            print("queue")
        elif not is_stack and not is_queue and is_priority_queue:
            print("priority queue")
        elif not is_stack and not is_queue and not is_priority_queue:
            print("impossible")
        else:
            print("not sure")

    except EOFError:
        break
