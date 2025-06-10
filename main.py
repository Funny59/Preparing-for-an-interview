from stack import MyStack

def getPair(ch):
    match ch:
        case ')':
            return '('
        case '}':
            return '{'
        case ']':
            return '['

s = MyStack()

psp = input()

for char in psp:
    if s.is_empty():
        s.push(char)
    else:
        if s.peek() == getPair(char):
            s.pop()
        else:
            s.push(char)

if s.is_empty():
    print("Сбалансированно")
else:
    print('Несбалансированно')
