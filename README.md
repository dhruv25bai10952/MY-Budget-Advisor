# 💸 Bill Split Calculator

A command-line Python tool that helps groups of friends, roommates, or colleagues split expenses fairly — and figures out the **minimum number of transactions** needed to settle up.

---

## 👤 Author

| Field     | Details                          |
|-----------|----------------------------------|
| Name      | DHRUV KUMAR SHARMA               |
| Roll No.  | 25BAI10952                       |
| Course    | Python Essentials                |
| Platform  | VITyarthi                        |

---

## 📌 The Problem

When a group shares expenses (trips, dinners, household bills), different people often pay for different things. Figuring out who owes whom — without overpaying or underpaying — is surprisingly tricky to do by hand.

This tool solves it automatically.

---

## ✨ Features

- Add any number of group members
- Record multiple expenses (who paid, how much, what for)
- Calculates each person's **net balance** (paid vs. fair share)
- Uses a **greedy algorithm** to compute the fewest possible repayment transactions
- Clean, formatted summary output
- Handles invalid input gracefully (no crashes on bad data)

---

## 🚀 Getting Started

### Requirements

- Python 3.x (no external libraries needed)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Failureorno/MY-Bill-Splitter

# 2. Navigate into the folder
cd bill-split-calculator

# 3. Run the program
python bill_splitter.py
```

---

## 🖥️ How to Use

When you run the program, it will guide you step by step.

**Step 1 — Enter group members**
```
Enter name: Alice
Enter name: Bob
Enter name: Carol
Enter name: done
```

**Step 2 — Enter expenses**
```
Who paid? ['Alice', 'Bob', 'Carol']
Payer's name (or 'done'): Alice
Amount paid by Alice: ₹ 600
Description (e.g. dinner, taxi): dinner

Payer's name (or 'done'): Bob
Amount paid by Bob: ₹ 300
Description (e.g. dinner, taxi): taxi

Payer's name (or 'done'): done
```

**Step 3 — View the summary**
```
=============================================
           EXPENSE SUMMARY
=============================================
Total spent       : ₹900.00
Number of people  : 3
Fair share each   : ₹300.00

--- INDIVIDUAL EXPENSES ---
  Alice           paid  ₹600.00  (dinner)
  Bob             paid  ₹300.00  (taxi)

--- NET BALANCES ---
  Alice           is owed  ₹300.00
  Bob             is settled
  Carol           owes     ₹300.00

--- SETTLE UP (minimum transactions) ---
  Carol → pays ₹300.00 → Alice
=============================================
```

---

## 🧠 How It Works

### Balance Calculation
The total of all expenses is divided equally among all group members. Each person's **net balance** is:

```
balance = total they paid  −  their fair share
```

- Positive balance → they are owed money
- Negative balance → they owe money
- Zero → they are settled

### Settlement Algorithm (Greedy)
To find the minimum number of transactions:

1. Separate group into **debtors** (negative balance) and **creditors** (positive balance)
2. Sort both lists by magnitude, largest first
3. Repeatedly match the biggest debtor with the biggest creditor
4. Each match results in one payment; repeat until all balances are zero

This guarantees at most **(N − 1)** transactions for a group of N people.

---

## 📁 Project Structure

```
bill-split-calculator/
│
├── bill_splitter.py    # Main program
└── README.md           # This file
```

---

## 🔮 Possible Future Improvements

- **Save/load sessions** — persist expenses to a JSON or CSV file
- **Unequal splits** — allow custom percentage splits (e.g. 60/40)
- **Multiple currencies** — support conversion for international trips
- **Web interface** — build a simple Flask or Streamlit UI
- **Export to PDF** — share a printable settlement report

---

## 📚 Concepts Used

| Concept | Where |
|---|---|
| Functions | Each logical step is its own function |
| Dictionaries | Storing balances and expense records |
| Lists | Group members, expense log, debtor/creditor queues |
| Loops | Input collection, balance computation, settlement |
| try/except | Handling non-numeric input gracefully |
| sorted() with key | Sorting debtors and creditors by magnitude |
| f-strings | Clean, formatted output |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
