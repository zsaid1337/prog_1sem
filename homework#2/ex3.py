stroka = input()
stroka1 = stroka
nach = stroka[0]
kon = stroka[-1]
pal = False
zerk = False
stroka1 = kon + stroka1[1:-1] + nach
if (('E' in stroka or 'J' in stroka or 'S' in stroka or 'Z' in stroka ) and ('3' in stroka or 'L' in stroka or '%' in stroka or '2' in stroka ))or ('M' in stroka) and  ('B' not in stroka or 'C' not in stroka or 'G' not in stroka):
    zerk = True
if stroka == stroka[::-1]:
    pal = True   
if pal == True and zerk == True:
    print(f'{stroka} is a mirrored palindrome.')
elif pal == True:
    print(f'{stroka} is a regular palindrome.')
elif zerk == True:
    print(f'{stroka} is a mirrored string.')
else:
    print(f'{stroka} is not a palindrome.')































                         
