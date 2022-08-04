'''

Input format. String s[1 . . . n], consisting of uppercase and uppercase letters 
of the Latin alphabet, numbers, punctuation marks and brackets from the set []{}().

Output format. If the brackets in s are placed correctly, print
the string "Success". Otherwise, output the index (using indexing from one) 
of the first closing bracket, for
which there is no corresponding opening one. If there is none,
print the index of the first opening bracket for which there is no
corresponding closing one.

'''

def check_brackets(s):
    brackets_pairs = {'(': ')', '[': ']', '{': '}'}
    
    stack = []
    counter = 0
    n = 10**5
    
    for l in s:
        counter += 1
        if l in list(brackets_pairs.keys()):
            stack.append((l, counter))
        if l in list(brackets_pairs.values()):
            if not stack:
                return counter
            elif brackets_pairs[stack[-1][0]] == l:
                stack.pop()
            else:
                return counter
        if len(stack) >= n:
            break
    if not stack:
        return 'Success'
    else:
        return stack[-1][1]
    
print(check_brackets(input()))
