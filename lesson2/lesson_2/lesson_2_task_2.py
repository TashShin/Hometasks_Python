def is_year_leap(year):
    return True if year_check % 4 == 0 else False


year_check = 1988
result = is_year_leap(year_check)
print(f"год {year_check}: {result}")

year_check = 1675
result = is_year_leap(year_check)
print(f"год {year_check}: {result}")
