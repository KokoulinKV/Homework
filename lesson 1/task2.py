# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_sec = int(input('Введите время в секундах: '))

sec = time_in_sec % 60
hours = time_in_sec // 3600
minutes = (time_in_sec // 60) - hours * 60

if hours < 10:
    str_hours = f'0{hours}'
else:
    str_hours = hours

if minutes < 10:
    str_minutes = f'0{minutes}'
else:
    str_minutes = minutes

if sec < 10:
    str_sec = f'0{sec}'
else:
    str_sec = sec

print(f'Текущее время {str_hours}:{str_minutes}:{str_sec}')
