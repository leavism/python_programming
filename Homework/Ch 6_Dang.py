# Exercise 6.9
''' Feet to meters module:'''
def footToMeter(foot):
	meter = 0.305 * foot
	return meter


'''
Meters to feet module:
def meterToFoot(meter):
	foot = meter / 0.305
	return foot


	# import footToMeter from feettometer.py
	# import meterToFoot from metertofoot.py

print("Feet     Meters     |     Meters     Feet")
for f in range(1, 10):
	print(f,"      ",format(footToMeter(f),"<10.3f"))
'''

# Exercise 6.11
def computerCommission(n):
	if n <= 5000:
		c = n * 0.08
		return c
	elif n > 5000 and n <= 10000:
		c = (5000 * 0.08) + ((n - 5000) * 0.1)
		return c
	elif n > 10000:
		c =  (5000 * 0.08) + (5000 * 0.1) + ((n - 10000) * 0.12)
		return c


print("Sales Amount          Commission")
for n in range(10000, 100000, 5000):
	print(n,"               ",format(computerCommission(n),"10.1f"))
print("100000               ",format(computerCommission(100000),"10.1f"))
# Exercise 6.18