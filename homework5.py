immutable_var_ = (1, 2, 'a', 'b')
print(immutable_var_)
#immutable_var_1 [0] = 100
#print(immutable_var_1)#этот картеж не поддерживает обращение по элементам, картеж не изменяем
#mutable_list = ([1, 2], 0)
mutable_list = ([1, 2, 'a', 'b', 'Modified'], 0)
print(mutable_list)
mutable_list[0] [0] = 2
print(mutable_list)



