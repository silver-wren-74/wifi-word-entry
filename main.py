#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun bounty entry.

Writes a single original word (1 to 20 characters) to /output/entry.txt,
exactly as the competition gate expects: one word describing home Wi-Fi,
aiming to be both the funniest and the truest.
"""

import os

# DRAFT 1: "Buffering" — on-subject and true, but it is the word everyone
# reaches for first (criterion 4 fails outright), and it describes a
# symptom rather than the lived experience. A judge that has seen it
# 200 times will not laugh.
# REVISION PASS (against the RULES judging criteria, in order):
# 1. On-subject: "Ghosting" is about Wi-Fi as the entrant lives it — the
#    signal is there, then it simply stops answering, mid-call, mid-game.
# 2. Funny at once: the dating-slang transplant lands instantly — your
#    router ghosts you. No explanation needed, no pun to decode.
# 3. True: every home network does this — full bars one minute, dead the
#    next, always at the worst moment. The joke lands because it is
#    recognisable to anyone who has ever shouted at a router.
# 4. Fresh angle: the field will be full of "Slow", "Buffering",
#    "Loading" and "Unstable". Nobody else names the router as a bad
#    date who vanishes without a word.
# 5. Standalone: one common word, eight letters, spelled exactly as a
#    reader expects — it works as a network name on its own, which is
#    what the winning word becomes.
WORD = "Ghosting"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = WORD.strip()
    assert 1 <= len(text) <= 20, f"word must be 1-20 chars, got {len(text)}"
    assert " " not in text and "\n" not in text, "entry must be a single word"
    # Single word, no trailing newline: the gate counts the file's characters.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
