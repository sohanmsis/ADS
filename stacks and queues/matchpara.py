def is_parentheses_balanced(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack
print(is_parentheses_balanced('()')) 
print(is_parentheses_balanced('()[]{}')) 
print(is_parentheses_balanced('(]')) 
print(is_parentheses_balanced('([)]'))
print(is_parentheses_balanced('{[]}')) 