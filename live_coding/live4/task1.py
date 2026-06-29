# 1.
# Потрібно створити функцію make_request, яка має дуже суворі обмеження щодо безпеки та зворотної сумісності.
# Умова: Реалізувати функцію make_request з такими правилами для аргументів:
# url - має бути тільки позиційним параметром (positional-only). Користувач не повинен мати змоги написати make_request(url="...").
# method - стандартний параметр (можна передавати і так, і так), але за замовчуванням він дорівнює "GET".
# timeout та retry_count - мають бути тільки іменованими (keyword-only). За замовчуванням timeout=5, retry_count=3.
# Функція повинна приймати будь-які інші додаткові налаштування (наприклад, заголовки headers, cookies тощо)
# у вигляді словника, але не через окремий аргумент, а динамічно.
# Всередині функція просто повертає рядок або словник, який показує, як саме розпарсилися аргументи.

# def make_request(url,
#                  /,
#                  method='GET',
#                  *,
#                  timeout=5,
#                  retry_count=3,
#                  **kwargs
#                  ):
#     return {"method": method,
#             "url":url,
#             "timeout":timeout,
#             "retry_count":retry_count,
#             "additional info": kwargs
#             }
#

# 2. Контекст: Замість того, щоб писати один величезний спагеті-код для очищення брудних даних
# (фільтрація матюків, видалення пробілів, форматування), ми хочемо збирати "конвеєр" (pipeline) з маленьких цеглинок.
#
# Умова:
# Дано три базові (універсальні) функції:
# replace_word(text, target, replacement) - замінює слово.
# strip_chars(text, chars) - обрізає специфічні символи з кінців.
# modify_case(text, style) - змінює регістр (style може бути "upper", "lower", "title").
# За допомогою functools.partial (і без використання lambda або створення нових функцій через def),
# учень має зібрати 2 специфічні інструменти:
# clean_shouting_text - заздалегідь налаштований так, щоб заміняти "блін" на "зірочка",
# обрізати знаки оклику ! та переводити все в нижній регістр.
# make_title_meta - обрізає хештеги #, міняє "важливо" на "⚠️", робить регістр "Title Case".
# Написати функцію-раннер run_pipeline(text, list_of_functions), яка приймає початковий рядок
# та список замикань/парціальних функцій, проганяє текст через них по черзі (ланцюжком) і повертає фінальний результат.

from functools import partial

def replace_word(text, target, replacement):
    return text.replace(target, replacement)

def strip_chars(text, chars):
    return text.strip(chars)

def modify_case(text: str, style):
    styles = {"upper": text.upper, "lower": text.lower, "title": text.title}
    return styles[style]()

clean_shouting_text = [
    partial(
    replace_word,
    target = "блін",
    replacement = "*"
    ),
    partial(
    strip_chars,
    chars = "!"
    ),
    partial(
    modify_case,
    style = "lower"
    )
]

make_title_meta = [
    partial(
    replace_word,
    target = "важливо",
    replacement = "⚠️"
    ),
    partial(
    strip_chars,
    chars = "#"
    ),
    partial(
    modify_case,
    style = "title"
    )
]

def run_pipeline(text, list_of_functions):
    for function in list_of_functions:
        text = function(text)
    return text

string = "!блін блін блін ляляляля тополя ЩВПТЗОІВШЩПМТЗЩВОШАПТЗУШОАВ валваьвщла #"
print(run_pipeline(string, clean_shouting_text))