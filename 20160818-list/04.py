x = [1,1,1]
x[1] =2
print x

del x[2]
print x

x = list('Perl')
x[2:] = list('ar')
print ''.join(x)

numbers = [1,2,3,4,5,6,7,8,9,10]
a = list('abc')
numbers[::4] = a
print numbers

numbers = [1,5]
numbers[1:1] = [2,3,4]
print numbers

