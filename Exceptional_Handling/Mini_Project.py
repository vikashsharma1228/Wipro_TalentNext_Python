def process_purchase_file():
    try:
        # Get filename at runtime
        file_name = input("Enter the purchase file name (e.g., Purchase-1.txt): ").strip()

        # Read file content
        with open(file_name, 'r') as file:
            lines = file.readlines()

        total_items = 0
        free_items = 0
        total_amount = 0.0

        for line in lines:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            try:
                parts = line.rsplit(' ', 1)
                if len(parts) != 2:
                    raise ValueError(f"Invalid format: {line}")

                item_name, price_str = parts
                price_str = price_str.strip()

                # Handle "Free" or price as 0
                if price_str.lower() == "free" or price_str == "0":
                    price = 0.0
                    free_items += 1
                else:
                    price = float(price_str)

                total_amount += price
                total_items += 1

            except ValueError as ve:
                print(f"Skipping line due to error: {ve}")

        discount_amount = total_amount * 0.10  # 10% discount
        final_amount = total_amount - discount_amount

        # Print results
        print(f"\nSummary of Purchase:")
        print(f"Total items purchased: {total_items}")
        print(f"Number of free items: {free_items}")
        print(f"Total amount (before discount): ₹{total_amount:.2f}")
        print(f"Discount amount (10%): ₹{discount_amount:.2f}")
        print(f"Final amount to pay: ₹{final_amount:.2f}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
process_purchase_file()
