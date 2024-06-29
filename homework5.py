immutable_var = 1 , True , 'simple'
print(immutable_var)
print('Кортеж предназначен (в том числе) для хранения данных, '
      'поэтому нельзя изменить значения элементов кортежа')
mutable_list = ['un' , 'dos' , 3]
print(mutable_list)
mutable_list[0] = 1
mutable_list[1] = 2
mutable_list[2] = 'tres'
print(mutable_list)