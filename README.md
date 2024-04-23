# Тестовое задание 
## В написании автотестов использовал следующие инструменты:</h2>
 * python 3.x
 * selenium 4
 * для отчета использовал библиотеку pytest-allure

Для запуска тестов, необходимо в терминале ввести:
`pytest -sv --alluredir=allure-results -m run`

Для запуска отчта
`allure serve`

Можно запустить отчет в firefox, предварительно настроив браузер:
1. Перейти к about:config
2. Найти параметр security.fileuri.strict_origin_policy
3. Установить как "неверно"
4. Запустить файл index.html
