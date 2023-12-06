class Car():
	"""A simple car object"""
	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def describe_car(self):
		description = f'{self.brand}, {self.model}, {self.year}.'
		print(f'{description.title()}')

	def read_odometer(self):
		print(f'This car has {self.odometer_reading} Km on it.')

	def update_odometer(self, kms):
		if kms >= self.odometer_reading:
			self.odometer_reading = kms
		else:
			print("You can't roll back the odometer!")

	def increment_odometer(self, kms):
		self.odometer_reading += kms


class Battery():
	"""Representación de batería eléctrica"""
	def __init__(self, battery_size=75):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f'This car has a {self.battery_size} kWh size.')

	def get_range(self):
		if self.battery_size == 75:
			range = 418
		elif self.battery_size == 100:
			range = 507

		print(f'This car can go about {range} km on full charge')

	def upgrade_battery(self):
		"""Upgrade the size of the battery"""
		if self.battery_size == 75:
			self.battery_size = 100
			print(f'Battery upgraded to {self.battery_size} kWh.')
		else:
			print('Battery is already upgraded')


class Electric_car(Car):
	def __init__(self, brand, model, year):
		"""Initiate attributes of base class"""
		super().__init__(brand, model, year)
		self.battery = Battery()


my_car = Electric_car('Volkswagen', 'Fox', '2023')


my_car.describe_car()
my_car.battery.get_range()

my_car.battery.upgrade_battery()
my_car.battery.get_range()