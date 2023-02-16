a=10
b=0
try:
    d=a/b
    print(d)
except:
    print('You cannot divide any no. with zero')
else:
    print('Inside Else')
finally:
    print('inside finally')
print('program end')