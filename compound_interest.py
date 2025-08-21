principle = 0
interest_rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter principle amount: "))
    if principle <= 0:
        print('Principle cant be 0')
    
while interest_rate <= 0:
    interest_rate = float(input("Enter interest rate: "))
    if interest_rate <= 0:
        print('Interest rate cant be 0')

while time <= 0:
    time = float(input("Enter time in years: "))
    if time <= 0:
        print('Time cant be 0')

total = principle * (1 + interest_rate / 100)**time
print(f"Balance after {time} years is ₱{total}")


