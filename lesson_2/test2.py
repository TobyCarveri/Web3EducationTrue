from typing import Union
from decimal import Decimal
from dataclasses import dataclass

import time

'''
Token:
    name
    address
    balance
'''

tokens_dict = {
    'ETH': {
        'address': '0x00000000000000000000000000000000000000',
        'balance': 1000000000000000000
    },
    'USDC': {
        'address': '0xIu67bubyTG23GBybuyb72672367826374gVHH76',
        'balance': 1000000
    }
}

'''
аннотоции типов
dicimals
try
'''

class TokenAmount:
    Wei: int
    Ether: Decimal
    decimals: int

    def __init__(self, amount: Union[int, float, str, Decimal], decimals: int = 18, wei: bool = False) -> None:
        if wei:
            self.Wei: int = amount
            self.Ether: Decimal = Decimal(str(amount)) / 10 ** decimals

        else:
            self.Wei: int = int(Decimal(str(amount)) * 10 ** decimals)
            self.Ether: Decimal = Decimal(str(amount))

        self.decimals = decimals

    # def __str__(self):
    #     return f'{self.Ether}'


amount = TokenAmount(amount=1000000000000000000000, wei=True)
print(amount.Ether)


class Token:
    def __init__(self, name: str, address: str, balance: TokenAmount):
        self.name = name
        self.address = address
        self.balance = balance


    def __str__(self) -> str:
        return f'{self.name}: {self.balance}'


class Tokens:
    ETH = Token(
        name='ETH',
        address='0x00000000000000000000000000000000000000',
        balance=TokenAmount(amount=1),
    )
    USDC = Token(
        name='USDC',
        address='0xIu67bubyTG23GBybuyb72672367826374gVHH76',
        balance=(TokenAmount(amount=532, decimals=6).Ether),
    )
print(Tokens.USDC)

@dataclass
class API:
    key: str
    url: str
    docs: str


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __add__(self, other):
        return Person(name=self.name + "years + " + other.name + ' years =', age=self.age + other.age)

    def __str__(self):
        return f'{self.name} | {self.age}'


persor_a = Person(name='Bob', age=20)
persor_b = Person(name='Alice', age=21)


# a = persor_a + persor_b
# print(a.__str__()), print(type(a.__str__())),


print(persor_a + persor_b), print((persor_a + persor_b).__str__())
# print(persor_a - persor_b)
# print(persor_a * persor_b)
# print(persor_a / persor_b)
print(persor_a == persor_b)
print(persor_a != persor_b)

# print(persor_a > persor_b)
# print(persor_a < persor_b)
#
#


@dataclass
class Person2:
    name: str
    age: int

    def __add__(self, other):
        return Person(name=self.name + "years + " + other.name + ' years =', age=self.age + other.age)


persor_a = Person2(name='Bob', age=20)
persor_b = Person2(name='Alice', age=21)


# a = persor_a + persor_b
# print(a.__str__()), print(type(a.__str__())),


print(persor_a + persor_b), print(type((persor_a + persor_b).__str__()))
print(persor_a == persor_b)
print(persor_a != persor_b)








