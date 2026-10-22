# Python Fundamentals

Documenting my process of getting back into coding: learning Python, writing good tests, and running them in a CI pipeline.

## What's in it

- **Ticket analysis**: counting, filtering and summarizing support tickets
- **CSV loading**: reading ticket data from a file, skipping blank lines and rejecting malformed ones
- **Code review exercise**: finding and fixing a bug in a scheduling function, with tests proving the fix
- **Report with error handling**: friendly messages and exit codes for missing or invalid files

## What I learned

- Testing at boundaries: just below, at, and just above every limit
- Breaking code purposefully to check tests that catch it errors
- Validating input and raising clear errors

## Running the tests

```
pip install pytest
python -m pytest
```

Every push runs the full test suite automatically with GitHub Actions.