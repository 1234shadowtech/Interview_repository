```python
def calculate_discount(price, discount_rate):
    # Ensure the price is a positive number
    if price < 0:
        raise ValueError("Price cannot be negative")  # Raise an error if the price is invalid

    # Ensure the discount rate is between 0 and 1
    if not (0 <= discount_rate <= 1):
        raise ValueError("Discount rate must be between 0 and 1")  # Raise an error if the discount rate is invalid

    # Calculate the discount amount
    discount = price * discount_rate  # Multiply price by discount rate to get the discount amount

    # Calculate the final price after applying the discount
    final_price = price - discount  # Subtract the discount from the original price

    return final_price  # Return the final price after discount


def process_order(order):
    # Check if the order contains the required keys
    if 'price' not in order or 'discount_rate' not in order:
        raise KeyError("Order must contain 'price' and 'discount_rate' keys")  # Raise an error if keys are missing

    # Extract price and discount rate from the order
    price = order['price']  # Get the price from the order dictionary
    discount_rate = order['discount_rate']  # Get the discount rate from the order dictionary

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(price, discount_rate)  # Call the function to compute the discounted price

    # Add the final price to the order dictionary
    order['final_price'] = final_price  # Store the computed final price back into the order dictionary

    return order  # Return the updated order dictionary


def main():
    # Example order data
    order = {
        'price': 100,  # Original price of the item
        'discount_rate': 0.2  # Discount rate to be applied (20%)
    }

    try:
        # Process the order to calculate the final price
        updated_order = process_order(order)  # Call the process_order function with the example order

        # Print the updated order with the final price
        print("Updated Order:", updated_order)  # Display the updated order dictionary

    except (ValueError, KeyError) as e:
        # Handle any errors that occur during processing
        print("Error:", e)  # Print the error message to the console


# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to execute the script
```