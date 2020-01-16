aa =dict()
aa["q"] = 1
aa["w"] = 12
aa["e"] = 123
# {'q': 1, 'w': 12, 'e': 123}


# {'w': 12, 'e': 123}

# print(aa)
dict1 =dict()
for i in aa: # q, w, e
    if i == 'e' or i =='w':
        dict1[i] = aa[i] # i = e ///dict1['e'] = 123   # i=w //// dict1['w'] = 12
print(dict1)

