"""
Electronics Stock Management System
===================================
A console-based inventory and sales manager with persistent JSON storage.
Data (stock, prices, discounts, offers, balance) and a transaction log
(history) survive across restarts via two JSON files.

Author: Om Singh Rajput
"""

import json
import os
import pandas as pd


# ----------------- Configuration -----------------
DATA_FILE = "stock_data.json"        # stock, prices, discounts, offers, balance
HISTORY_FILE = "stock_history.json"  # transaction log (Lekh)

ADMIN_PASSWORD = "Chabhi"   # full management access
USER_PASSWORD = "Khulja"    # sales / operations access
MAX_LOGIN_ATTEMPTS = 2


# ----------------- Default data -----------------
def default_state():
    """Return a fresh copy of the default state (used on very first run)."""
    return {
        "Stock": {"iPad": 15, "iPhone": 20, "Mac": 25, "iBuds": 50},
        "Item_Price": {"iPad": 150000, "iPhone": 196000, "Mac": 250000, "iBuds": 18000},
        "Item_discount": {"iPad": 5, "iPhone": 5, "Mac": 5, "iBuds": 5},
        "Item_offer": {"iPad": 0, "iPhone": 0, "Mac": 0, "iBuds": 0},
        "Balance": 5000000,
        "Lekh": [["S.No.", "Operation", "Input", "Value", "Comment"]],
        "k1": 0,
    }


# ----------------- Persistence helpers -----------------
def load_data():
    """Load saved state from JSON files; return defaults if files are missing."""
    state = default_state()

    # Load main data file
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
            for key in ("Stock", "Item_Price", "Item_discount", "Item_offer", "Balance"):
                if key in data:
                    state[key] = data[key]
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not read data file. Using defaults.\n")

    # Load history file
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                state["Lekh"] = json.load(f)
            # Recompute k1 from the last numeric serial number in history
            state["k1"] = 0
            for row in state["Lekh"][1:]:  # skip header row
                try:
                    state["k1"] = max(state["k1"], int(row[0]))
                except (ValueError, IndexError):
                    pass
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not read history file. Using empty history.\n")

    return state


def save_data(state):
    """Write current state and history to JSON files."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump({
                "Stock": state["Stock"],
                "Item_Price": state["Item_Price"],
                "Item_discount": state["Item_discount"],
                "Item_offer": state["Item_offer"],
                "Balance": state["Balance"],
            }, f, indent=4)
    except IOError as e:
        print(f"Warning: Could not save data file: {e}")

    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(state["Lekh"], f, indent=4)
    except IOError as e:
        print(f"Warning: Could not save history file: {e}")


def log_entry(state, operation, inp, value, comment):
    """Append a row to the transaction history and advance the serial counter."""
    state["k1"] += 1
    state["Lekh"].append([str(state["k1"]), operation, str(inp), str(value), comment])


def effective_price(state, item):
    """Return the selling price after applying discount and offer percentages."""
    base = state["Item_Price"].get(item, 0)
    discount = state["Item_discount"].get(item, 0)
    offer = state["Item_offer"].get(item, 0)
    return base - (base * (discount + offer) / 100)


# ----------------- Admin menu -----------------
def manage_stock(state):
    """Sub-menu for stock-related updates (admin)."""
    while True:
        print(state["Stock"])
        print("1. New Stock\n"
              "2. Stock Update\n")
        try:
            choice2 = int(input("Enter: "))
        except ValueError:
            print("Enter a valid number.\n")
            choice2 = None

        if choice2 == 1:
            while True:
                key = input("Enter product name: ")
                try:
                    qty = int(input("Enter product quantity: "))
                    price = int(input("Enter product price: "))
                    disc = int(input("Enter product discount (%): "))
                    offer = int(input("Enter product offer (%): "))
                except ValueError:
                    print("Invalid number entered. Skipping.\n")
                    break
                # NOTE: original code did Stock.clear() here, wiping everything.
                # We now ADD the item instead of replacing the whole stock.
                state["Stock"][key] = qty
                state["Item_Price"][key] = price
                state["Item_discount"][key] = disc
                state["Item_offer"][key] = offer
                save_data(state)
                if input("Add another? (0=yes): ") != "0":
                    break

        elif choice2 == 2:
            while True:
                print("1. Add Item\n"
                      "2. Quantity Update\n")
                try:
                    k3 = int(input("Enter: "))
                except ValueError:
                    print("Enter a valid number.\n")
                    k3 = None
                if k3 == 1:
                    key = input("Enter product name: ")
                    try:
                        value = int(input("Enter product quantity: "))
                    except ValueError:
                        print("Invalid quantity.\n")
                        continue
                    state["Stock"][key] = value
                    save_data(state)
                elif k3 == 2:
                    key = input("Enter product name: ")
                    if key in state["Stock"]:
                        print(key, ":", state["Stock"].get(key))
                        try:
                            state["Stock"][key] = int(input("Enter new quantity: "))
                            save_data(state)
                        except ValueError:
                            print("Invalid quantity.\n")
                    else:
                        print("Item not found.\n")
                else:
                    print("Enter a valid number.\n")
                if input("Another stock update? (0=yes): ") != "0":
                    break
        else:
            print("Enter a valid number.\n")

        if input("Any other stock update? (0=yes): ") != "0":
            break


def manage_prices(state):
    """Update item prices (admin)."""
    print(state["Item_Price"])
    while True:
        print("1. Price Update\n")
        try:
            k3 = int(input("Enter: "))
        except ValueError:
            print("Enter a valid number.\n")
            k3 = None
        if k3 == 1:
            key = input("Enter product name: ")
            print(key, ":", state["Item_Price"].get(key))
            try:
                state["Item_Price"][key] = int(input("Enter new price: "))
                save_data(state)
            except ValueError:
                print("Invalid price.\n")
        else:
            print("Enter a valid number.\n")
        if input("Another price update? (0=yes): ") != "0":
            break


def manage_discounts(state):
    """Update item discounts (admin)."""
    print(state["Item_discount"])
    while True:
        print("1. Discount Update\n")
        try:
            k4 = int(input("Enter: "))
        except ValueError:
            print("Enter a valid number.\n")
            k4 = None
        if k4 == 1:
            key = input("Enter product name: ")
            print(key, ":", state["Item_discount"].get(key))
            try:
                state["Item_discount"][key] = int(input("Enter new discount (%): "))
                save_data(state)
            except ValueError:
                print("Invalid discount.\n")
        else:
            print("Enter a valid number.\n")
        if input("Another discount update? (0=yes): ") != "0":
            break


def manage_offers(state):
    """Update item offers (admin)."""
    print(state["Item_offer"])
    while True:
        print("1. Offer Update\n")
        try:
            k5 = int(input("Enter: "))
        except ValueError:
            print("Enter a valid number.\n")
            k5 = None
        if k5 == 1:
            key = input("Enter product name: ")
            print(key, ":", state["Item_offer"].get(key))
            try:
                state["Item_offer"][key] = int(input("Enter new offer (%): "))
                save_data(state)
            except ValueError:
                print("Invalid offer.\n")
        else:
            print("Enter a valid number.\n")
        if input("Another offer update? (0=yes): ") != "0":
            break


def manage_balance(state):
    """Add, subtract, or reset the balance (admin)."""
    print("Current Balance:", state["Balance"])
    print("1. Add Amount\n"
          "2. Subtract Amount\n"
          "3. New Balance\n")
    try:
        choice = int(input("Enter: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return
    if choice == 1:
        state["Balance"] += int(input("Amount: "))
    elif choice == 2:
        state["Balance"] -= int(input("Amount: "))
    elif choice == 3:
        state["Balance"] = int(input("Enter: "))
    else:
        print("Please enter a valid input.\n")
        return
    save_data(state)


def show_history(state):
    """Display the transaction log as a DataFrame."""
    log_entry(state, "History", "-", "-", "Successful")
    save_data(state)
    df = pd.DataFrame(state["Lekh"])
    print(df)


def admin_menu(state):
    """Main admin management menu."""
    while True:
        print("Make any update:\n"
              "1. Stock\n"
              "2. Item Price\n"
              "3. Item Discount\n"
              "4. Item Offer\n"
              "5. Balance\n"
              "6. History\n")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Please enter a valid input.\n")
            continue

        if choice == 1:
            manage_stock(state)
        elif choice == 2:
            manage_prices(state)
        elif choice == 3:
            manage_discounts(state)
        elif choice == 4:
            manage_offers(state)
        elif choice == 5:
            manage_balance(state)
        elif choice == 6:
            show_history(state)
        else:
            print("Please enter a valid input.\n")

        if input("Continue admin? (0=yes): ") != "0":
            break


# ----------------- User (operations) menu -----------------
def show_stock(state):
    """Show the full stock dictionary."""
    print("\n", state["Stock"])
    log_entry(state, "Show Stock", "-", "-", "Successful")
    save_data(state)


def show_item(state):
    """Show details of a single item."""
    name = input("\nEnter name: ")
    if name in state["Stock"]:
        price = effective_price(state, name)
        print(f"\n{name}: {state['Stock'][name]}\nPrice: {price}")
        log_entry(state, "Show item", name, state["Stock"][name], "Successful")
    else:
        print("\nNo item found.")
        log_entry(state, "Show item", name, "-", "No item found.")
    save_data(state)


def add_stock_quantity(state):
    """Purchase more quantity of an existing item (reduces balance)."""
    name = input("Enter name: ")
    if name in state["Stock"]:
        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity.\n")
            return
        cost = qty * state["Item_Price"].get(name, 0)
        if state["Balance"] - cost < 0:
            print("No required balance.")
            log_entry(state, "Add quantity", name, "-", "Unsuccessful")
        else:
            state["Stock"][name] += qty
            state["Balance"] -= cost
            print(name, ":", state["Stock"][name])
            log_entry(state, "Add quantity", name, qty, state["Stock"][name])
    else:
        print("Item not found.")
        log_entry(state, "Add quantity", name, "-", "Item not found")
    save_data(state)


def sell_item(state):
    """Sell quantity of an item (increases balance by effective price)."""
    name = input("\nEnter name: ")
    if name in state["Stock"]:
        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity.\n")
            return
        if state["Stock"][name] - qty >= 0:
            state["Stock"][name] -= qty
            revenue = qty * effective_price(state, name)
            state["Balance"] += revenue
            print(name, ":", state["Stock"][name])
            log_entry(state, "Sell Item", name, qty, state["Stock"][name])
        else:
            print("\nNot enough stock available.")
            log_entry(state, "Remove quantity", name, qty, "Insufficient stock")
    else:
        print("\nNo item found.")
        log_entry(state, "Remove quantity", name, "-", "No item found")
    save_data(state)


def add_new_item(state):
    """Add a brand-new item to the inventory."""
    name = input("\nEnter name: ")
    if name in state["Stock"]:
        print(f"\n{name} is in stock.\n{name}: {state['Stock'][name]}")
        log_entry(state, "Add item", "-", "-", "Unsuccessful")
    else:
        try:
            qty = int(input("Enter quantity: "))
            unit_price = int(input("Enter unit price: "))
            disc = int(input("Enter discount (%): "))
            offer = int(input("Enter offer (%): "))
        except ValueError:
            print("Invalid number entered.\n")
            return
        cost = qty * unit_price
        if state["Balance"] > cost:
            state["Stock"][name] = qty
            state["Item_Price"][name] = unit_price
            state["Item_discount"][name] = disc
            state["Item_offer"][name] = offer
            state["Balance"] -= cost
            print("\n", state["Stock"])
            log_entry(state, "Add item", name, qty, "Successful")
        else:
            print("No required balance.")
            log_entry(state, "Add item", name, "-", "Unsuccessful")
    save_data(state)


def remove_item(state):
    """Completely remove an item from the inventory."""
    name = input("\nEnter name: ")
    if name in state["Stock"]:
        # Refund the item's base price to balance
        state["Balance"] += state["Item_Price"].get(name, 0)
        state["Stock"].pop(name, None)
        state["Item_Price"].pop(name, None)
        state["Item_discount"].pop(name, None)
        state["Item_offer"].pop(name, None)
        print(state["Stock"])
        log_entry(state, "Remove item", name, "-", "Successful")
    else:
        print("\nNo item found.")
        log_entry(state, "Remove item", name, "-", "No item found")
    save_data(state)


def check_balance(state):
    """Print the current balance."""
    print("Current Balance:", state["Balance"])
    log_entry(state, "Balance", "-", "-", "Successful")
    save_data(state)


def user_menu(state):
    """Main user operations menu (sales / inventory operations)."""
    while True:
        try:
            print("\n<--- Operations --->\n"
                  "1. Show Stock\n"
                  "2. Show Item\n"
                  "3. Add Item Stock\n"
                  "4. Item Sell\n"
                  "5. Add New Item\n"
                  "6. Remove Item\n"
                  "7. Check Balance\n")
            n = int(input("Enter: "))

            if n == 1:
                show_stock(state)
            elif n == 2:
                show_item(state)
            elif n == 3:
                add_stock_quantity(state)
            elif n == 4:
                sell_item(state)
            elif n == 5:
                add_new_item(state)
            elif n == 6:
                remove_item(state)
            elif n == 7:
                check_balance(state)
            else:
                print("\nEnter a valid choice.")
                continue

        except ValueError:
            print("Please enter a valid value.\n")
            continue

        if input("\nIf again, enter 0: ") != "0":
            break


# ----------------- Main entry point -----------------
def main():
    """Load saved state, authenticate, and route to the appropriate menu."""
    state = load_data()

    print("              Welcome to Electronics")
    print("*" * 50)

    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        password = input("Enter Password: ")
        if password == ADMIN_PASSWORD:
            attempts += 1
            admin_menu(state)
        elif password == USER_PASSWORD:
            attempts += 1
            user_menu(state)
        else:
            print("\nWrong Password.\n")
            attempts += 1

    # Final save before exit
    save_data(state)
    print("\nThank You!\n")


if __name__ == "__main__":
    main()
