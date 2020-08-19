score= []
maxscore=0
minscore=100
total=0
name= []

for i in range(5):
    n = int(input("成績"))
    score.append(n)
    na = input("名字")
    name.append(na)
    
    if n > maxscore:
        maxscore=n
        b=na
    if n < minscore:
        minscore=n
        c=na
    total = total + n
    
yee =  total/len(score)
print("總分:",total)
print("平均:",yee)
print("最高分:",maxscore,b)
print("最高分:",minscore,c)
        