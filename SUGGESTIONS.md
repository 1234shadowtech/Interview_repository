### Suggestions for `bye.py`

1. **[Severity: Medium | Tag: Accuracy]** Use `math.pi` instead of hardcoding `3.14159` for better precision in the `calculate_area` function.
2. **[Severity: Low | Tag: Code Organization]** Move all imports to the top of the file for better readability and adherence to Python conventions.
3. **[Severity: Medium | Tag: Error Handling]** Replace `return None` in `calculate_area` with `raise NotImplementedError` for unsupported shapes to make the error explicit.
4. **[Severity: Medium | Tag: Performance]** In `validate_user`, the loop can break early when all conditions are met, but this is already implemented. Consider adding comments to clarify this optimization.
5. **[Severity: Low | Tag: Error Handling]** In `process_data`, handle unsupported data types more gracefully instead of raising a `TypeError`. For example, log the error or skip the unsupported item.
6. **[Severity: Low | Tag: Code Readability]** Add docstrings to all functions to improve code documentation and clarity.
7. **[Severity: Low | Tag: Code Readability]** Use type hints for function arguments and return types to make the code more self-documenting.
8. **[Severity: Medium | Tag: Validation]** In `format_output`, validate the `format_type` argument explicitly and raise an error for unsupported formats instead of defaulting to `str(data)`.
9. **[Severity: Low | Tag: Code Organization]** Consider splitting the `main` function into smaller test functions for better modularity and easier testing.
10. **[Severity: Low | Tag: Code Readability]** Use constants for error messages to avoid repetition and improve maintainability.

---

