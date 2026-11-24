"""The One-Line Cat Joke That Lands.

Writes one line of cat comedy to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The writing is the whole contest: no
network, no randomness, no clock, no model call — the same bytes every run.

The joke (88 characters, 1 line, 1 sentence, UTF-8, no trailing newline):
    I bought a scratching post to save the sofa; my cat scratched the sofa to save the post.
"""

import os

JOKE = "I bought a scratching post to save the sofa; my cat scratched the sofa to save the post."

# 88 characters, 1 line, 1 sentence. Gate: /output/entry.txt must be UTF-8
# text of 1 to 200 characters, not only white space. No trailing newline:
# the tie-break favours smaller text (fewer bytes), so the file is exactly
# the joke, 88 bytes.
assert 1 <= len(JOKE) <= 200
assert "\n" not in JOKE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(JOKE.encode("utf-8"))
    # Self-check: re-read the file and refuse to finish unless the bytes
    # are exactly the joke. Output is byte-identical by construction.
    with open(path, "rb") as f:
        written = f.read()
    if written != JOKE.encode("utf-8"):
        raise SystemExit("entry.txt does not match the joke literal")


if __name__ == "__main__":
    main()
