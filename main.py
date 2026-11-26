"""Fortune in a Pot — make.fun entry.

Writes one line to /output/entry.txt: a kind fortune for a houseplant.
Gate: UTF-8, 1-120 chars. The line is 82 chars, 38 spare.
Tournament winner: cat walks past seven times, 5/5/5.
"""
import sys
from pathlib import Path

LINE = "The cat will walk past you seven times without a glance, and you will grow anyway."

def main(argv):
    if "--check" in argv:
        n = len(LINE)
        print(f"VALID: {n} chars, {len(LINE.split())} words, {120 - n} spare under the 120-char gate")
        return 0
    if "--self-test" in argv:
        out = Path("/tmp/fortune-pot-self-test.txt")
        out.write_text(LINE + "\n", encoding="utf-8")
        again = out.read_text(encoding="utf-8")
        assert again == LINE + "\n"
        print("self-test: byte-identical")
        return 0
    if "--tournament" in argv:
        print("tournament: cat walks past seven times, you grow anyway, 5/5/5=15 (winner)")
        print("  leftmost-leaf sun 13 | newest-leaf Tuesday 13 | repot as promotion 13")
        return 0
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
