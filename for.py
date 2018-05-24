# for 반복문

a = ['dog', 'pig','soyoung']

for animal in a:
    print(animal, end = ' ')
else:
    print('')

print('!!!!!!!!!!!!!!!!')


#복합 자료형을 사용하는 for문

l = [('소영', 10), ('또영', 20), ('여소',30)]

for data in l:
    print('이름:%s, 나이:%d' % data)

for name, age in l:
    print('이름:{0},나이:{1}'.format(name,age))

l = [{'name':'소영','age': 10}, 
     {'name':'또영','age': 20}, 
     {'name':'여소','age': 30}]

for data in l:
    print('이름:%(name)s, 나이:%(age)d' % data)


# 1~10 합 구하기

s=0
for i in range(1,11):
    s+=i

print(s)

#break

for i in range(10):
    if i>5:
        break

    print(i, end = ' ')
else:
    print('')
print('!!!!!!!!!!!')

#continue
for i in range(10):
    if i<=5:
        continue

    print(i, end= ' ')
else:
    print('')

print('------------------------------')



#구구단
for i in range(1,10):
    for j in range (1,10):
      print(str(j) +"x" + str(i) +"="+str(j*i) ,end = '\t')

else:
    print('')
