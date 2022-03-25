# # infile1 = open('States.txt', 'r')
# # for line in infile1:
# #     print(line)
#
# infile2 = open('States.txt', 'r')
# ldata = [line.rstrip() for line in infile2]
# print(ldata)
# ldata.sort()
# print(ldata)
#
# outfile = open('StatesAlpha.txt', 'w')
# outfile.writelines(ldata)
# infile2.close()
# outfile.close()

infile1 = open('USPres.txt', 'r')
infile2 = open('VPres.txt', 'r')

sdata1 = {line for line in infile1}
sdata2 = {line for line in infile2}

idata = sdata1.intersection(sdata2)
print(idata)

outfile1 = open('bdata.txt', 'w')
outfile1.writelines(idata)
outfile1.close()

ldata = sorted(idata)
print(ldata)

outfile2 = open('bdata2.txt', 'w')
outfile2.writelines(ldata)
outfile2.close()