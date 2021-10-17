import src.algo as algo 
print(__name__)
string = 'gninraeL nIdekniL htiw tol a nraeL'
reversed_string=''
s=algo.Stack()
for char in string:
    s.push(char)
while not s.is_empty():
    reversed_string += s.pop()
print(reversed_string)