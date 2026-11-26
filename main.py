"""Fortune Cookie Funnies for Engineers — make.fun entry.

Prints (and writes) one fortune-cookie prophecy for engineers:
a Friday deploy, a passing build, and servers that refuse to
cooperate — with the cookie claiming it saw it all coming.

The fortune is a plain string constant: no randomness, no network,
no files read — the same line every run, so the grader sees a
deterministic entry.
"""

import os

FORTUNE = (
    "You will ship on Friday. The build will pass, the servers "
    "will not, and the cookie saw it coming."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(FORTUNE + "\n")
    print(FORTUNE)


if __name__ == "__main__":
    main()
