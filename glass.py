def glass(lst):
    lst_glass=[]
    for i in lst:
        if i=='а'or i=='е'or i=='ё'or i=='и'or i=='о'or i=='у'or i=='ы'or i=='э'or i=='ю'or i=='я':
            lst_glass.append(i)
    lst_glass
    return lst_glass
a=glass(list(input()))
a=''.join(a)
print(a)