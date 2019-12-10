from collections import OrderedDict

f = dict()
f[1] = 45
f[2] = 46
f[3] = 97
f[6] = 6
open_list = []
open_list.append(2)
open_list.append(6)

sorted_f = OrderedDict(sorted(f.items(), key = lambda x : x[1]))
print(open_list)

for tile in sorted_f.keys():
    if tile in open_list:
        current_tile = tile
        open_list.remove(tile)
        break

print(sorted_f.keys())
print(current_tile)
print(open_list)