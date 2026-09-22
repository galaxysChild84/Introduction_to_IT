# -----------------------------------------
# Credit Card Payment Program
# -----------------------------------------

def get_input():
    """Multi-valued input function."""
    old_balance = float(input("Enter old balance: "))
    charges = float(input("Enter charges for month: "))
    credits = float(input("Enter credits: "))
    return old_balance, charges, credits


def compute_payment(old_balance, charges, credits):
    """Multi-valued calculation function."""
    # Finance charge is 1.5% of old balance
    finance_charge = old_balance * 0.015

    # New balance formula
    new_balance = old_balance + charges + finance_charge - credits

    # Minimum payment rules
    if new_balance <= 20:
        minimum_payment = new_balance
    else:
        minimum_payment = 20 + 0.10 * (new_balance - 20)

    return new_balance, minimum_payment


def display_results(new_balance, minimum_payment):
    """Output function."""
    print(f"New balance: ${new_balance:.2f}")
    print(f"Minimum payment: ${minimum_payment:.2f}")


def main():
    old_balance, charges, credits = get_input()
    new_balance, minimum_payment = compute_payment(old_balance, charges, credits)
    display_results(new_balance, minimum_payment)


# Run the program
main()
