# Chip8 Main File
import sys
import os
import chip8_cpu
import chip8_memory
import chip8_gpu
import chip8_events

os.system( 'cls' )

def main(rom, debug):
	# Create system component objects.
	cpu_part	= chip8_cpu.CPU()					# Create a CPU Object from the chip8_cpu.py class file.
	memory_part	= chip8_memory.MMU()				# Create a Memory Object from the chip8_memory.py class file.
	gpu_part	= chip8_gpu.GPU()					# Create a GPU Object from the chip8_gpu.py class file.
	events_part	= chip8_events.EVENTS()				# Create an Events Object from the chip8_events.py class file.
	
	# Connect the parts that need to be connected.
	cpu_part.system_memory = memory_part			# Connect the CPU to the system memory.
	cpu_part.gpu_memory = gpu_part					# Connect the CPU to the GPU.
	gpu_part.cpu = cpu_part							# Connect the GPU to the CPU.
	
	# Loading ROM into Memory
	memory_part.loadROM(rom)
	
	# Turn on the Screen
	if debug == '0':
		gpu_part.screen()

	
	# CPU Main Loop
	# Run an infinite loop of calling the CPU tick() function, returning any results after each "tick",
	# check for any outside events that happened during the "tick", and then draw any graphics to the screen.
	while True:
		if debug == '1':
			while True:
				step = input( "\nPress the Enter Key to step to the next Instruction. Press 'q' to quit: " )
				os.system( 'cls' )

				if step == '':
					cpu_part.tick()
					print( "******************* CPU Debug Data *******************" )
					print( "General Purpose Register Data" )
					print( "V00:", format(cpu_part.V[0], '02x'), "\t", end="", flush=True )
					print( "V08:", format(cpu_part.V[8], '02x') )
					print( "V01:", format(cpu_part.V[1], '02x'), "\t", end="", flush=True )
					print( "V09:", format(cpu_part.V[9], '02x') )
					print( "V02:", format(cpu_part.V[2], '02x'), "\t", end="", flush=True )
					print( "V10:", format(cpu_part.V[10], '02x') )
					print( "V03:", format(cpu_part.V[3], '02x'), "\t", end="", flush=True )
					print( "V11:", format(cpu_part.V[11], '02x') )
					print( "V04:", format(cpu_part.V[4], '02x'), "\t", end="", flush=True )
					print( "V12:", format(cpu_part.V[12], '02x') )
					print( "V05:", format(cpu_part.V[5], '02x'), "\t", end="", flush=True )
					print( "V13:", format(cpu_part.V[13], '02x') )
					print( "V06:", format(cpu_part.V[6], '02x'), "\t", end="", flush=True )
					print( "V14:", format(cpu_part.V[14], '02x') )
					print( "V07:", format(cpu_part.V[7], '02x'), "\t", end="", flush=True )
					print( "V15:", format(cpu_part.V[15], '02x') )
					
					'''
					Easy method without using special print() arguments.
					print( "V00:", format(cpu_part.V[0], '02x'), "\t", "V08:", format(cpu_part.V[8], '02x') )
					print( "V01:", format(cpu_part.V[1], '02x'), "\t", "V09:", format(cpu_part.V[9], '02x') )
					print( "V02:", format(cpu_part.V[2], '02x'), "\t", "V10:", format(cpu_part.V[10], '02x') )
					print( "V03:", format(cpu_part.V[3], '02x'), "\t", "V11:", format(cpu_part.V[11], '02x') )
					print( "V04:", format(cpu_part.V[4], '02x'), "\t", "V12:", format(cpu_part.V[12], '02x') )
					print( "V05:", format(cpu_part.V[5], '02x'), "\t", "V13:", format(cpu_part.V[13], '02x') )
					print( "V06:", format(cpu_part.V[6], '02x'), "\t", "V14:", format(cpu_part.V[14], '02x') )
					print( "V07:", format(cpu_part.V[7], '02x'), "\t", "V15:", format(cpu_part.V[15], '02x') )
					'''
					# Special Purpose Registers ***************************************************
					print( "\nSpecial Purpose Registers Data" )
					print( "PC Register  :", format(cpu_part.pc, '04x') )
					
					# Special Purpose Registers ***************************************************
					print( 'Stack Pointer:', format(cpu_part.sp, '04x') )
					print( 'CPU Stack' )
					for k, v in enumerate(cpu_part.stack):
						print( str(k)+':', '\t', format(v, '04x') )
					print( '\nNext Instruction Address:', format(cpu_part.instruction, '04x') )
					
					# Memory Dump *****************************************************************
					print( '\nSystem Memory:' )

					for k in range(0, 10, 2):	# 10 / 2 = 5 lines to print
						print( '\n', format(cpu_part.pc + k, '04x') + ':', '\t', end="", flush=True )
						for v in range(0, 2):	# 2 = 16-bit chunks
							if v <= 1:
								print( format( memory_part.read((cpu_part.pc + k) + v), '02x' ), '\t', end="", flush=True )
					print( '\n' )

				elif step == 'q':
					sys.exit()

		else:
			while True:
				cpu_part.tick()
				# INSERT EVENT CHECK CODE HERE
			
				# INSERT DRAW GRAPHICS CODE HERE
				if cpu_part.draw_flag == True:
					gpu_part.draw_graphics()
			
				# End CPU loop.

				

if __name__ == '__main__':
	if len( sys.argv ) == 3:
		main( sys.argv[1], sys.argv[2] )
	else:
		print( "Usage: py chip8_main.py [rom_file] [Debug Mode: 0 = off, 1 = on]" )

