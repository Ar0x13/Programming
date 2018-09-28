'''
Класс это по сути схема как можно собрать обьект.

'''

class Monitor:
# Свойства/Атрибуты класса
	color = 'black'
	brand = 'Dell'
	state = 'off'
# Методы класса - что может делать класс
	def switch_on(self):
		self.state = 'on'


mon = Monitor()
mon.switch_on()

# Если по другому
#mon = Monitor()
#switch_on(mon)

mon1 = Monitor()
print('Monitor one -> {} and monitor two -> {}'.format(mon.state, mon1.state))
