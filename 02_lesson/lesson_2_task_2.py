def is_year_leap(year):
    return "True" if year % 4 == 0 else "False"


yo = int(input("Введите год: "))
result = is_year_leap(yo)
print(f"Год {yo}: {result}")
