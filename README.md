
# Regex Data Extraction (Command-line)

This small Python utility extracts common structured data from a text file using regular expressions. It reads `sample_input.txt`, finds emails, URLs, phone numbers, and credit-card-like sequences, masks credit card numbers, and prints a readable summary to stdout.

**Features**
- **Emails:** detects common email formats.
- **URLs:** finds `http`/`https` links.
- **Phones:** matches US-style 10-digit phone numbers with common separators.
- **Credit cards:** detects 16-digit groups and masks all but the last 4 digits.

**How it works (high level)**
- The main entry point is the `main()` function in `main.py`.
- `extract_data(text)` runs several compiled regex patterns to collect matches.
- `is_safe(value)` filters out inputs containing obvious HTML/script indicators.
- `mask_card(card)` replaces a detected card number with a masked form like `**** **** **** 1234`.

**Files**
- `main.py`: program source. Run it to extract data from `sample_input.txt`.
- `sample_input.txt`: input text to scan (provide your own or edit the existing file).
- `sample_output.txt`: example output (optional reference).

**Usage**
1. Ensure you have Python 3.7+ installed.
2. Place the text you want scanned into `sample_input.txt` (or modify the code to read a different file).
3. Run:

```
python main.py
```

The script will print an `Extracted Data:` summary to the console.

**Notes & Security**
- The `is_safe()` check is a simple, conservative filter and is not a substitute for robust input sanitization.
- The credit-card masking keeps only the last 4 digits visible to help avoid accidental exposure of sensitive data.
- Regex-based extraction is heuristic; adjust patterns in `main.py` if you need stricter or locale-specific matching.


