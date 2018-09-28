class Terminator:
	# class characheristics
	manufacturer = 'Cyberdyne Systems'
	ai = 'Skynet'
	endoskeleton_material = 'titanium'
	type = 'humanoid'
	cpu = 'ai'
	look ='none'


	def t_600(self):
		self.weapon = 'minigun'
		self.type = 'humanoid'

	def t_800(self):
		self.weapon = 'must_find'
		self.main_program = 'infiltration'
		self.look = 'human_type'
		self.speak = 'naturally'
		self.type = 'Flesh-bound endoskeleton'


	def t_1000(self):
		self.main_program = 'infiltration'
		self.type = 'nanorobotic nanitest'


trm = Terminator()
trm.t_800()
trm.t_600()

print(trm.weapon, trm.main_program, trm.look)

