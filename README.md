# Robotics Vision Project Documentation

Этот проект определяет огонь через YOLOv8.

## Требования

- Python 3.x

## Установка

1. Клонируй репозиторий:
    ```bash
    git clone https://github.com/mkhmtolzhas/RoboticsVision.git
    cd RoboticsVision
    ```
2. Создай виртуальное окружение для Python:
    ```bash
    # Создаем виртуальное окружение
    python -m venv venv

    # Заходим туда через Windows
    venv\Scripts\activate

    # Заходим туда через macOS или Linux
    source venv/bin/activate
    ```

3. Установи зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Создай файл `.env` на основе `.env.example`:
    ```bash
    cp .env.example .env
    ```

5. Заполни файл `.env`
    ```bash
    INFOBIP_API_KEY=
    INFOBIP_API_URL=
    ```

## Usage

1. Просто запустите main.py:
    ```bash
    python main.py
    ```

## Важно!

Удалите README.md обязательно, если хотите что бы вас не спалили :D