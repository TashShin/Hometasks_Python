def month_to_season(month):
    if 1 <= month <= 2:
        return "Winter"
    if month == 12:
        return "Winter"
    if 3 <= month <= 5:
        return "Spring"
    if 6 <= month <= 8:
        return "Summer"
    if 9 <= month <= 11:
        return "Fall"
    return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))
