#!/usr/bin/env python3
"""Write a 120-word cold email to /output/entry.txt.

The email pitches ClearLedger Bookkeeping to a busy plumber: it opens
on the plumber's week (leaks, van receipts, night paperwork), makes one
small concrete offer (flat monthly fee, first tidy-up free, a free
15-minute look at the books), and ends with a single easy ask.
"""

import os

ENTRY = (
    "Subject: Your books, done while you're on the next job\n"
    "\n"
    "Hi \u2014 I'm Maya from ClearLedger Bookkeeping. You fix leaks; I fix "
    "the paperwork leaks: unlogged invoices, receipts in the van, "
    "tax-season panic. For one flat monthly fee I track every job, chase "
    "late payers, and hand you clean books you can read in two minutes "
    "between calls. No software to learn, no hourly meter running. Most "
    "plumbers I help get their Sundays back within the first month, and "
    "your first tidy-up is free if you mention this email. If I save you "
    "one evening a week, that's a job won back \u2014 want a free 15-minute "
    "look at your books this week? Reply \"yes\" and I'll send a time.\n"
)


def main() -> None:
    # The gate wants 1 to 800 characters of non-whitespace UTF-8 text.
    assert 1 <= len(ENTRY) <= 800 and ENTRY.strip(), "entry out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
