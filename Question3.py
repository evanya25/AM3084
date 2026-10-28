import sympy as sp

t = sp.Symbol('t')
f = t ** 3 - 6 * t ** 2 + 9 * t + 2

print("(a) f(t) =", sp.factor(f))
print("    Roots =", sp.Poly(f, t).nroots())
print("(b) f(t)=0 roots:", sp.Poly(f, t).nroots())
print("    f(t)=2 ->", sp.solve(sp.Eq(f, 2), t))
print("(c) f'(t) =", sp.diff(f, t))
print("    f''(t) =", sp.diff(f, t, 2))
print("(d)", sp.integrate(f, t), "+ C")
print("(e)", sp.integrate(f, (t, 0, 2)))
