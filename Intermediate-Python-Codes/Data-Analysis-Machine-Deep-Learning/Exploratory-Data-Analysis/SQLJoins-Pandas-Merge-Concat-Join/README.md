# SQLJoins-Pandas-Merge-Concat-Join

This repo explains how SQL joins (INNER, LEFT, RIGHT, CROSS) relate to common Pandas DataFrame operations for combining data.

---

## SQL Join Types vs Pandas

| Join Type   | SQL Purpose                                | Pandas Equivalent         | Set Logic           |
|:------------|:-------------------------------------------|:-------------------------|:--------------------|
| INNER JOIN  | Only matching rows from both tables        | `pd.merge(how='inner')`  | Intersection        |
| LEFT JOIN   | All rows from left, matching from right    | `pd.merge(how='left')`   | Set Difference (A ∪ B, keep all from A)|
| RIGHT JOIN  | All rows from right, matching from left    | `pd.merge(how='right')`  | Set Difference (A ∪ B, keep all from B)|
| OUTER JOIN  | All rows from both, fill in missing data   | `pd.merge(how='outer')`  | Union               |
| CROSS JOIN  | Every combination of both tables (cartesian product) | `pd.merge(how='cross')` or `pd.DataFrame.merge/cross` | Cartesian Product   |

---

## Pandas Concatenation

- **`pd.concat([df1, df2], axis=0)`** stacks DataFrames vertically (like SQL `UNION ALL`)—duplicates are kept.
- **`pd.concat([df1, df2], axis=1)`** stitches side by side by index.

---

## Quick Summary

- **Use `.merge()`** for database-like joins (on common columns/keys).
- **Use `.concat()`** to append rows (vertical) or columns (horizontal).
- **Use `.join()`** for a shortcut when joining on indices.

**Remember:**  
- `INNER` = only intersection  
- `LEFT`/`RIGHT` = all rows from one DataFrame, matches from the other  
- `CROSS` = all combinations (cartesian product)

---

> For examples:  
> See Pandas docs or [Real Python pandas merging](https://realpython.com/pandas-merge-join-and-concat/) and [Merge vs Join vs Concat](https://www.getgalaxy.io/learn/glossary/pandas-merge-vs-join-vs-concat).