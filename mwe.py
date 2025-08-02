#!/usr/bin/env python3

import argparse
import base64
import sys
from urllib.parse import urlparse

def extract_and_decode_markwhen(url: str) -> str:
    """
    Extract the Base64‐encoded timeline data after '#mw=' in the URL,
    decode it, and return the plain-text timeline.
    """
    parsed = urlparse(url)
    fragment = parsed.fragment  # everything after '#'
    prefix = "mw="
    if not fragment.startswith(prefix):
        raise ValueError("URL fragment does not start with 'mw='")
    b64_data = fragment[len(prefix):]
    try:
        decoded = base64.b64decode(b64_data).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Failed to decode Base64 data: {e}")
    return decoded

def main():
    parser = argparse.ArgumentParser(
        description="Extract and decode the Markwhen timeline data from a URL."
    )
    parser.add_argument(
        "url",
        help="The full Markwhen URL (e.g. https://timeline.markwhen.com#mw=…)",
    )
    args = parser.parse_args()

    try:
        timeline_text = extract_and_decode_markwhen(args.url)
    except Exception as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    print(timeline_text)

if __name__ == "__main__":
    main()
