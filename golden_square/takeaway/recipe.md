## User stories

> As a customer <br>
> So that I can check if I want to order something <br>
> I would like to see a list of dishes with prices.

<br>

> As a customer <br>
> So that I can order the meal I want <br>
> I would like to be able to select some number of several available dishes.

<br>

> As a customer <br>
> So that I can verify that my order is correct <br>
> I would like to see an itemised receipt with a grand total.

<br>

> As a customer <br>
> So that I am reassured that my order will be delivered on time <br>
> I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## Design the Class System

<img width="952" alt="Screenshot 2023-05-03 at 15 31 54" src="https://user-images.githubusercontent.com/93719632/235957439-bf273460-7afa-4f1e-99a5-aa328946fa32.png">

##### I'm aware this doesn't quite match up!

## Class Interface

```python
class Menu:
    # User-facing properties:
    #   dishes: list of instances of Dish

    def __init__(self):
        pass

    def list_dishes(self):
        # Returns:
        #   list of dishes (str of index, title and price)
        pass

class Dish:
    # User-facing properties:
    #   title: str, title of the meal
    #   price: int, price of the meal
    def __init__(self, title, price):
        # Side Effects:
        #   adds meal and price properties of the self object
        pass

class Order:
    # User-facing properties:
    #   dishes: list of instances of Dish the customer wants to order

    def __init__(self):
        pass

    def add_to_order(self, dish):
        # Parameters:
        #   dish: instance of Dish customer wants to order
        # Side Effects:
        #   adds dish to list of dishes customer wants to order
        pass

class Receipt:
    def __init__(self, order):
        # Parameters:
        #   order: instance of Order customer made
        # Side Effects:
        #   adds order to the order property of the self object
        pass

    def grand_total(self):
        # Side Effects:
        #   grand total of all dishes ordered as a float
        pass


class SMS:
    def __init__(self, receipt):
        # Parameters:
        #   receipt: instance of Receipt
        # Side Effects:
        #   adds receipt to the receipt property of the self object
        pass

    def send(self):
        # Side Effects:
        #   sends an SMS to the customer's phone confirming their order
        pass
```

## Integration tests

```python

"""
When I ask to see the menu
I see a list of dishes (their name and price)
"""

"""
I can add dishes to my order, some in duplicate
"""

"""
Once I have confirmed my order I ask for an itemised receipt
Returns the total amount I owe for all of the dishes I have ordered
"""

"""
Once I have submitted my order
I receive SMS confirmation as an itemised receipt
"""



```

## Unit tests

### Menu

```python
"""
When there are no dishes
Returns an empty list
"""

"""
When mock dishes are added
Returns a list of dishes showing their name and price
"""

```

### Dish

```python
"""
When a dish is created with a string for price
An error is thrown
"""

"""
When a dish is created with an integer for price
The price is converted into a float
"""

"""
When a dish is created with None for title
An error is thrown
"""

"""
When a dish is created with an empty string
An error is thrown
"""

"""
When a dish is created with a price equal to or less than zero
An error is thrown
"""
```

### Order

```python
"""
When there are no dishes
Returns an empty dictionary
"""

"""
When mock dishes are added
Returns a dictionary of Mock dishes
"""

"""
When anything other than an instance of Dish is added
An error is thrown
"""

"""
When an item already in the dictionary is added
The dish is not added to the dictionary but the number of that dish goes up by one
"""
```

### Receipt

```python

"""
When anything other than an instance of Order is being added
An error is thrown
"""

"""
When there are no dishes in an order
An error is thrown
"""

"""
When an order has multiple mock dishes
The correct grand total is shown
"""

"""
When an order has multiple of the same mock dish
The correct grand total is shown
"""
```

### SMS

```python

"""
When anything other than an instance of Receipt is being added
An error is thrown
"""

"""
When grand total of a Receipt is zero
An error is thrown
"""

"""
When a user wants to confirm their order
Returns correct SMS message and grand total to user's phone
"""
```
