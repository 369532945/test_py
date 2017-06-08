字符串
name = input('plse input you name:')
age = input('plse input you age:')

#-------------------------- #拼接，少用
info = '''
- - - info - - -
Name:'''+name+'''
Age:'''+age
print(info)

#---------------------------  #默认输出为字符串要转换为数字整型，只能输入数字  %s 字符串，%d 为数字
info2 = '''
--- info2 %s ---
Name:%s
Age:%s''' %(name,name,age)
print(info2)

#--------------------------  #{_name} 这个可以是其它的字符串，这里只是为了好区分
info3 = '''
--- info3 {_name} ---
Name:{_name}
Age:{_age}'''.format(_name=name,_age=age)
print(info3)

#------------------------- #按照format() 里的顺序
info4 = '''
--- info4 {0} ---
Name:{0}
Age:{1}'''.format(name,age)
print(info4)
