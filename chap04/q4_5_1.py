functions = [sum,min,max]
number_list= range(1,11)
for func in functions:
    print("function:{},result:{}".format(func.__name__,func(number_list)))
