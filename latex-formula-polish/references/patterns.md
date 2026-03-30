# LaTeX Formula Polish Patterns

Use these patterns when the main skill workflow tells you what to improve but you need a concrete rewrite strategy.

## 1. Condense A Fragmented Derivation

Problem:
- six short lines feel choppy
- each line carries only one small term

Approach:
- group terms with the same coefficient or denominator
- keep negative storage terms together
- keep remainder terms together

Example pattern:

```tex
\begin{align}
T_k
&\le a_k \notag\\
&\quad + b_k \notag\\
&\quad + c_k \notag\\
&\quad - d_k \notag\\
&\quad - e_k \notag\\
&\quad + f_k.
\end{align}
```

becomes

```tex
\begin{align}
T_k
&\le a_k + b_k \notag\\
&\quad + c_k + f_k \notag\\
&\quad - d_k - e_k.
\end{align}
```

Only do this when the grouped terms still read naturally.

## 2. Align `=` With Continuation Signs

Problem:
- first line starts at `=`
- continuation lines start at inconsistent `+` positions

Preferred pattern:

```tex
\begin{equation}
\begin{aligned}
\dd X(t)
&=
\Bigl[\cdots\Bigr]\dd t \\
&{}+{}
\Bigl[\cdots\Bigr]\dd W(t) \\
&{}+{}
\int_{\mathcal Z}\cdots \,\widetilde N(\dd t,\dd z).
\end{aligned}
\end{equation}
```

If the continuation must sit directly under the operator slot of the first line, use:

```tex
\phantom{=}+ \cdots
```

Prefer a real shared anchor first; use `\phantom` only for a specific operator-slot alignment effect.

## 3. Stabilize A Heavy Drift Line

Problem:
- one continuation line contains only a short negative block
- the formula feels visually lopsided

Approach:
- keep the dominant deterministic block on the first line
- move additive nonlinear or delay terms to the next line

Pattern:

```tex
\begin{aligned}
\dd X(t)
&=
\Bigl[
-CX(t)-\kappa LX(t)-PM\widehat X(t)
\\
&\quad {}+{} A\Phi(X(t))+B\Psi(X(t-\sigma))
\Bigr]\dd t.
\end{aligned}
```

This usually reads better than breaking after every sign.

## 4. Turn Side-By-Side Definitions Into A Vertical Pair

Problem:
- two long definitions on one line overflow or look crowded

Pattern:

```tex
\[
\begin{aligned}
\Phi(X)&:=\operatorname{col}(\cdots),\\
\Psi(X)&:=\operatorname{col}(\cdots).
\end{aligned}
\]
```

Use the same idea for `D_x/E_y`, `\mathcal D_N/\mathcal V_N`, `\Gamma_{11}/\Gamma_{12}/\Gamma_{22}`, and similar blocks.

## 5. Recast Long Inequalities

Problem:
- a single-line estimate contains drift, diffusion, and jump terms
- `\le` is visually lost

Pattern:

```tex
\begin{equation}
\begin{aligned}
&2x^\top Q[\cdots] \\
&{}+\|S_1x+S_2y\|^2
+\lambda_J\|R_1x+R_2y\|^2 \\
&{}\le -\beta_1\|x\|^2+\beta_2\|y\|^2.
\end{aligned}
\end{equation}
```

The key is to align the leading `+` and `\le` on the same column.

## 6. Build Parameter Grids With `alignedat`

Problem:
- multiple matrices or parameters listed sequentially create ragged blocks

Pattern:

```tex
\[
\begin{alignedat}{2}
C&=\begin{bmatrix}\cdots\end{bmatrix},
\qquad
&A&=\begin{bmatrix}\cdots\end{bmatrix},\\
B&=\begin{bmatrix}\cdots\end{bmatrix},
\qquad
&L&=\begin{bmatrix}\cdots\end{bmatrix},\ \kappa=0.06,\\
P&=I_2,
\qquad
&M&=\begin{bmatrix}\cdots\end{bmatrix}.
\end{alignedat}
\]
```

Use a second `alignedat` block for `S_1/S_2` and `R_1/R_2` if that keeps the page calmer.

## 7. Decide Whether To Wrap `diag(...)`

Wrap a long `\operatorname{diag}(...)` only when:
- it actually overruns the measure
- it breaks the grid rhythm
- the wrapped form still looks intentional

Keep it on one line when:
- the page width allows it
- wrapping would create unnecessary vertical noise

## 8. Escalate Carefully

Only after local restructuring:
- reduce excessive `\qquad` gaps
- consider lighter global flexibility such as `\emergencystretch`
- consider `\allowdisplaybreaks[1]` for long derivations

Avoid shrinking math or introducing ad hoc negative spaces unless the improvement is clearly justified.
