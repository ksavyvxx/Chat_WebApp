[README.md](https://github.com/user-attachments/files/29375565/README.md)
# Chat WebApp 💬

Простое и функциональное веб-приложение для обмена сообщениями в реальном времени (чат-комната), построенное на веб-фреймворке Django.

## ✨ Функционал

*   **Простая регистрация:** Вход по имени пользователя (сессии хранятся локально).
*   **Чат-комната:** Возможность отправлять текстовые сообщения всем участникам.
*   **Фильтрация:** Поиск сообщений по конкретной дате.
*   **Редактирование:** Возможность изменять свои сообщения в течение **30 минут** с момента отправки.
*   **Архивное удаление:** Сообщения не удаляются из базы навсегда, а переносятся в архив, откуда автор может их восстановить в один клик.
*   **Система уведомлений:** Всплывающее боковое меню с системными сообщениями (ошибки, успешные действия, предупреждения).

## 🚀 Инструкция по локальному запуску

Следуйте этим шагам, чтобы развернуть проект у себя на компьютере:
## 1. Подготовка проекта
Склонируйте репозиторий и перейдите в корневую директорию проекта:
```bash
git clone <ссылка_на_ваш_репозиторий>
cd chat_webapp
```
## 2. Настройка виртуального окружения

```bash
    На Windows:
    python -m venv venv
    venv\Scripts\activate
    
    На macOS / Linux:
    python3 -m venv venv
    source venv/bin/activate
```

## 3. Автоматический запуск

```bash
  Для Windows (Command Prompt / cmd):
  pip install -r requirements.txt && python manage.py migrate && python manage.py runserver

  Для Windows (PowerShell):
  pip install -r requirements.txt; python manage.py migrate; python manage.py runserver

  Для macOS / Linux (Bash/Zsh):
  pip install -r requirements.txt && python manage.py migrate && python manage.py runserver
```
