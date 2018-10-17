from numpy import size

print("USING LIST:")

# initialize a list of countries
countries = ["sPain", "inDo", "franCe"]
print(countries)

# add a country at the end
countries.append("italY")
print(countries)

# remove by index
del countries[0]
print(countries)

# add a country in the middle
countries.insert(len(countries)/2, "myanMar")
print(countries)

# -------------

print("\n\nUSING SET:")

# initialize a set of countries
countriesSet = {"sPain", "inDo", "franCe"}
print(countriesSet)

# add a country at the end
countriesSet.add("italY")
print(countriesSet)

# remove by index
countriesSet.remove("sPain")
print(countriesSet)

# add a country in the middle
# cannot do this
