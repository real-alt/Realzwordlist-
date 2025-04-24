# Custom Wordlist Generator

This is a powerful and customizable wordlist generator written in Python, designed for penetration testers, ethical hackers, and cybersecurity enthusiasts.

## Features

- Input multiple names, numbers, and dates with comma separation
- Combine personal data with:
  - Clothing brands
  - Shoe brands
  - Colors
  - Keyboard walk patterns
- Toggle options for:
  - Leetspeak conversions (e.g., password -> p@ssw0rd)
  - Symbol sets
  - Reversed names and numbers
  - Custom rules
- Generate phone numbers:
  - Standalone numbers
  - Combined with names/words
- Wordlist size limit option for performance
- Hashcat-ready output mode

## Usage

```bash
python wordlist_generator.py
```

You'll be prompted to enter the following:
- Names (comma-separated)
- Phone numbers or area codes (optional)
- Symbols, colors, brands (optional or pre-built)
- Leetspeak toggle (y/n)
- Reversed patterns toggle (y/n)
- Output file name
- Maximum wordlist size (optional)

## Example

```
Enter names (comma separated): john,mary
Enter phone numbers (comma separated or press enter to skip): 312,773
Use leetspeak? (y/n): y
Use reversed names? (y/n): y
Limit wordlist size? (Enter number or press enter to skip): 50000
```

## Requirements

- Python 3.x

No external libraries required.

## Disclaimer

This tool is intended for educational and authorized penetration testing purposes **only**. Do not use it against systems you do not have explicit permission to test.

## License

MIT License
