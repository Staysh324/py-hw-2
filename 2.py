# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает 
# Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sumnum = int (input("введите сумму двух чисел: "))
prodnum = int (input("введите произведение чисел: "))
firstnum = sumnum
secondnum = 0
while (firstnum * secondnum) < prodnum:
    secondnum += 1
    firstnum -= 1
print (f"загаданные числа {secondnum} и {firstnum}")