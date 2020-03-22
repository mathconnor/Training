# This is the class blueprint for a GPU Object. ---------------------|
import pygame
from pygame import Rect


class GPU():
	def __init__(self):
		self.black = 0,0,0									# Define the color black.
		self.white = 255,255,255							# Define the color white.
		self.colors = [self.black, self.white]				# Colors listing.
		
		self.width = 64										# Sets Max Screen Width.
		self.height = 32									# Sets Max Screen Height.
		self.pixels = self.width * self.height				# Calculate the total number of pixels (2,048‬ max).
		self.size = self.width * 10, self.height * 10		# Scale Screen to larger size.

		# Initialize GPU Memory
		self.graphics_memory = [0x00] * self.pixels			# The main graphics memory for the GPU (2,048k)

		# CPU Connection Variable
		self.cpu = 0										# Connects the GPU to the CPU.


	def screen(self):
		# Build Main Screen
		self.screen = pygame.display.set_mode(self.size)	# Creates a blank window. Window is scaled according to self.size.
		
		# Display an initial blank screen.
		self.screen.fill((0,0,0))							# Sets all pixels to black and starts the screen.


	def draw_graphics(self):
		# Draw entire screen using data stored in GPU memory.
		for scanline in range(self.height):					# For each scanline that makes up the screen (32 in total)
			for pixel_in_scanline in range(self.width):		# Process each pixel in the current scanline.
				self.screen.fill( self.colors[self.graphics_memory[pixel_in_scanline + (scanline * self.width)]], Rect(pixel_in_scanline*10, scanline*10, 10, 10) )
				
		pygame.display.flip()								# Update the screen with the new data.
		self.cpu.draw_flag = False							# Disable the CPU draw flag.

