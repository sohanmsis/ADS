stack = []
with open('file.txt', 'r') as file:
    for line in file:
      stack.append(line)
    reversed_file = []
    while stack:
        reversed_file.append(stack.pop())
        with open('reversed_file.txt', 'w') as file:
          for line in reversed_file:
            file.write(line)