"""Третий модуль многофайлового проекта."""
print(f'Начало выполнения: {__name__}\n')

import module2

def without_builtins(namespace: dict) -> dict:
    return {
        name: obj
        for name, obj in namespace.items()
        if not name.startswith('__')
    }

M3 = 300

print(f'Завершение выполнения: {__name__}\n')
