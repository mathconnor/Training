# This is the class blueprint for a Memory Management Unit Object. --|

class MMU():
	# The __init__(self) function contains what the Object will
	# immediately HAVE, once created.
	def __init__(self):
		self.memory = [0] * 4096
	
	
	# The functions below define what the Object can DO once created.
	def read(self, address):
		return self.memory[address]


	def write(self, address, value):
		self.memory[address] = value


	def loadROM(self, rom):
		# Loading ROM into Memory
		with open(rom, 'rb') as romDataFile:
			rom_data = romDataFile.read()
			
			count = 0x0200
			for byte in rom_data:
				self.memory[count] = byte
				count += 1

