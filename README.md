# Управление ссылками через bitly

Приложение позволяет сокращать ссылки через [bitly](https://bitly.com/) и получать статистику переходов по сокращенным ссылкам.

[![asciicast](https://asciinema.org/a/nSQufceSLBj1Vcq3q0TbIVQTU.svg)](https://asciinema.org/a/nSQufceSLBj1Vcq3q0TbIVQTU)

### Установка

Для работы приложения требуется **Docker** и **Docker Compose**.

### Настройка

Для взаимодействия с **bitly** требуется получить [API-токен](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-find-my-OAuth-access-token-).

Подготовить файл для хранения API-токена сервиса:
```
cp .env.example .env
```

Указать **API-ключ** в `.env`:
```
BITLY_TOKEN=<token>
```

### Запуск

Создание сокращенной ссылки:

```
make run args=http://site.ru
```

Получение статистики по ссылке:

```
make run args=http://bit.ly/test
```

Удаление всех временных файлов приложения:
```
make flush
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).