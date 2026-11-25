# u-xvader-tell-a-whole-story-in-32-characters-f86dd978: Tell a Whole Story in 32 Characters
# One Wi-Fi network name of at most 32 characters that lands a joke and
# implies a whole story. The program writes the name to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR).
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The name in two beats: the setup names the breakup ("The Ex"), the punch
# is the petty divorce settlement — the router went with them, in 2019.
# A whole story (split, custody battle over the Wi-Fi) in 30 characters.
NAME = "The Ex Took The Router In 2019"


def validate_name(name):
    assert 1 <= len(name) <= 32, f"name is {len(name)} chars, must be 1-32"
    assert name.strip(), "name must not be only whitespace"


def main():
    validate_name(NAME)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NAME)


if __name__ == "__main__":
    main()
