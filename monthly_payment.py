def calculate_monthly_payment(principal, annual_rate, year):
    rate = annual_rate / 100 / 12
    months  = years *12

    payment = (principal*rate) / (1 -(1+rate)**-months)
    return payment

principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")  