from bill import Ev_Saving

print('''
Welcome to the Electric Vehicle Savings Calculator!
This is a simple program that will help you determine how much money you can save by switching to an electric vehicle.
 ''')


gas_cost = float(input('Please enter how much you currently spend(JOD) on gas per month: '))
monthly_km = float(input('Please enter how many kilometers you drive per day: ')) * 30
electricity_spend = float(input('Please enter your monthly electricity consupmtion in kWh: '))
bill_support = input('Is your electricity bill supported by the government? (y/n): ')

ev = Ev_Saving()
x = ev.increased_electricity(monthly_km) +electricity_spend
bill = Ev_Saving.electic_bill(x ,bill_support, x)
bill_increase = bill - ev.before_bill(bill_support, electricity_spend)
savings = gas_cost - bill_increase


print(f'Your monthly electricity bill before buying an electric vehicle: {ev.before_bill(bill_support, electricity_spend)} JOD')
print(f'Your monthly electricity bill after buying an electric vehicle: {bill} JOD')
print(f'Your monthly electricity bill increase:{bill_increase} JOD')
print(f'Your monthly savings are: {savings} JOD')
