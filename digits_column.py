# Програма, яка виводить цифри 4-значного числа в стовпчик
# Використовується функція divmod

# Користувач вводить 4-значне число
number = int(input("Введіть 4-значне число: "))

# Отримуємо першу цифру (тисячі) та залишок
digit1, remainder = divmod(number, 1000)

# Отримуємо другу цифру (сотні) та залишок
digit2, remainder = divmod(remainder, 100)

# Отримуємо третю цифру (десятки) та залишок
digit3, digit4 = divmod(remainder, 10)

# Виводимо цифри в стовпчик
print(digit1)
print(digit2)
print(digit3)
print(digit4)
