age_in_days = int(input())
days = (age_in_days % 365) % 30
months = (age_in_days % 365) // 30
years = age_in_days // 365

print(f"{years} ano(s)\n{months} mes(es)\n{days} dia(s)")
