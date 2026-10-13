x=int(input(':請輸入成績'))
if X>100 or x<0:
    print('錯誤成績')
else:
    if x>=60:
        print('通過')
    elif 50<=x<=59:
        print('補考')
    else:print('當掉')
