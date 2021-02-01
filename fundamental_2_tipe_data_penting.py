
print('\nTipe data skalar / sederhana')
anak1 = 'Kenar'
anak2 = 'Senja'
anak3 = 'Gantari'
anak4 = 'Rinjani'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nTipe Data List/Daftar/Array')
anak = ['Kenar', 'Senja', 'Gantari', 'Rinjani']
print(anak)
anak.append('Banyubiru')
print(anak)

print('\nsapa anak ke 2')
print(f'Hai {anak[1]}')

print('\nsapa anak ke 1')
print(f'Hai {anak[0]}')

print('\nsapa semua anak')
for a in anak :
    print(f'Hai {a}')

print('\nsapa semua anak cara ribet')
for a in range (0, len(anak)) :
    print(f'{a+1}. Hai {anak[a]}')