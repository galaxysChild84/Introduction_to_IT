import math

def ceil(x):
    """Round non-integer numbers up to the next integer."""
    return math.ceil(x)

def cost(ounces):
    """Compute the postage cost for an airmail letter."""
    if ounces <= 1:
        return 0.05
    else:
        extra_ounces = ceil(ounces - 1)
        return 0.05 + (extra_ounces * 0.10)

# Main program
ounces = float(input("Enter the number of ounces: "))
postage = cost(ounces)
print(f"Cost: ${postage:.2f}")
