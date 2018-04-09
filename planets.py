#Ivan Parrales
import re

def print_planets(content:str):
	pattern = re.compile("\"event\":\"Scan\",\s\"BodyName\":\"[-\w+\s\d+]+\"")
	matches = pattern.findall(content)
	for match in matches:
		print(match)
