from pulp import LpMaximize, LpProblem, LpVariable

# Ініціалізація моделі
model = LpProblem(name="beverage_production", sense=LpMaximize)

# Оголошення змінних
lemonade = LpVariable(name="lemonade", lowBound=0)
fruit_juice = LpVariable(name="fruit_juice", lowBound=0)

# Додавання обмежень на ресурси
water_constraint = 2 * lemonade + fruit_juice <= 100
sugar_constraint = lemonade <= 50
lemon_juice_constraint = lemonade <= 30
fruit_puree_constraint = 2 * fruit_juice <= 40

# Додавання обмежень до моделі
model += water_constraint, "water"
model += sugar_constraint, "sugar"
model += lemon_juice_constraint, "lemon_juice"
model += fruit_puree_constraint, "fruit_puree"

# Функція максимізації
model += lemonade + fruit_juice, "total_production"

# Вирішення задачі
model.solve()

# Виведення результатів
print("Результати обрахунків:")
print("Лимонад:", lemonade.varValue)
print("Фруктовий сок:", fruit_juice.varValue)