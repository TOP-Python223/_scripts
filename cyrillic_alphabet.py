for i in range(ord('а'), ord('я')+1):
    print(f"{chr(i)}={i}", end=' ')
print(f"{'ё'}={ord('ё')}\n")


cyr_alph = ({chr(i): i-1071 for i in range(1072, 1078)}
            | {'ё': 7}
            | {chr(i): i-1070 for i in range(1078, 1104)})
print(cyr_alph)


part1 = {chr(i): i-1071 for i in range(1072, 1078)}
part2 = {'ё': 7}
part3 = {chr(i): i-1070 for i in range(1078, 1104)}

cyr_alph2 = part1
cyr_alph2.update(part2)
cyr_alph2.update(part3)

cyr_alph3 = {}
cyr_alph3 |= part1 | part2 | part3
