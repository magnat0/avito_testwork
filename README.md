Данный код предназначен для проведения автоматизированных скриншотных тестов.
Тесты проверяют работу счетчиков эковклада пользователя Avito.
Каждый тест проверят работу сразу 3 счетчиков: сохранённого объёма воды, предотвращённого объёма выброса CO2 и сэкономленной
электроэнергии, так как они с друг другом никак не связаны.
Тесты не проверяют результат, а только создают скриншоты фрагмента страницы с счетчиком.

Чтобы запустить авто-тесты на своем личном ПК, нужно провести следующие действия:

1. Склонировать репозиторий

```git clone https://github.com/magnat0/avito_testwork.git```

2. Перейти в директорию проекта

```cd avito_testwork```

3. Установить зависимости

```pip3 install -r requirements.txt```

4. Скачать браузерные движки

```playwright install```

5. Запустить скрипт

```pytest .```