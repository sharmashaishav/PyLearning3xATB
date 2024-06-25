letters=['a','s','u','c','v','e','z','i','o','l']

def get_vowels(n):
    vowels=['a','e','i','o','u']
    return n in vowels

result = get_vowels('v')
print(result)

filter_vowels=list(filter(get_vowels,letters))
print(filter_vowels)

# If we use MAP function instead of FILTER it will return as many items as there are in the list/tuple/set
map_vowels=list(map(get_vowels,letters))
print(map_vowels)