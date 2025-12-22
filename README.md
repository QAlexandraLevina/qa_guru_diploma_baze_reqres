# <img src='icons_and_img/baze_rp.png' width="30" height="30"/> Дипломный WEB / Mobile проект тестирования РП проекта BAZE + API Reqres.in с использованием Python, Pytest, Selene, Allure, Jenkins, Selenoid, Allure TestOps, Jira.

---
## 📋 О проекте

---
Данный проект представляет собой фреймворк для UI-тестирования веб-сайта '[BAZE RP](https://bazerp.com/)', Mobile тестирования приложения '[BAZE Mobile](https://bazemobile.com/)', API тестирования сервиса '[Reqres.in](https://reqres.in/)'.
<img src='icons_and_img/Baze RP Main Page.png' width="900" height="800"/>

---
## 🛠️ Технологии и инструменты

---
<img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original-wordmark.svg' width="70" height="70"/> <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg' width="70" height="70"/> <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg' width="70" height="70"/> <img src='https://img.icons8.com/stickers/100/selenium-test-automation.png' width="70" height="70"/> <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg' width="70" height="70"/> <img src='https://avatars.githubusercontent.com/u/5879127?s=200&v=4' width="70" height="70"/> <img src='icons_and_img/Allure_Report.svg' width="70" height="70"/> <img src='icons_and_img/Selenoid.svg' width="70" height="70"/> <code><img width="7%" title="Allure TestOps" src="icons_and_img/allure_testops.png"></code> <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jira/jira-original-wordmark.svg' width="70" height="70"/> <img src='https://img.icons8.com/color/144/telegram-app--v1.png' width="70" height="70"/>

---
## 🔍 Область тестирования

---
Охватывает смоук и регрессионные сценарии для:

UI тестов:
- Header - проверка 'шапки' сайта на всех страницах для авторизованного и неавторизованного пользователя.

- Footer - проверка 'подвала' сайта на всех страницах.

- Раздел 'Ключевые особенности' - валидация контента и его функциональности.

- Навигация - клик по кнопке 'Начать игру' с переходом в раздел 'Как начать играть' и проверкой ссылок.

- Авторизация - позитивная проверка входа в аккаунт.

Mobile тестов:
- Авторизация в режиме гостя

- Проверка разделов Главного меню

API тестов:
- Создание пользователя
- Получение информации о пользователе
- Обновление информации о пользователе
- Удаление пользователя
- Неуспешная регистрация пользователя

---
### <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' width="20" height="20"/> Запуск UI тестов локально

---
**1.** Клонирование репозитория:

`git clone https://github.com/QAlexandraLevina/qa_guru_diploma_baze_reqres.git`

**2.** Установка зависимостей:

`pip install -r requirements.txt`

**3.** Запуск UI тестов с генерацией отчёта Allure:

`pytest web_baze/tests/ -v --alluredir=allure-results`

**4.** Просмотр Allure отчёта:

`allure serve allure-results`

---
### <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' width="20" height="20"/> Запуск Mobile тестов локально

---
**1.** Клонирование репозитория:

`git clone https://github.com/QAlexandraLevina/qa_guru_diploma_baze_reqres.git`

**2.** Установка зависимостей:

`pip install -r requirements.txt`

**3.** Предварительные требования (должны быть установлены):

- Appium Server (версия 2.x)

- Android Studio с эмулятором

- Созданный эмулятор (рекомендуется: Google Pixel 8, Android 16.0)

- APK файл приложения BAZE RP Mobile

**4.** Настройка конфигурации эмулятора:

- Файл .env.local_emulator уже содержит настройки для эмулятора.
- Проверка/обновление пути к APK файлу в строке:

`APP=ваш_локальный_путь_к_apk_файлу`

Пример: 

Windows:
`APP=C:\Users\Имя\Downloads\com.bazemobile.main.apk`

macOS/Linux:
`APP=/Users/Имя/Downloads/com.bazemobile.main.apk`

**5.** Запуск Appium сервера (в отдельном терминале):

`appium`

Должно появиться:

`[Appium] Welcome to Appium v2.x.x`

`[Appium] Appium REST http interface listener started on 0.0.0.0:4723`

**6.** Запуск Android эмулятора:

- Открыть Android Studio

- Запустить эмулятор Pixel 8 (Android 16.0)

Проверка в терминале, что эмулятор запущен:

`adb devices`

- Должно появиться: 

`List of devices attached`

`emulator-5554   device`

**7.** Запуск Mobile тестов с генерацией отчёта Allure:

`pytest mobile_baze/tests/ -v --alluredir=allure-results --context=local_emulator`

**8.** Просмотр Allure отчёта:

`allure serve allure-results`

---
### <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' width="20" height="20"/> Запуск API тестов локально

---
**1.** Клонирование репозитория:

`git clone https://github.com/QAlexandraLevina/qa_guru_diploma_baze_reqres.git`

**2.** Установка зависимостей:

`pip install -r requirements.txt`

**3.** Запуск API тестов с генерацией отчёта Allure:

`pytest api_reqres/tests/ -v --alluredir=allure-results`

**4.** Просмотр Allure отчёта:

`allure serve allure-results`

---
### <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg' width="20" height="20"/> Запуск тестов на удалённом сервере Jenkins

---
**1.** Авторизоваться в '[Jenkins](https://jenkins.autotests.cloud/)'.

**2.** Перейти в Джобу: `test_jenkins_qa_guru_diploma_baze_reqres`.
<img src='icons_and_img/search_job.png' width="900" height="800"/>

**3.** Нажать 'Build with Parameters' на панели слева для запуска тестов.
<img src='icons_and_img/build_now.png' width="900" height="800"/>

**4.** Выбрать параметры сборки для запуска тестов и нажать 'Build'.
<img src='icons_and_img/parametrize_build.png' width="900" height="800"/>

**5.** После завершения сборки открыть Allure-отчёт, кликнув на соответствующую иконку:
<img src='icons_and_img/Allure_Report.svg' width="20" height="20"/>
<img src='icons_and_img/report_icon.png' width="900" height="800"/>

---
### 📊 Визуализация отчётов с результатами (Allure Report, Allure TestOps, Jira, Telegram)

---
#### <img src='https://avatars.githubusercontent.com/u/5879127?s=200&v=4' width="30" height="30"/> **Allure Report**
<img src='icons_and_img/Passed WEB Tests Allure Report.png' width="900" height="800"/>
<img src='icons_and_img/Passed Mobile Tests Allure Report.png' width="900" height="800"/>
<img src='icons_and_img/Passed API Tests Allure Report.png' width="900" height="800"/>

#### <code><img width="3%" title="Allure TestOps" src="icons_and_img/allure_testops.png"></code> **[Allure TestOps](https://allure.autotests.cloud/project/5034/dashboards)**
<img src='icons_and_img/Dashboard TestOps.png' width="900" height="800"/>

#### <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jira/jira-original-wordmark.svg' width="30" height="30"/> **[Jira](https://jira.autotests.cloud/browse/HOMEWORK-1562?filter=allissues)**
<img src='icons_and_img/Issue Jira.png' width="900" height="800"/>

#### <img src='https://img.icons8.com/color/144/telegram-app--v1.png' width="30" height="30"/> **Telegram Notifications**
<img src='icons_and_img/telegram_notification WEB.png' width="350" height="300"/>
<img src='icons_and_img/telegram_notification API.png' width="350" height="300"/>