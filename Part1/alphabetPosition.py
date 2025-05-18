def alfabetoPosicion(texto):
    r=''
    alfa=list('abcdefghijklmnopqrstuvwxyz')
    for i in texto:
        if i.isalpha():
            r+=str(alfa.index(i.lower())+1)+' '
    return r[0:len(r)-1]

print(alfabetoPosicion("abc"))