"""
Bill Split Calculator
=====================
Course   : Python Essentials
Project  : Bring Your Own Project (BYOP)
Platform : VITyarthi

Student  : DHRUV KUMAR SHARMA
Roll No. : 25BAI10952

Description:
    Enter group members and their expenses.
    The program calculates who owes whom and outputs
    the minimum number of transactions to settle up.
"""


def get_people():
    """Ask the user to enter group members."""
    print("\n=== BILL SPLIT CALCULATOR ===")
    print("Enter the names of people in your group.")
    print("Type 'done' when finished.\n")

    people = []
    while True:
        name = input("Enter name: ").strip()
        if name.lower() == "done":
            if len(people) < 2:
                print("You need at least 2 people. Keep going!")
                continue
            break
        if name == "":
            print("Name cannot be empty.")
            continue
        if name in people:
            print(f"'{name}' is already added.")
            continue
        people.append(name)
        print(f"  Added: {name}")

    return people


def get_expenses(people):
    """Ask the user to enter all expenses."""
    print("\n--- ENTER EXPENSES ---")
    print("Type 'done' when all expenses are entered.\n")

    expenses = []

    while True:
        print(f"Who paid? {people}")
        payer = input("Payer's name (or 'done'): ").strip()

        if payer.lower() == "done":
            if not expenses:
                print("Enter at least one expense first.")
                continue
            break

        if payer not in people:
            print(f"'{payer}' is not in the group. Try again.")
            continue

        try:
            amount = float(input(f"Amount paid by {payer}: ₹ "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        description = input("Description (e.g. dinner, taxi): ").strip()
        if not description:
            description = "expense"

        expenses.append({
            "payer": payer,
            "amount": amount,
            "description": description
        })

        print(f"  Recorded: {payer} paid ₹{amount:.2f} for {description}\n")

    return expenses


def calculate_balances(people, expenses):
    """
    Calculate net balance for each person.
    Positive = they are owed money.
    Negative = they owe money.
    """
    total = sum(e["amount"] for e in expenses)
    share = total / len(people)

    balance = {person: 0.0 for person in people}

    for expense in expenses:
        balance[expense["payer"]] += expense["amount"]

    for person in people:
        balance[person] -= share

    return balance, total, share


def settle_up(balance):
    """
    Find the minimum set of transactions to settle all debts.
    Uses a greedy algorithm: the biggest debtor pays the biggest creditor.
    """
    debtors   = sorted([(p, -b) for p, b in balance.items() if b < -0.01], key=lambda x: -x[1])
    creditors = sorted([(p,  b) for p, b in balance.items() if b >  0.01], key=lambda x: -x[1])

    transactions = []

    i, j = 0, 0
    while i < len(debtors) and j < len(creditors):
        debtor,   debt   = debtors[i]
        creditor, credit = creditors[j]

        payment = min(debt, credit)
        transactions.append((debtor, creditor, round(payment, 2)))

        debt   -= payment
        credit -= payment

        debtors[i]   = (debtor,  debt)
        creditors[j] = (creditor, credit)

        if debt < 0.01:
            i += 1
        if credit < 0.01:
            j += 1

    return transactions


def print_summary(people, expenses, balance, total, share, transactions):
    """Print the full summary report."""
    print("\n" + "=" * 45)
    print("           EXPENSE SUMMARY")
    print("=" * 45)

    print(f"\nTotal spent       : ₹{total:.2f}")
    print(f"Number of people  : {len(people)}")
    print(f"Fair share each   : ₹{share:.2f}")

    print("\n--- INDIVIDUAL EXPENSES ---")
    for e in expenses:
        print(f"  {e['payer']:<15} paid  ₹{e['amount']:>8.2f}  ({e['description']})")

    print("\n--- NET BALANCES ---")
    for person, bal in balance.items():
        if bal > 0.01:
            status = f"is owed  ₹{bal:.2f}"
        elif bal < -0.01:
            status = f"owes     ₹{abs(bal):.2f}"
        else:
            status = "is settled"
        print(f"  {person:<15} {status}")

    print("\n--- SETTLE UP (minimum transactions) ---")
    if not transactions:
        print("  Everyone is already settled!")
    for debtor, creditor, amount in transactions:
        print(f"  {debtor} → pays ₹{amount:.2f} → {creditor}")

    print("\n" + "=" * 45)
    print("All done! Enjoy your trip/meal/outing :)")
    print("=" * 45 + "\n")


def main():
    people   = get_people()
    expenses = get_expenses(people)
    balance, total, share = calculate_balances(people, expenses)
    transactions = settle_up(balance)
    print_summary(people, expenses, balance, total, share, transactions)


if __name__ == "__main__":
    main()
