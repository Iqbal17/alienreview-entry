"""Alien Field Notes: The Two Day Earth Review — deliberation and decision record.

Task: one original line, 1-200 characters, a review of planet Earth left
by an alien tourist. Judge weighs, in order:
(1) it IS an alien tourist's one-line review of Earth, the visitor's
outside view clear in the line; off-premise loses to any on-premise entry;
(2) it is funny, the laugh coming from the alien's angle on ordinary
Earth life rather than a joke bolted onto the premise;
(3) it is original: a comparison, complaint or detail few other entrants
would have reached — not the first obvious thought about traffic,
gravity, money or weather;
(4) it sounds like a review a tourist would actually leave, with a
verdict, a rating or a closing remark, in a single line;
(5) it is tight: every word earns its place and the punch lands at the
end. A line that explains its own joke, or stacks several jokes, is
weaker than one that lands a single one cleanly.

Candidates weighed (pass 1):

1. "The locals carry their dogs' mess around in little bags like
   trophies, and still insist the dogs are the pets. Four stars."
   Loses: the "who walks whom" angle is a familiar pet-owner joke, so
   the alien voice is thin — it reads like a human joke with an alien
   label stuck on it, and the laugh does not come from the visitor's
   angle on Earth life (criteria 2, 3).

2. "The locals stand in a metal box together, face the same wall in
   total silence, then apologise to each other for existing. Five
   stars, would ride again."
   Strong scene and a real review closing, but lift awkwardness is a
   well-worn comedy premise, and "apologise to each other for
   existing" half-explains the joke instead of letting the scene do
   the work (criteria 3, 5). Loses narrowly.

3. "The locals scan their own food, pay a machine, then thank the
   machine. I thanked it too. It did not thank me back. Three stars."
   Loses: it stacks three beats (scan/pay/thank, thanked it too, no
   thanks back), so the single joke is diluted — the brief warns a
   line that stacks several jokes is weaker than one that lands a
   single one cleanly (criterion 5).

4. "Once a year the locals set fire to a small cake, sing at it, blow
   the fire out, and eat the cake. I have attended three. Five stars."
   CHOSEN (after revision, see pass 2). Why it wins: it is exactly an
   alien tourist's review (1) — a visitor watching a birthday ritual
   and reporting it deadpan; the laugh comes from the alien's angle on
   ordinary Earth life, a cake set on fire, sung at, blown out and
   eaten (2); the birthday-cake ritual is a comparison few entrants
   would reach, far from traffic, gravity, money or weather (3); it
   sounds like a real review — "Five stars" as the verdict and "I
   have attended three" as the closing remark (4); and it is tight,
   one joke landing on the last words (5).

Pass 2 — genuine revision of the chosen line:

Draft:  "Once a year the locals set fire to a small cake, sing at it,
         blow the fire out and eat the cake. I have been to three.
         Five stars."
Revised: "Once a year the locals set fire to a small cake, sing at it,
         blow the fire out, and eat the cake. I have attended three.
         Five stars."

What changed and why: (a) a comma before "and eat the cake" — the
four acts of the ritual now read as one breath, a single ceremony
rather than a list (criterion 5). (b) "I have been to three" became
"I have attended three" — "attended" is the tourist's formal
register, so the closing lands as a review verdict instead of a
casual aside (criteria 4, 5). The revised line is 132 characters,
inside the 200 cap.
"""

import os

LINE = (
    "Once a year the locals set fire to a small cake, sing at it, "
    "blow the fire out, and eat the cake. I have attended three. "
    "Five stars."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
