print(f'Начало выполнения: {__name__}\n')

import module_cycle1
import module_cycle2

print(f'{module_cycle1.M1 = }')
print(f'{module_cycle2.M2 = }\n')

print(f'Завершение выполнения: {__name__}\n')
