# Проверка на палиндром.
import re
def check_palindrome(s):
    word =s.lower() # приводим к нижнему регистру
    word=re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', word) #удаление лишних символов, регулярное выражение
    return word == word[::-1] # сравнение с разворотом

print(check_palindrome("А роза упала на лапу Азора"))
print(check_palindrome("День на дне"))
print(check_palindrome("Алла"))
print(check_palindrome("лидер бредил"))
print(check_palindrome("искать такси"))
print(check_palindrome("ШАЛАШ"))
print(check_palindrome("Собака"))
print(check_palindrome("Аргентина манит негра"))
print(check_palindrome("Кошка"))

# Полиморфизм
class Bird:
    def fly(self):
        return "Птица летит"

class Airplane:
    def fly(self):
        return "Самолет взлетает"

def let_it_fly(entity):
    print(entity.fly())  # Вызов метода fly

# Пример использования
sparrow = Bird()
boeing = Airplane()

let_it_fly(sparrow)  # Птица летит
let_it_fly(boeing)   # Самолет взлетает

# Наследование
class Animal:
    def speak(self):
        return "Животное издает звук"

class Dog(Animal):  # Класс Dog наследует от класса Animal
    def speak(self):
        return "Гав!"

class Cat(Animal):  # Класс Cat также наследует от класса Animal
    def speak(self):
        return "Мяу!"

# Пример использования
dog = Dog()
cat = Cat()

print(dog.speak())  # Гав!
print(cat.speak())  # Мяу!

# Инкапсуляция
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # публичное свойство
        self.__balance = balance  # приватное свойство

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} добавлено. Текущий баланс: {self.__balance}")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} снято. Текущий баланс: {self.__balance}")
        else:
            print("Недостаточно средств или неверная сумма.")

    def get_balance(self):
        return self.__balance  # Метод доступа к приватному свойству

# Пример использования
account = BankAccount("Иван")
account.deposit(100)
account.withdraw(50)
print(account.get_balance())  # Текущий баланс: 50
# print(account.__balance)  # Ошибка: 'BankAccount' object has no attribute '__balance'
#проверка апдейта