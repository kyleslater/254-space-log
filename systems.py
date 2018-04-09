#Jose Alvarado
import re

def solar_systems(content:str):
	pattern = re.compile("\"event\":\"FSDJump\",\s\"StarSystem\":\"[-\w+\s\d+]+\"")
	systems = pattern.findall(content)
	return systems
