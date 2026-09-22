# -----------------------------------------
# Planets sorted by surface area (descending)
# -----------------------------------------

def main():
    Planets = [
        ('Mercury', 75, 1),
        ('Venus', 460, 2),
        ('Mars', 140, 4),
        ('Earth', 510, 3),
        ('Jupiter', 62000, 5),
        ('Neptune', 7640, 8),
        ('Saturn', 42700, 6),
        ('Uranus', 8100, 7)
    ]

    # Sort by surface area (index 1) in descending order
    sorted_planets = sorted(Planets, key=lambda p: p[1], reverse=True)

    print("Sorted by surface area in descending order:")
    for planet in sorted_planets:
        print(planet[0], end=" ")


# Run the program
main()
