def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        try:
            result = num / denom
            return f"The result of the division is {result:.2f}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
