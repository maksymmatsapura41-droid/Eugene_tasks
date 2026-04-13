# Task 2
# Дано довгий текстовий рядок. Написати функцію top_3_words(text),
# яка повертає список з трьох слів, що зустрічаються у тексті найчастіше,
# у порядку спадання їхньої частоти. Регістр не має значення, розділові знаки слід ігнорувати.


def top_3_words(text: str) -> list:
    text = text.lower()
    for item in text:
        if item in ",.!?":
            print(item)
            text = text.replace(item, " ")
    words = text.split()
    print(words)
    dic = {}
    for word in words:
        dic[word] = dic.get(word, 0) + 1
    return [item[0] for item in sorted(dic.items(), key=lambda x: x[1], reverse=True)[:3]]

print(top_3_words("Hello World a a ajaoifhoihjf oisjfosidn fisjfo isjfoi jofpj opjf finish. shit, finish, shit. finish!, finish? finish"))
