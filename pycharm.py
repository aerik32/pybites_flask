from random import choice

class Person:
    def  __init__(self, name):
        self.greeting = "<div>Hello There {name}</div>"
        self.name = name

    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):

        return self.greeting.format(name=self.name)


def main():

    people = [
        Person('Jane'),
        Person("Aaron"),
        Person("Ava")
    ]

    person = choice(people)
    print(person)        self.greeting = "Hello {name}"

if __name__ == '__main__':
    main()
