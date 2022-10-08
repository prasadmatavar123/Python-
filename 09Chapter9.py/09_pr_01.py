f = open('poems.txt')
t = f.read()
if 'Twinkel' in t:
    print("Twinkel is present")
else:
    print("Twinkel is not present")    
f.close()