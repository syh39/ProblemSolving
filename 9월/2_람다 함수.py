# 람다함수 == 익명함수
# 람다 표현식이라고도 함

def plus_one(x):
    return x+1

plus_two=lambda x:x+2

print(plus_one(1))
print(plus_two(1))

a=[1,2,3]
print(list(map(plus_one, a)))
print(list(map(lambda x:x+1, a)))