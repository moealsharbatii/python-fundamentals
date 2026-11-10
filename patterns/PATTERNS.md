# Pattern Cheat Sheet

Which tool fits which kind of problem. Add to this as you learn new patterns.

## First question to ask

**"Can I decide right here?"**

- **Yes:** one pass. Words like *first to appear again* or *within k* usually mean you can.
- **No:** you need the whole list first, so use two passes. Words like *every*, *exactly once* or *most* usually mean this.

---

## 1. Remembering what you've seen

**Clue:** "Have I seen this before?" or "How many times has this shown up?"

| Need | Tool | Problems |
|---|---|---|
| Just *seen or not* | `set` with `add()` and `in` | P1 |
| Seen + **where** (its index) | `dict`, value → index, plus `enumerate()` | P2 Two Sum, P3 latest position |
| Seen + **how many times** | `dict`, value → count | P4, P5 |

**Names to know:** a `dict` is a **hash map**, the general name used in interviews and other languages (`Map` in JavaScript, `HashMap` in Java). A `set` is sometimes called a **hash set**.

**Habits:**

- Ask "Which one is my memory?" The input list is what you're reading. The dict or set is what you remember.
- Counting problems are usually two loops: count everything first, then decide.

---

## 2. Walking through a list by index (sliding window)

**Clue:** "k in a row", "consecutive", "any stretch of k", "within a window".

| Tool | What it does | Example |
|---|---|---|
| `len(list)` | how many items | `len([3, 1, 4])` → `3` |
| `range(n)` | `0, 1, ..., n-1` | `range(4)` → `0, 1, 2, 3` |
| `list[start:stop]` | slice: from `start` up to **not including** `stop` | `[3, 1, 4, 1][1:3]` → `[1, 4]` |
| `sum(list)` | adds every number | `sum([3, 1, 4])` → `8` |

**Useful counts** (list of length `n`, window size `k`):

- Number of windows: `n - k + 1`
- Number of slides: `n - k`
- When index `i` leaves the window, index `i + k` enters it.

**The idea:** add up the first window once. Then for each slide, subtract the number leaving and add the number entering, and keep track of the best total.

**Steps:**

1. Not enough items for one window? Return early.
2. `total = sum(list[:k])`, the first window, once, before the loop.
3. `best = total`, so the first window counts even if the loop never runs.
4. `for i in range(n - k):` then `total = total - list[i] + list[i + k]`, and update `best`.
5. Return `best` after the loop.

**Mistakes I made (watch for these):**

- Using the index (`i`) instead of the value (`list[i]`).
- Looping over windows (`n - k + 1`) instead of slides (`n - k`).
- Setting `best` inside the loop, so it forgot earlier totals.

**Testing lesson:** a test without `assert` can never fail. Break the code on purpose (e.g. `return 999`) to prove the tests are watching. Test answers at the start, middle and end of the list.

**Problems:** P6 busiest stretch (slow version with slices first, then sliding)

---

## Coming later

- **Two pointers:** one index at each end of the list, moving toward each other.
