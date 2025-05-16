def create_phone_number(n):
    if len(n) < 10:
        return None
    else:
        n = [str(c) for c in n]
        return '({}) {}-{}'.format(''.join(n[:3]), ''.join(n[3:6]), ''.join(n[6:10]))
    
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0,9]) )