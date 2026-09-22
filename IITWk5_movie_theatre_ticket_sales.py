
# Movie price list

movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each)


# Part D  Discounts & validation (challenge)
def apply_group_discount(qty, price_each):
    """10% off if buying 4 or more tickets in one line."""
    line_total = qty * price_each
    if qty >= 4:
        return line_total * 0.90   # 10% off
    return line_total

def apply_member_discount(total, is_member):
    """Extra 5% off the grand total."""
    if is_member:
        return total * 0.95
    return total


# Part A —  Input loop (while) & list of purchases
while True:
    title = input("Enter movie title (or 'done'): ")

    if title.lower() == "done":
        break

    if title not in movies:
        print("Movie not found. Available titles:")
        print(", ".join(movies.keys()))
        continue

    # quantity with validation
    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Quantity must be a number.")
        continue

    purchases.append((title, qty, movies[title]))


# Part B — Receipt (for loop over list)
print("\n--- RECEIPT ---")

grand_total = 0

for title, qty, price_each in purchases:
    line_total = apply_group_discount(qty, price_each)
    print(f"{title}: {qty} × ${price_each:.2f} = ${line_total:.2f}")
    grand_total += line_total

# Member discount
member = input("Do you have a member code? (yes/no): ").lower() == "yes"
grand_total = apply_member_discount(grand_total, member)

print(f"Grand Total: ${grand_total:.2f}")

# Part C — Sales summary (dictionaries)

tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each in purchases:
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0) + apply_group_discount(qty, price_each)

print("\n--- SALES SUMMARY ---")
for title in movies:
    t = tickets_by_movie.get(title, 0)
    r = revenue_by_movie.get(title, 0)
    print(f"{title}: {t} tickets, ${r:.2f} revenue")


# Part E — Analytics
# Top seller by tickets
top_title = None
top_qty = -1
for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title, top_qty = title, qty

print("\nTop seller:", top_title, top_qty)

# Sort by revenue
sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)
print("Revenue ranking:", sorted_by_rev)

# Average tickets per purchase
if purchases:
    total_tickets = sum(qty for _, qty, _ in purchases)
    avg = total_tickets / len(purchases)
    print(f"Average tickets per purchase: {avg:.2f}")
else:
    print("No purchases made.")
