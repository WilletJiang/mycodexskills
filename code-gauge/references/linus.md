# Linus-Inspired Checks

Use these checks when judging whether a planned change is structurally sound. Treat them as operational heuristics, not slogans.

## 1. Protect External Contracts

- Treat user-visible breakage as a regression by default.
- Count public APIs, CLIs, config keys, file formats, schemas, emitted events, and machine-read logs as external contracts when downstream tools depend on them.
- Before changing one, state who breaks, what migration path exists, and why the change is worth the cost.
- If the breakage is unapproved or the migration story is weak, redesign the change.

Source:
- https://yarchive.net/comp/linux/compatibility.html

## 2. Reject Made-Up Rules

- Do not enforce a style rule, architecture rule, or process rule unless it has a concrete technical reason.
- If a rule cannot point to a real bug class, correctness property, or measurable maintenance benefit, treat it as suspect.
- When a clean-looking rule conflicts with reality, prefer the technically correct design over the cosmetically tidy one.

Source:
- https://yarchive.net/comp/linux/lock_ordering.html

## 3. Remove Special Cases by Fixing Structure

- If code keeps growing branches, case tables, or flags, ask whether the data model or boundary is wrong.
- Prefer designs where the common path becomes natural and the number of exceptions goes down.
- Look for opportunities to make equivalent things truly equivalent instead of encoding extra distinctions.

Sources:
- https://yarchive.net/comp/linux/lists.html
- https://yarchive.net/comp/linux/compatibility.html

## 4. Default to Sane Behavior

- When an unknown or extended case appears, prefer a conservative fallback if that preserves correctness and compatibility.
- Do not add a special case just because the system can distinguish it.
- If the distinction does not matter to the user-visible outcome, keep the behavior simple.

Source:
- https://yarchive.net/comp/linux/compatibility.html

## 5. Prefer Clear Ownership and Boundaries

- If a change cuts across too many areas, suspect weak modularity or unclear interfaces.
- Favor boundaries that reduce cross-cutting knowledge and make responsibility obvious.
- Prefer narrow, well-defined interfaces over central coordinators that must understand everything.

Source:
- https://yarchive.net/comp/linux/maintainers.html

## 6. Use Good Taste as a Structural Test

- Interpret good taste as fewer exceptions, clearer invariants, smaller surface area, and a more natural common path.
- If a design needs repeated explanation to justify itself, assume it is not clean enough yet.
- If one design removes categories or branches that another design must constantly remember, prefer the simpler one.

Sources:
- https://yarchive.net/comp/linux/maintainers.html
- https://yarchive.net/comp/linux/lists.html

## Quick Checklist

Ask these before coding:

- Does this change preserve existing contracts?
- Am I inventing a rule that has no technical payoff?
- Am I fixing structure or only adding control-flow patches?
- Can I remove a category, branch, or flag entirely?
- Are ownership and interfaces clearer after the change?
- Is the simpler design also easier to verify?
