#!/usr/bin/env python3
"""One satirical sentence roasting lawmakers who would regulate AI, crypto
or the internet but cannot convert a file to PDF.

Writes the sentence to /output/entry.txt. Gate: UTF-8 text, 1-320 chars,
not only whitespace, single sentence.
"""

LINE = (
    "The same lawmakers who want to write the rules for AI, crypto, and the "
    "entire internet still forward a Word document to an intern with the "
    "subject line 'please make PDF'."
)

MAX_CHARS = 320


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
