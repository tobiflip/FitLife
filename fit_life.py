# Проект FitLife - MVP версия 1.0


# 1. Знакомство
print('Привет! Я твой личный Фитнес трейкер')
# Сбор данных
user_name = input('Для начала, введи свое имя: ')
inuser_age = int(input('Теперь возраст: '))

# 2. Сбор данных
try:
    user_weight = float(input('Далее нужен вес(в кг): '))
except ValueError:
    print('Ввод не коректен')
    user_weight = float(input('Далее нужен вес(в кг): '))
try:
    user_height = float(input('И в заключение рост в метрах(Пример 1.75): '))
except ValueError:
    print('Ввод не коректен')
    user_height = float(input('Далее нужен вес(в кг): '))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = user_weight / (user_height ** 2)


# Подсчет воды: вес * 30 мл
water_l = (user_weight * 30) / 1000


# 4. Вывод красивого результата
print(f'Отчет для пользователя: {user_name} ({inuser_age} г.)')

print(f'Твой Индекс Массы Тела: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')

print('Расчет окончен. Будьте здоровы!')
