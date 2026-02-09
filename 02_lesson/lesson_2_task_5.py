def month_to_season(month):
    if 1 <= month <= 12:
        if month in [12, 1, 2]:
            return "Зима"
        elif month in [3, 4, 5]:
            return "Весна"
        elif month in [6, 7, 8]:
            return "Лето"
        else:
            return "Осень"
    else:
        return "Номер месяца должен быть от 1 до 12"


month_num = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month_num))
