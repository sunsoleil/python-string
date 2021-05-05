print("helloworld")
print("hell'o' world")
print("hell'o' \"w\"orld")
#\를 앞뒤에 두면 그냥 문자로 봐줌 \=escape

#newline 줄바꿈 \n
print('H')
print('E')
print('L')
print('L')
print('O')
print('h\ne\nl\nl\no')

#docstring
print('''
H
E
L
L
O
''')

a = 'Hello Python'
print(a)
#length
print(len(a))
#index 문자 순서 0부터가 처음
print(a[0])
print(a[1])
print(a[6:12])

#repeat
print(a*2)
print((a+'\n')*2)
#\n이 줄바꿈이므로 a 변수에 줄바꿈을 결합하여 곱하기 2한 것임




#+name+으로 변수 설정 가능 +name+앞에는 문자열이 끝나므로 꼭 ''를 붙여줘야 하고 뒤에도 붙여줘야 함
name = 'hyejin'
age = '13'
print('Bonjour hello to '+name+'. adlhfk alhfd alcdh acnlq aclncf lqceln '+age+' apple computer qlhecq, ahclhfue '+name+' alfchqp fruit apple cdhcfnlq acldfhqu')


#positional formatting
print('Bonjour hello to {}. adlhfk alhfd alcdh acnlq aclncf lqceln {} apple computer qlhecq, ahclhfue {} alfchqp fruit apple cdhcfnlq acldfhqu'.format('hyejin', 13, 'hyejin'))


#named placeholder (:d는 무조건 숫자만)
print('Bonjour hello to {name}. adlhfk alhfd alcdh acnlq aclncf lqceln {age:d} apple computer qlhecq, ahclhfue {name} alfchqp fruit apple cdhcfnlq acldfhqu'.format(name='hyejin', age=13))

