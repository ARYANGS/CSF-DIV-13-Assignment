#LIST OPERATIONS
l = [5, 2, 8]
print("Original List:", l)

l.append(4)      
l.insert(1, 9)   
l.remove(2)      
x = l.pop()      
l.sort()         

print("Final List:", l)

#TUPLE OPERATIONS
t = (10, 20, 20, 30, 40)
print("Original Tuple:", t)

c = t.count(20)  
i = t.index(30)  
size = len(t)    
big = max(t)     
small = min(t)   

print("Count of 20:", c)
print("Index of 30:", i)
print("size:", size)
print("biggest element:", big)
print("smallest element:", small)

#DICTIONARY OPERATIONS
d = {1: 'A', 2: 'B', 3: 'C'}
print("Original Dict:", d)

d[4] = 'D'       
val = d.pop(2)   
k = d.keys()     
v = d.values()   
item = d.get(3)  

print("Final Dict:", d)
print("Keys:", list(k))
print("Values:", list(v))