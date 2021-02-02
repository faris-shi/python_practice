"""
Removing Duplicates from a Sequence while Maintaining Order
"""
import collections


#to check if the item is hashable
def _is_hashable(item):
    return isinstance(item, collections.abc.Hashable)

def dedupe(seq, key=None):
    seen = set()
    for item in seq:
        is_hashable = _is_hashable(item)
        if not is_hashable and not key:
            raise ValueError(f'{item} is unhashable, need provide key parameter')
        val = item if key is None or is_hashable else key(item)
        
        if val not in seen:
            seen.add(val)
            yield item

print(list(dedupe([1,2,4,5,2,1])))

#[2, 3] will be removed since its key is 2.
print(list(dedupe([1, 2, 1, [2, 3], [4, 5], 1, 2, 3], key=lambda x: x[0])))