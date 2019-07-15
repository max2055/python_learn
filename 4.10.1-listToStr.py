def listToStr(spams):
    str = ''
    for i in range(0, len(spams)):
        if i==0:
            str=spams[i]
        elif i==len(spams)-1:
            str=str+', and '+spams[i]
        else:
            str = str + ', ' + spams[i]
    return str


spams = ['apple', 'orange', 'banana', 'peach']

str = listToStr(spams)
print(str)
