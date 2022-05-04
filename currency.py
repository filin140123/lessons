rate_start_date = float(input("Введите курс доллара при покупке: "))
rate_final_date = float(input("Введите курс доллара при продаже: "))

buy_price = float(input("Введите сумму покупки в долларах: "))
buy_price_in_rub = buy_price * rate_start_date
sell_price = float(input("Введите сумму продажи в долларах: "))
sell_price_in_rub = sell_price * rate_final_date
result = sell_price_in_rub - buy_price_in_rub

print(f"Сумма покупки в рублях {round(buy_price_in_rub, 2)}")
print(f"Сумма продажи в рублях {round(sell_price_in_rub, 2)}")
print(f"Вы заработали {round(result, 2)} рублей.")
