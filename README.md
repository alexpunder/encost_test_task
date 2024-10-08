## Описание проекта.

_**Encost**_ - тестовое задание на FastAPI + Tortoise ORM, реализующее решение следующих поставленных задач:  
Задание 1  
    1) Написать роут, который принимает схему schemas.SchemaTask1  
    2) Отправить на роут input_start равный "2023-12-20T22:39:40" (таймзона UTC+3)  
    3) Найти все записи из endpoint_state где state_start >= input_start и endpoint_id = 139. Отсортировать данные по state_start desc.  
    4) Из данных, полученных в C, найти записи, где id строки кратен числу 3.  
    5) В ответ роут в формате json возвращает: “filtered_count” – количество полученных записей в пункте D, "state_id" - state_id у третьей записи из списка пункта D.  
Задание 2  
    1) Написать GET-роут, который реализует фильтрацию (используя query-параметры) данных из таблицы endpoint_states по следующим операторам:  
        1) endpoint_id: eq  
        2) state_name: eq  
        3) state_reason: eq  
        4) state_start: eq, gt, gte, lt, lte  
где eq – равно, gt – больше, gte – больше или равно, lt – меньше, lte -меньше или равно.  
    2) state_start передается в таймзоне UTC+0, формат (YYYY-MM-DDThh:mm:ss)  
    3) Роут возвращает json, в котором содержатся отфильтрованные записи со всеми колонками из таблицы endpoint_states, сортировка по state_start desc.  
    4) Получить результат с параметрами запроса endpoint_id__eq=139, state_reason__eq= Опоздание, state_start__gte=2024-01-30T08:57:56  

Будет плюсом:  
    • Оформление swagger (/docs)  
    • Docker-файл  

Требования:  
    1. Запрещается менять структуру или данные БД.  
    2. Требуется написать асинхронный сервис на стеке FastAPI + Tortoise ORM.  
    3. В таблице endpoint_states, в колонках state_start, state_end, время в таймзоне UTC+0, формат Unix MicroSecond  

## Используемые технологии.

Python 3.12, FastAPI, Tortoise ORM, Uvicorn, Poetry

## Установка проекта.

1. Находясь в дериктории, где будет размещаться проект, склонируйте его репозиторий:  
```
git@github.com:alexpunder/encost_test_task.git
```
2. Перейди в папку проекта:  
```
cd encost_test_task
```
3. Установите `Poetry`
4. Активировать виртуальное окружение:
```
poetry shell
```
5. Создайте и заполните .env-файл необходимыми данными, выполните команду установки зависимостей проекта:
```
poetry install --no-root
``` 
6. Для корректной работы приложения, выполните следующие команды:  
```
poetry run python src/manage.py makemigrations
```
```
poetry run python src/manage.py migrate
```
7. Для запуска локального сервера, используя терминал, введите команду:  
```
poetry run python src/manage.py runserver
```

## Примеры запросов.

1. Задание 1, пункт 5:  

<details>

```
{
  "filtered_count": 12,
  "state_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-02-09 10:16:23"
}
```

</details>

2. Задание 2, пункт 4:  

<details>

```
[
  {
    "id": 9275,
    "endpoint": {
      "id": 139,
      "endpoint_name": "endpoint_6"
    },
    "client": {
      "id": 139,
      "client_name": "Client"
    },
    "state_name": "Опоздание",
    "state_reason": "Опоздание",
    "state_start": 1707826038000,
    "state_end": 1707827947000,
    "state_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-02-13 15:07:18",
    "group_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-02-13 15:07:18",
    "reason_group": "[NULL]",
    "info": {}
  },
  {
    "id": 9256,
    "endpoint": {
      "id": 139,
      "endpoint_name": "endpoint_6"
    },
    "client": {
      "id": 139,
      "client_name": "Client"
    },
    "state_name": "Опоздание",
    "state_reason": "Опоздание",
    "state_start": 1707816030000,
    "state_end": 1707817455000,
    "state_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-02-13 12:20:30",
    "group_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-02-13 12:20:30",
    "reason_group": "[NULL]",
    "info": {}
  },
  {
    "id": 9181,
    "endpoint": {
      "id": 139,
      "endpoint_name": "endpoint_6"
    },
    "client": {
      "id": 139,
      "client_name": "Client"
    },
    "state_name": "Опоздание",
    "state_reason": "Опоздание",
    "state_start": 1707808471000,
    "state_end": 1707813440000,
    "state_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-02-13 10:14:31",
    "group_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-02-13 10:14:31",
    "reason_group": "[NULL]",
    "info": {}
  },
  {
    "id": 9171,
    "endpoint": {
      "id": 139,
      "endpoint_name": "endpoint_6"
    },
    "client": {
      "id": 139,
      "client_name": "Client"
    },
    "state_name": "Опоздание",
    "state_reason": "Опоздание",
    "state_start": 1707462983000,
    "state_end": 1707463929000,
    "state_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-02-09 10:16:23",
    "group_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-02-09 10:16:23",
    "reason_group": "[NULL]",
    "info": {}
  },
  {
    "id": 9059,
    "endpoint": {
      "id": 139,
      "endpoint_name": "endpoint_6"
    },
    "client": {
      "id": 139,
      "client_name": "Client"
    },
    "state_name": "Опоздание",
    "state_reason": "Опоздание",
    "state_start": 1706605076000,
    "state_end": 1706606502000,
    "state_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-01-30 11:57:56",
    "group_id": "Опоздание|SimpleManualState|cid=139|eid=139|chid=-1001921701685|mt=2024-01-30 11:57:56",
    "reason_group": "[NULL]",
    "info": {}
  }
]
```

</details>
