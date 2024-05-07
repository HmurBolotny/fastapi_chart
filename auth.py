"""
Здесь храним логику проверки и авторизации пользователей.

пользователи:
	lab_worker
	engineer
    admin
    viewer

Предполагаем, что если viewer залогинился,,
то его не нужно разлогинивать через определенный промежуток времени.

Если залогинился lab_worker, engineer, admin, то их нужно разлогинить через два часа (например.)

Пример взаимодействия.

user: User = User.get_user(request)
if not user.is_authenticated()
    return

user: User = User.register(login, password)


"""


