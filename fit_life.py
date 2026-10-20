# Проект FitLife - MVP версия 1.0
import constants

# 1. Знакомство
print('Привет! Я твой личный Фитнес трейкер')

# 2. Сбор данных

user_name = input('Для начала, введи свое имя: ').title()
try:
    user_age = int(input('Теперь возраст: '))
except ValueError:
    print('Ввод не коректен')
    user_age = int(input('Теперь возраст: '))

try:
    user_weight = float(input('Далее нужен вес(в кг): ').replace(',', '.'))
except ValueError:
    print('Ввод не коректен')
    user_weight = float(input('Далее нужен вес(в кг): ').replace(',', '.'))

try:
    user_height = float(input('И в заключение рост в метрах(Пример 1.75): ').replace(',', '.'))
except ValueError:
    print('Ввод не коректен')
    user_height = float(input('Далее нужен вес(в кг): ').replace(',', '.'))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = user_weight / (user_height ** 2)


# Подсчет воды: вес * 30 мл
water_l = (user_weight * constants.ML_PER_KG) / constants.ML_IN_LITER


# 4. Вывод красивого результата
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')

print(f'Твой Индекс Массы Тела: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')

print('Расчет окончен. Будьте здоровы!')
