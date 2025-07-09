### Suggestions for `example.py`

1. **[SEVERITY: HIGH] [SECURITY]**: The `eval` function in `process_user_input` is a major security risk as it can execute arbitrary code. Replace it with a safer alternative like `ast.literal_eval` or a custom expression parser.

2. **[SEVERITY: MEDIUM] [ERROR HANDLING]**: The `process_user_input` function has a bare `except` block, which is a bad practice. It should catch specific exceptions (e.g., `ValueError`, `TypeError`) to avoid masking unexpected errors.

3. **[SEVERITY: MEDIUM] [ROBUSTNESS]**: The `generate_report` function assumes that `data` is a non-empty list and that the first element is a dictionary. Add checks to handle cases where `data` is empty or not a list of dictionaries.

4. **[SEVERITY: MEDIUM] [IMPORTS]**: The `datetime` module is imported inside the `__main__` block. It should be imported at the top of the file for better readability and consistency.

5. **[SEVERITY: LOW] [PERFORMANCE]**: In `filter_products`, the `filtered` list could be replaced with a list comprehension for better readability and performance.

6. **[SEVERITY: LOW] [CODE STYLE]**: The `analyze_text` function could use a dictionary comprehension to make the code more concise and Pythonic.

7. **[SEVERITY: LOW] [CODE STYLE]**: The `calculate_stats` function could use the `statistics` module for calculating mean and median, which would make the code cleaner and more maintainable.

8. **[SEVERITY: LOW] [USABILITY]**: The `process_user_input` function could provide more descriptive error messages instead of just returning "Invalid input."

---

