def sqInRect(lng, wdth):
	if lng==wdth:
		return None
	result = []
	if lng<wdth:
		lng,wdth=wdth,lng
	while lng>wdth:
		result.append(wdth)
		if lng-wdth==wdth:
			result.append(wdth)
		elif lng-wdth>wdth:
			lng = lng-wdth
		else:
			lng,wdth = wdth,lng-wdth
	return result

print(sqInRect(5,3))