names = ["alex", "jack", "john", "alan", "mary", "nicole", "jack"]

# print(type(names))

print(names[1])
print(names.index("alex"))
print(names[2:])
print(names.count("jack"))

names.append("goose")
names.insert(5, "mike")

print(names)
names.pop(3)
names.remove("jack")
print(names)

names[names.index("jack")] = "pony"
print(names)


