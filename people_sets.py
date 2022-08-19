# найти всех людей, который владеют одновременно русским и китайским языком
# (опционально) с номером телефона

from people_data import people

required_langs = {'RU', 'CH'}

ru_ch, rus_adult = set(), set()
for pers in people:
    # if required_langs.issubset(set(pers['langs'].split())):
    if required_langs <= set(pers['langs'].split()):
        # ru_ch.update(pers['name'])
        ru_ch |= {pers['name']}
    if 27 <= int(pers['age']) <= 55 and pers['country'] == "Russia":
        rus_adult |= {pers['name']}

print("люди, владеющие русским и китайским языками, в возрасте от 27 до 55, живущие в России")
print(*(ru_ch & rus_adult), sep='\n', end='\n\n')

print("люди, в возрасте от 27 до 55, живущие в России и не владеющие ни русским ни китайским языками")
print(*(rus_adult - ru_ch), sep='\n', end='\n\n')
