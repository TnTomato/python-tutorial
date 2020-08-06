foo = 10
bar = 'Sam'


# Python now has type hints, in order to indicate variable's type
a: int = 10
b: float = 10.5
c: complex = 2 + 3j
d: bool = True

result = a + b
print(result, type(result))


# String
sentence1 = "Nice to meet you."
sentence2 = 'Nice to meet you.'

sentence3 = "Sam said 'Nice to meet yuo' to John."
# or
sentence4 = 'Sam said \'Nice to meet yuo\' to John.'

sentence5 = 'Hello every one. Nice to meet all of you. My name is Sam ' \
            'and I am 25 years old. I am a software engineer.'
# or
sentence6 = '''Hello every one. Nice to meet all of you. My name is Sam
 and I am 25 years old. I am a software engineer.'''
# or
sentence7 = """Hello every one. Nice to meet all of you. My name is Sam
 and I am 25 years old. I am a software engineer."""


# List
animals = ['dog', 'cat', 'tiger', 'wolf', 'rabbit']
numbers = [111, 222, 333, 444, 555]

print(animals[0])  # The first element
print(animals[:2])  # The first to the index value 2 element slice, but index value 2 element is excluded
print(animals[2:])  # The index value 2 to the last element slice
print(animals[2:-1])  # The index value 2 to the last element slice, but the last element is excluded
print(animals[2:4])  # The index value 2 to the index value 4 element slice, but the index value 4 element is excluded
print(animals[:])  # The first to the last element slice(copy the list)


# Dictionary
sam = {
    'name': 'Sam',
    'age': 20,
    'hobbies': ['basketball', 'pcgames'],
    'pets': [
        {
            'type': 'dog',
            'name': 'Bob',
            'age': 2,
        },
        {
            'type': 'cat',
            'name': 'Alice',
            'age': 1
        }
    ]
}

print(sam['name'])  # Sam
print(sam.get('age'))  # 20
print(sam['pets'][0]['type'])  # dog
print(sam.get('gender'))  # None
