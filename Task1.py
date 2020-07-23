
x = [1,2,3,4,5,6,7,8,9,10]
y = [i**2 for i in x if i % 2!=0]
print(y)     #Ans [1, 9, 25, 49, 81]


#Also we can apply in the dictionary object
x = [1,2,3,4,5,6,7,8,9,10]
y = {i:i**2 for i in x if i % 2!=0}

print(y)  #Ans{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
