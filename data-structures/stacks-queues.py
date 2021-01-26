#stacks = LIFO
stack = [1,2,3,4]
stack.append(5)
elem = stack.pop()
elem2 = stack.pop(3)
stack.insert(0,6)
print(elem)
print(elem2)
print(stack)

#queues = FIFO
queue = []
queue.append(5)
queue.append(10)
queue.append(15)
queue.append(20)
queue.append(25)
element = queue.pop(0)
queue.pop(0)
print(queue)
print(element)