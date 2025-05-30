# worldlivetv

A simple Python script to generate unlock codes for [worldlivetv.stream](http://worldlivetv.stream).

## Features

- Generates unlock codes with different validity periods (`click` for 24h, `view` for 2h)
- Outputs the code, unlock URL, and expiration time

## Requirements

- Python 3.x

## Usage

Run the script from the command line:

```bash
python main.py
```

## Example

```text
Enter method (click/view): view

✅ Unlock Code Generated Successfully!
Code: 1712345678901
URL: http://worldlivetv.stream?code=1712345678901
Valid Until: Sat Jun 15 14:00:00 2025
```
