# Implement a simple playfair cipher
# Problem description here:
# https://open.kattis.com/problems/playfair

alpha = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
cipher = {}
graph = {}
cipherKeys = cipher.keys()
key = input().upper().replace(" ", "")
plain = input().upper().replace(" ", "")

def build(phrase, row, col):
	for i in range(len(phrase)):
		if(col % 6 == 0):
			row +=1
			col = 1
		if(not phrase[i] in cipherKeys):
			cipher[phrase[i]] = (row, col)
			graph[(row, col)] = phrase[i]
			col += 1
	return row, col
    
r, c = build(key, 0,0)
build(alpha, r, c)

pairs = []
i = 0
while(i < len(plain)):
	if (i < len(plain)-1):
		if (plain[i] == plain[i+1]):
			pairs.append([plain[i], "X"])
			plain = plain[:i+1]+"X"+plain[i+1:]
		else:
			pairs.append([plain[i],plain[i+1]])
	else:
		pairs.append([plain[-1], "X"])
	i += 2

encoded = ""

for pair in pairs:
	y1 = cipher[pair[0]][0]
	x1 = cipher[pair[0]][1]
	y2 = cipher[pair[1]][0]
	x2 = cipher[pair[1]][1]
        
	if (y1 == y2):
		encoded = encoded + graph[(y1,((x1%5) + 1))] + graph[(y2,((x2 % 5) + 1))]
	elif (x1 == x2):
		encoded = encoded + graph[((y1 % 5) + 1,x1)] + graph[((y2 % 5) + 1,x2)]
	else:
		encoded = encoded + graph[(y1, x2)] + graph[(y2, x1)]
            
print(encoded)
