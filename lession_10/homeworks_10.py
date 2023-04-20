"""
Текстова гра на тему Українських народних казок
Правила гри:
    Гравець має обирати персонажа, за яким він буде грати. Потім гравець починає свою
    пригоду у вигляді текстових повідомлень. Гра складається з декількох етапів, на кожному з яких гравець зустрічає нових
    персонажів та переживає різні пригоди. Гравець має право вибирати, як він хоче діяти у певній
    ситуації: діалог з персонажем, бій, втеча тощо. Залежно від вибору гравця, відбуваються різні
    наслідки.

Приклади:

* Гравець обирає персонажем козака. Він зустрічає чаклуна, який накладає на нього прокляття.
    Гравець може спробувати розв'язати прокляття, знайти антидот або битися з чаклуном.
    Залежно від вибору гравця, він може отримати нову здатність або втратити частину своїх вмінь.
* Гравець обирає персонажем пересмішника. Він потрапляє в хитру ситуацію, де йому потрібно
    обдурити злодія. Гравець може скористатися своїм словесним даром, знайти слабкі місця
    злодія або спробувати зібрати команду з іншими персонажами для змагання проти злодія.

Ідеї для  тестів:

    Тест на перевірку правильності вибору персонажа гравцем.
    Тест на перевірку вибору гравцем діалогу, який приводить до нової здатності персонажа.
    Тест на перевірку вибору гравцем діалогу, який приводить до втрати здатностей персонажа.
    Тест на перевірку правильності вибору гравцем
    Тест на введення некоректної відповіді гравцем: спроба ввести символи, відмінні від "так" і "ні".
    Тест на перехід до наступної дії: перевірка, чи збільшується лічильник після завершення попередньої.
    Тест на завершення гри: перевірка, що гравець не може перейти до наступної дії, якщо він вже завершив останню.
    Тест на вибір гравцем дії: перевірка, чи збільшується лічильник правильних відповідей після кожної правильної відповіді.

Поради до написання коду:

1. Створіть словник, що містить перелік персонажів та їх характеристик, таких як ім'я,
    рівень життя, сила тощо.
2. Запросіть у гравця вибір персонажа зі списку.
3. Визначте етапи гри, наприклад, "Зустріч з першим персонажем", "Бій з монстром",
    "Вирішення головоломки" тощо.
4. Для кожного етапу гри створіть функцію, яка відповідає за обробку цього етапу.
    Функція повинна виводити текстове повідомлення, яке описує ситуацію гравця,
    а також список доступних дій, які гравець може вибрати. Наприклад,
    "Ви зустрілися з гобліном. Що ви будете робити?
    1. Почати діалог з ним. 2. Розпочати бій. 3. Спробувати втекти".
5. Для кожної дії, яку може вибрати гравець, створіть окрему функцію.
    Функція повинна перевіряти, чи є ця дія можливою в поточній ситуації,
    і виконувати відповідні дії. Наприклад, якщо гравець вибирає
    "Розпочати бій", функція повинна розпочати бій з монстром і вивести повідомлення про результат.
6. Для обробки помилок та виключень, наприклад, якщо гравець ввів
    неправильне значення, використовуйте блоки try/except.
7. Для збереження прогресу гравця у грі, зберігайте дані у файл.

Не ускладнюйте собі життя:
Достатньо 3 персонажи та 3 дії а також 3  кроки:
    1. початок(вибір героя - Котигорошко, Змій, кінь)
    2. взаємодія(комп'ютер обирає героя з тих що лишилися і пропонує дії гравцю)
    3. розв'язка ( відповідно до обраних дій та коефіцієнтів - перемога, поразка чи нічия)
І треба хоча б 9 тестів на усе це добро.
"""