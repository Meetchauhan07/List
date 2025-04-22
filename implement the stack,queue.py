#menu-driven program to implement the Queue data structure.
queue = []
while True:
    print("1.Enqueue 2.Dequeue 3.Display 4.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        queue.append(input("Enter value: "))
    elif ch == 2:
        if queue: print("Dequeued:", queue.pop(0))
        else: print("Queue empty")
    elif ch == 3:
        print("Queue:", queue)
    else: break
'''
output:
1.Enqueue 2.Dequeue 3.Display 4.Exit
Choice: 3
Queue: []
1.Enqueue 2.Dequeue 3.Display 4.Exit
Choice: 1
1.Enqueue 2.Dequeue 3.Display 4.Exit
Choice: 4
'''
#menu-driven program to implement the stack data structure.
stack = []
while True:
    print("1.Push 2.Pop 3.Display 4.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        stack.append(input("Enter value: "))
    elif ch == 2:
        if stack: print("Popped:", stack.pop())
        else: print("Stack empty")
    elif ch == 3:
        print("Stack:", stack)
    else: break
    1.Push 2.Pop 3.Display 4.Exit
'''
output:
Choice: 1
Enter value: 46
1.Push 2.Pop 3.Display 4.Exit
Choice: 2
Popped: 46
1.Push 2.Pop 3.Display 4.Exit
Choice: 1
Enter value: 86
1.Push 2.Pop 3.Display 4.Exit
Choice: 4
'''











