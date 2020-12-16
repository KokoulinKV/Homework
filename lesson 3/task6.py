# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    exit_word = word[0].upper() + word[1:]
    return exit_word


s = input('Введите несколько слов в нижнем регистре, разделенных пробелом: ')
words = s.split(' ')
exit_words = []
try:
    for el in words:
        if el == '':
            continue
        elif not el.isalpha():
            raise ValueError
        exit_words.append(int_func(el))
    exit_string = ' '.join(exit_words)
    print(exit_string)

except ValueError:
    print('Слова могут состоять только из букв!')
