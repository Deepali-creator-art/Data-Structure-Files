from structlinks.DataStructures import Stack
s1=Stack.Stack()
print(s1)
s1.push(20)
s1.push_multiple([30,40,50,60])
print("After adding elements into a stack")
print(s1)
s1.pop()
print("After remove an element from a stack")
print(s1)
s1.invert()
print("Inverted stack")
print(s1)
s2=s1.map(lambda x:x*2)
print(s2)
s1.push(30)
print("Add element 30")
print(s1)
s1.pop()
print("Updated stack")
print(s1)
print(len(s1))
print(s1.is_empty())
