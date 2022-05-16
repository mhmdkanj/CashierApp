# CashierApp

CashierApp provides tools to print out a receipt given some items.
The items are taxed depending on whether the item was imported (+5%) and whether it was non-essential (+10%).

Given are three example shopping lists, whose receipts are printed out.

## Run Examples

To run the examples, execute the following in the project's root directory:

```bash
python -m cashier
```

## Usage

To use the receipt generation API provided, four classes are mainly used for that purpose:
- [Item](cashier/cash_register/item.py): models an item to be bought
- [ItemCategory](cashier/cash_register/tax_office.py): models the category of the item, which can either be:
    * Food
    * Book
    * Medical
    * Non-essential
- [Register](cashier/cash_register/register.py): models a cash register, which generates the receipt
- [Receipt](cashier/cash_register/register.py): models a receipt output from a register

You can initialize an item as follows, given some properties:

```python
from cashier.cash_register.item import Item 
item = Item(name="box of chocolates", price=10.00, category=ItemCategory.FOOD, quantity=1, imported=True)
```

To be able to process this item as if you were buying it, we need a `Register` for that:

```python
from cashier.cash_register.register import Register
register = Register()
```

To scan the item:

```python
register.process_item(item)
```

When you're done adding items, you can trigger the register to finish, output the receipt, and print it out via:

```python
from cashier.cash_register.utils import ReceiptPrinter

receipt = register.get_receipt()
ReceiptPrinter.print_receipt(receipt)
```

## Test

### Requirements

Unit tests for this app are provided and implemented using `pytest`.
To install the requirements for running the tests, execute the following in the project's root directory (preferable in a [virtual environment](https://docs.python.org/3/library/venv.html)):

```bash
pip install -r requirements-dev.txt
```

To run the tests, just execute `pytest` in the project's root directory:

```bash
pytest
```