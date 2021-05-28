
text = input('Введите текст на англ :')
eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
rus = 'йцукенгшщзхъфывапролджэячсмитьбю'
newword = ''

for i in text:
    if i == ' ':
        newword += ' '
    else:
        n = eng.find(i)
        newword += rus[n]

print('Ваше предложение :')
print(newword)
