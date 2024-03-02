inp = "ABCA"
dictval = dict()
for i in range(len(inp)) :
    if inp.count(inp[i]) >1 :
        dictval[inp[i]] = inp.count(inp[i])

for key , value in dictval.items():
    print("character : "+key)
    print("NUmber of iterations : " + str(value))

