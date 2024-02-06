f = open("input.txt", "r")
s = f.readlines()
#test = "ACGTCGTGTT"


result = open("output.txt", "x")


for line in s:
    curr = line.strip()
    res = ""
    resdict = {}
    for i in curr:
        if i in resdict:
            resdict[i] += 1
        else:
            resdict[i] = 1
    res += str(resdict["A"]) +" "
    res += str(resdict["C"]) +" "
    res += str(resdict["G"]) +" "
    res += str(resdict["T"])

    result.write(res+"\n")
        
#contains exactly 4 integers separated by spaces 
# that represent the numbers of each letter in the order specified above.
#append number of As

result.close()
f.close()
