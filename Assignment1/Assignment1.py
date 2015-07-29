import ReadWrite as RW


linesFile = RW.readFile('grvfld.ggm02s')
ggm02s = RW.organizeLines(linesFile)


# print(ggm02s)
f = open('new.txt', 'w')

for i,j in ggm02s.items():
	# print(j.coeff,j.m,j.n,j.value)
	f.write(str(j.coeff)+'  '+str(j.m)+' '+str(j.n)+'    '+str(j.value)+'\n')



print(ggm02s['S 160 16'].value)

