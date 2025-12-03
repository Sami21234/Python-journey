
# 4. What will be the length of following set s: s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 

s = set()
s.add(20)
s.add(20.0)   # In python if the equality operator concist of same value like here --> 20 == 20.0 will act as same values and returns the true
s.add('20')
print(len(s))