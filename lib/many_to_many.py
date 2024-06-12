class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all_instances if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})


class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all_instances if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book type. Must be an instance of Book.")
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all_instances = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author type. Must be an instance of Author.")
        if not isinstance(book, Book):
            raise Exception("Invalid book type. Must be an instance of Book.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all_instances.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        contracts = sorted(cls.all_instances, key=lambda x: x.date)
        return [contract for contract in contracts if contract.date == date]
