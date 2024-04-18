immutable_var = 1,2.3, [4,5], True,"False"
print("Immutable tuple: " + str(immutable_var))
#immutable_var[0]=3
#числа и строки в кортеже являются неизменяемыми, можно изменить только элементы списка внутри кортежа:
#immutable_var[2][0] = "n"
#print("Immutable tuple: " + str(immutable_var))
mutable_list = [1,2.3,True,"False"]
mutable_list[0]= False
mutable_list[-1]= 6
print("Mutable list: " + str(mutable_list))
