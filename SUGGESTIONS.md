### Suggestions for `Hi.py`

1. **[Critical] Function Logic Issue**: The `ADD` function is defined to take parameters `x` and `y`, but it does not use them. Instead, it uses the global variables `a` and `b`. This is misleading and violates the principle of encapsulation. The function should use its parameters (`x` and `y`) for computation.
2. **[Moderate] Naming Convention**: The function name `ADD` is in uppercase, which is unconventional in Python. Function names should follow snake_case (e.g., `add`).
3. **[Low] Unused Parameters**: The parameters `x` and `y` are defined but not used, which is unnecessary and confusing.
4. **[Low] Lack of Output Handling**: The result of the `ADD` function is computed but not stored or printed. This makes the code incomplete for practical use.
5. **[Low] Lack of Comments**: The code lacks comments explaining its purpose or logic, which reduces readability and maintainability.

