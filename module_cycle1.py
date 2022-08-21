print(f'Начало выполнения: {__name__}\n')

import module_cycle2
import module_cycle3

M1 = module_cycle2.M2 // 2

print(f'Завершение выполнения: {__name__}\n')
