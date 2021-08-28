# Private Fields


<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="https://www.loom.com/embed/de5c457d29854cad9093650e160fc9da?sharedAppSource=personal_library" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>


```{admonition} Tip
:class: tip

Recall: a Python file is also called a
**module.**


```

Suppose you work at a bank and want to write a program to model someone's bank account. We might start by writing a class like so in a file `bank_account.py` . For this reading, we can't actually create a file called `bank_account.py` so we leave a `#` comment at the top saying what file this would be in if we were in a real Python project.  

A few things to notice:  

-  You can (and should) add a doc-string to the class itself! This will describe what the class is used for. You put it as the first thing after the class header.  

-  The naming convention for classes is     `CapitalCase`     rather than     `snake_case`     . The naming convention for variables, fields, and method names is still     `snake_case`     .  


```python
# Written in bank_account.py

class BankAccount:
    """
    A class that represents a bank account owned by a single person.
    """
    
    def __init__(self, owner, initial_deposit):
        """
        Constructs a BankAccount starting with the initial_deposit for the
        given owner
        """
        self.owner = owner
        self.amount = initial_deposit
        
    def deposit(self, amount):
        """
        Adds the given amount to this BankAccount. 
        Returns the new amount
        """
        self.amount += amount
        return self.amount
        
    def withdraw(self, amount):
        """
        Withdraws the given amount from this bank account, returning 
        the remaining balance. If there are not sufficient funds for 
        this withdrawal, does not do the transaction and returns None.
        """
        if self.amount < amount:
            return None
        else:
            self.amount -= amount
            return self.amount
        
    def to_string(self):
        """
        Returns a string representation of this BankAccount, in the format:
           "Bank Account for {owner}: {amount}"
        """
        return 'Bank Account for ' + self.owner + ': ' + str(self.amount)
```

This seems great and we can make sure that someone's balance never goes negative. However, the client can still write something like this to break our `BankAccount` .  

```python
bank = BankAccount('Nicole', 20)
bank.withdraw(400) # Returns None because I don't have enough money
bank.amount = 200000000 
bank.withdraw(400) 

# Maybe feeling more malicious
bank.amount = "I don't need any money!"
bank.withdraw(20)  # Crashes because it compares a str to an int!
```

What happened here? As a client (outside the object), we accessed its `amount` field and changed it to a value we wanted. Python allows you to access the fields of an object, just like you can access its methods (by using the `.` syntax). This is not ideal since now the client can arbitrarily violate any things we wanted to assume about our state (e.g. the `amount` is a non-negative `int` ).  

What we want to do is to restrict the client so they can't access the fields and instead have to go through the methods to deposit/withdraw money. To do this, we need to make the fields **private** so the client can't access them.  

Some languages have ways of enforcing this notion of having a private field (one where a client can't access it from outside the class), but Python does not. Instead, Python has a convention that everyone follows:  

> If a field name starts with an underscore (i.e. '_'), it is considered private and you shouldn't access it (to either read the value or modify it).
Technically, this is not enforced by the language itself. This means someone *could* violate this rule and access the private field, but that doesn't mean they *should* . There is usually no public-facing documentation describing these private fields, so you would be making assumptions about how they work; this will almost surely cause your programs to have bugs. Additionally, the Python community takes respecting privacy very seriously so they might call the Python-police on you if they see you doing that.  

To make our fields private, we would rewrite the class so that the field names were `self._owner` and `self._amount` like in the following code block.  


```{admonition} Warning
:class: warning

For every class you write in CSE 163, you should make all fields private unless specified otherwise! What this means is if we ask you to make a field called
`amount`
, you should really name it
`_amount`
to indicate that it is private.

```

```python
# Written in bank_account.py

class BankAccount:
    """
    A class that represents a bank account owned by a single person.
    """
    
    def __init__(self, owner, initial_deposit):
        """
        Constructs a BankAccount starting with the initial_deposit for the
        given owner
        """
        self._owner = owner
        self._amount = initial_deposit
        
    def deposit(self, amount):
        """
        Adds the given amount to this BankAccount. 
        Returns the new amount
        """
        self._amount += amount
        return self._amount
        
    def withdraw(self, amount):
        """
        Withdraws the given amount from this bank account, returning 
        the remaining balance. If there are not sufficient funds for 
        this withdrawal, does not do the transaction and returns None.
        """
        if self._amount < amount:
            return None
        else:
            self._amount -= amount
            return self._amount
        
    def to_string(self):
        """
        Returns a string representation of this BankAccount, in the format:
           "Bank Account for {owner}: {amount}"
        """
        return 'Bank Account for ' + self._owner + ': ' + str(self._amount)
```

