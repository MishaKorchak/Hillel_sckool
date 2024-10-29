import numbers

l3 = [1,2,3,4,5,6,7,8,9,10,15,20,30,40,50,60,70,80,90,100]
l3_num = sum(num for num in l3 if num % 2 == 0 )
print(f':',l3_num)
