import requests
import json
import random
import string


def generate_username():
    return ''.join(random.choice(string.ascii_letters) for _ in range(8))


def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(12))


def random_string():
    return ''.join(random.choice(string.ascii_letters) for _ in range(4))


name = generate_username()
password = generate_password()


# Регистрация
def sign_up(url="api/sign-up"):
    payload = json.dumps({
        "fio": "Hideo Kojima",
        "name": name,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Вход в систему
def sign_in(url="api/sign-in"):
    sign_up()
    payload = json.dumps({
        "name": name,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


response = sign_in()
jwt = response.json().get("jwt")
refreshToken = response.json().get("refreshToken")


# Обновление jwt и refresh токена
def token_refresh(url="api/token-refresh"):
    global jwt
    global refreshToken
    payload = json.dumps({
        "refreshToken": f"{refreshToken}"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    jwt = response.json().get("jwt")
    refreshToken = response.json().get("refreshToken")
    return response


# Отправка решения по согласованию отпуска
def tasks_decision_vacation(url="api/tasks/decision/vacation"):
    payload = json.dumps({
        "id": 1,
        "status": "APPROVED"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Получение списка заявок на согласование отпуска
def vacation_requests(url="api/vacation/requests?name=inci"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список городов заданной страны для командировок
def businesstrip_country_cities(url="api/business-trip/Россия/cities"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает архив командировок
def businesstrip_archive(url="api/business-trip/archive"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список стран для командировок
def businesstrip_countries(url="api/business-trip/countries"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


trip_aim = random_string()


# Отправление заявки на командировку
def businesstrip_request(url="api/business-trip/request"):
    payload = json.dumps({
        "additionalWishes": "TEST",
        "bookHotel": True,
        "city": "Новосибирск",
        "country": "Россия",
        "employee": "Hideo Kojima",
        "firstDate": 775,
        "lastDate": 460,
        "returnTickets": True,
        "ticketsType": "AIRPLANE",
        "tripAim": f"{trip_aim}"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Обработка заявки на отправку справки на почту (на данный момент является заглушкой)
def certificate_get_email(url="api/certificate/get/email"):
    payload = json.dumps({
        "certificateDate": "01.01.2023",
        "certificateType": "TEST",
        "destinationEmail": "TEST@yahoo.com",
        "originalNecessary": True
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Инициирует скачивание документа на устройство пользователя
def certificate_load_url(url="api/certificate/load/inci"):
    payload = {}
    headers = {
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Добавляет заявку на получение справки
def certificate_send(url="api/certificate/send?name=inci"):
    payload = json.dumps({
        "certificateDate": "01.01.2023",
        "certificateType": "TEST",
        "originalNecessary": True
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Возвращает список документов на отпуск
def vacation_documents(url="api/vacation/1/documents"):
    payload = ""
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает cписок сотрудников компании для последующего их выбора в качестве заместителя на время отпуска
def vacation_alternates(url="api/vacation/alternates?name=inci"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Получение краткой информации о всех существующих задачах
def inventory(url="api/inventory"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


barcode = random_string()
comment = random_string()


# Добавление задачи на инвентаризацию
def inventory_details(url="api/inventory/details"):
    payload = json.dumps({
        "comment": f"{comment}",
        "date": 100,
        "listBarcode": [
            f"{barcode}"
        ],
        "location": "TEST",
        "status": "PERFORMED"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


put_comment = random_string()


# Обновление задачи на инвентаризацию
def put_inventory_details(url="api/inventory/details"):
    payload = json.dumps({
        "comment": f"{put_comment}",
        "date": 100,
        "listBarcode": [
            f"{barcode}"
        ],
        "location": "TEST",
        "status": "PERFORMED",
        "taskId": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response


# Получение информации о задаче по идентификатору
def inventory_details_id(url="api/inventory/details/1"):
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список забронированных переговорных
def booked_meeting_rooms(url="api/booked/booked_meeting_rooms"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


sick_leave_number = random_string()


# Отправляет номер электронного больничного и период больничного
def sick_leave_request(url="api/sick_leave/request"):
    payload = json.dumps({
        "sickLeaveNumber": f"{sick_leave_number}",
        "sickLeavePeriodFirst": 1,
        "sickLeavePeriodLast": 100
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Возвращает модель, которая содержит в себе список заданий
def tasks_feed(url="api/tasks/feed?name=inci"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Отправка решения по согласованию выдачи со склада
def tasks_decision_delivery(url="api/tasks/decision/delivery"):
    payload = json.dumps({
        "requestId": 1,
        "requestStatus": "APPROVED"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Отправка решения по согласованию отпуска
def vacation_request_decision(url="api/vacation/request_decision?name=inci"):
    payload = json.dumps({
        "id": 1,
        "status": "APPROVED"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Возвращает количество дней отпуска на сегодняшний день, на конец года и дату последнего перерасчета отпускных дней
def vacation_days_info(url="api/vacation/days_info"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Отправка заявки на отпуск
def vacation_period(url="api/vacation/period?name=inci"):
    payload = json.dumps({
        "alternates": [
            {
                "alternateName": "Hideo Kojima"
            }
        ],
        "comment": f"{comment}",
        "firstDate": 1,
        "lastDate": 100,
        "type": "WITH_SALARY"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Возвращает список категорий товаров
def categories(url="api/categories"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список товаров на складе
def warehouse(url="api/warehouse"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Возвращает список заявок на выдачу товаров со склада
def warehouse_requests_from_warehouse(
        url="api/warehouse/requests_from_warehouse?name""=inci"):
    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# Отправляет заявку на выдачу товара со склада
def delivery_from_warehouse(url="api/delivery_from_warehouse/request"):
    payload = json.dumps({
        "categoryId": 1,
        "comment": f"{comment}",
        "quantity": 1,
        "requestReason": "TEST",
        "subcategoryId": 1,
        "tmcId": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# Обновляет статус заявки на выдачу со склада
def delivery_request_decision(url="api/delivery/request_decision?name=inci"):
    payload = json.dumps({
        "requestId": 1,
        "requestStatus": "APPROVED"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {jwt}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response
