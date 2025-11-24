import time
import random

def run_store_app():
    store_name = "VIT MARKET"
    cashier_name = random.choice(["Himanshu", "Aryan", "Priyanshu", "Jainam"])

    print(f" Welcome to {store_name}")
    print(f"Cashier {cashier_name} is ready to help you.")
    print("Type 'q' or 'quit' when you are done shopping \n")

    basket = []
    running_total = 0.0

    while True:
        # 1. Get the item name (Conversational input)
        product = input("What are you buying? ").strip().title()

        # Check for exit condition
        if product.lower() in ['q', 'quit', 'exit', 'done']:
            break

        # Check if user just hit enter by mistake
        if not product:
            continue

        # 2. Get the price with error handling
        while True:
            try:
                price_input = input(f"  > How much does the '{product}' cost? $")
                price = float(price_input)

                # Logic check: Price can't be negative
                if price < 0:
                    print("  (!) Price cannot be negative. Try again.")
                    continue

                break # Break the price loop if input is valid
            except ValueError:
                print("  (!) Oops, that doesn't look like a valid price.")

        # Add to our list and update total
        basket.append((product, price))
        running_total += price
        print(f"  OK, added {product} to your basket.\n")

    # --- The Receipt Section ---

    # Check if they actually bought anything
    if not basket:
        print("\nLooks like you didn't buy anything. Have a nice day!")
        return

    print("\n" + "*" * 40)
    print(f"{store_name:^40}") # Centers the text
    print(f"{'Receipt generated for you':^40}")
    print("*" * 40)

    # Simulating a short delay like a real printer
    print("Printing receipt...", end="", flush=True)
    time.sleep(1)
    print(" Done!\n")

    # List items
    for product, price in basket:
        # Format: Name on left, Price on right
        print(f"{product:<30} ${price:>7.2f}")

    print("-" * 40)

    # Calculate Tax
    tax_rate = 0.08 # 8% tax
    tax_amount = running_total * tax_rate
    final_amount = running_total + tax_amount

    print(f"Subtotal:{running_total:>30.2f}")
    print(f"Tax (8%):{tax_amount:>30.2f}")
    print("=" * 40)
    print(f"TOTAL DUE:{final_amount:>29.2f}")
    print("=" * 40)
    print(f"You were served by: {cashier_name}")
    print("Thanks for visiting!\n")

if __name__ == "__main__":
    run_store_app()
