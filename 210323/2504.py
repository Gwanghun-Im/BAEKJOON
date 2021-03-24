string = input()
string = string.replace('()','2')
string = string.replace('[]','3')

stack = []
i = 0
while i < len(string):
    if string[i] not in ')]':
        stack.append(string[i])
        i += 1
    else:
        try:
            if string[i]==')':
                temp = 0
                while stack and stack[-1] != '(':
                    temp += int(stack.pop())
                stack.pop()
                stack.append(temp * 2)

            if string[i]==']':
                temp = 0
                while stack and stack[-1] != '[':
                    temp += int(stack.pop())
                stack.pop()
                stack.append(temp * 3)
            i += 1
        except:
            print(0)
            exit()

try :
    print(sum(list(map(int, stack))))
except :
    print(0)