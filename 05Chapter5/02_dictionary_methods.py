a = {"name": "Harry",
     "From": "India",
     "Marks": [92,98,96]}
print(a.items())
print(a.keys())
print(a.values())
print(a)
updateDict ={"friends":"Sam"}
a.update(updateDict)
print(a)
print(a.get("Harry"))
b ={"data ": "The value of store",
     "opend ": "The value of art"}
print(b.get("data"))     