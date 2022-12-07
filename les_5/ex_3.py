# Используем filter
#2. Напишите программу, удаляющую из текста все слова, содержащие "абв".

txt = 'Привет, забвение меня накрыло, этот опыт был незабвен'
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')


string_text = "абв гарпорвыпав проабвал абцв попакл длывао" \
         "олаывдлор" \
         "абвнк" \
         "покра"
substring = 'абв'
text_lst = string_text.split(" ")
print(text_lst)
output_txt = filter(lambda x: x.lower().find(substring) == -1, text_lst)
print(*output_txt)
