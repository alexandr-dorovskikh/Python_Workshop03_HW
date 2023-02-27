# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
"""
num_list = [int(input(f"A{i+1} = ")) for i in range(int(input("N = ")))]
X = int(input("X = "))
print(f"{X} встречается {num_list.count(X)} раз")
"""

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X

"""
num_list = [int(input(f"A{i+1} = ")) for i in range(int(input("N = ")))]
X = int(input("X = "))

close_num = num_list[0]
for num in num_list[1:]:
    if abs(num - X) < abs(close_num - X):
        close_num = num

print(f"Ближайшее число к числу {X}: {close_num}")
"""

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

"""
# en
letters_points = {letter: 1 for letter in 'A,E,I,O,U,L,N,S,T,R'.split(",")}
letters_points = letters_points | {letter: 2 for letter in 'D,G'.split(",")}
letters_points = letters_points | {letter: 3 for letter in 'B,C,M,P'.split(",")}
letters_points = letters_points | {letter: 4 for letter in 'F,H,V,W,Y'.split(",")}
letters_points = letters_points | {'K': 5}
letters_points = letters_points | {letter: 8 for letter in 'J,X'.split(",")}
letters_points = letters_points | {letter: 10 for letter in 'Q,Z'.split(",")}

# ru
letters_points = letters_points | {letter: 1 for letter in 'А,В,Е,И,Н,О,Р,С,Т'.split(",")}
letters_points = letters_points | {letter: 2 for letter in 'Д,К,Л,М,П,У'.split(",")}
letters_points = letters_points | {letter: 3 for letter in 'Б,Г,Ё,Ь,Я'.split(",")}
letters_points = letters_points | {letter: 4 for letter in 'Й,Ы'.split(",")}
letters_points = letters_points | {letter: 5 for letter in 'Ж,З,Х,Ц,Ч'.split(",")}
letters_points = letters_points | {letter: 8 for letter in 'Ш,Э,Ю'.split(",")}
letters_points = letters_points | {letter: 10 for letter in 'Ф,Щ,Ъ'.split(",")}

#
score = 0
for letter in list(input("Введите слово: ")):
    score += letters_points[letter.upper()]

print(f"Количество очков: {score}")
"""