### Suggestions for `example.py`

1. **[CRITICAL] Replace `eval` in `process_user_input` with a safer alternative**  
   Using `eval` is a major security risk as it can execute arbitrary code. Consider using a library like `ast.literal_eval` for safer evaluation of expressions.

2. **[HIGH] Add specific exception handling in `process_user_input`**  
   The catch-all `except` block is bad practice. It should be replaced with specific exception handling (e.g., `ValueError`, `TypeError`) to avoid masking unexpected errors.

3. **[HIGH] Add validation for `data` in `generate_report` to handle empty or invalid inputs**  
   The function assumes `data` is a non-empty list of dictionaries. Add checks to handle cases where `data` is empty or not structured as expected.

4. **[MEDIUM] Move the `datetime` import to the top of the file**  
   Imports should be at the top of the file to follow Python's best practices for readability and maintainability.

5. **[MEDIUM] Use list comprehensions in `filter_products` for better readability**  
   The filtering logic can be simplified using list comprehensions, making the code more concise and Pythonic.

6. **[MEDIUM] Use dictionary comprehensions in `analyze_text` for conciseness**  
   The `stats` dictionary can be constructed using a dictionary comprehension to reduce repetitive code.

7. **[LOW] Use the `statistics` module in `calculate_stats` for mean and median calculations**  
   The `statistics` module provides built-in functions for mean and median, which are more robust and readable.

8. **[LOW] Improve error messages in `process_user_input` for better user feedback**  
   Provide more descriptive error messages to help users understand what went wrong.

---

