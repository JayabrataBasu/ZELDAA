from csv import reader
from os import walk
import pygame
import os

def import_csv_layout(filename):
	abs_path = os.path.join(os.path.dirname(__file__), '..', 'map', filename)
	with open(abs_path) as level_map:
		layout = reader(level_map,delimiter = ',')
		return [list(row) for row in layout]

def import_folder(rel_folder):
	surface_list = []
	abs_folder_path = os.path.join(os.path.dirname(__file__), '..', rel_folder)
	for _,__,img_files in walk(abs_folder_path):
		for image in img_files:
			full_path = os.path.join(_, image)
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)
	return surface_list
			