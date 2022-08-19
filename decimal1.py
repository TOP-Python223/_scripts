from decimal import Decimal as D
from fractions import Fraction as F

print(f'\n{0.1 + 0.1 + 0.1 == 0.3 = }')

print(f"\n{D('0.1') + D('0.1') + D('0.1') == D('0.3') = }")

print(f"\n{F(D('0.33')).limit_denominator(10) = }")

print(f"\n{D('134.98').as_tuple() = }")

print(f"\n{D('0.0121').sqrt() = }")

print(f"\n{D('134.98').to_eng_string() = }")

print(f"\n{D('134.98').to_integral() = }")
