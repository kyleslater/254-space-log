import re

def terraformable(content:str):
	pattern = re.compile("\"TerraformState\":\"Terraformable\"")
	matches = pattern.findall(content)
	return len(matches)