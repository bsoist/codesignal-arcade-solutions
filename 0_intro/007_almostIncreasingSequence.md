# Almost Increasing Sequence
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
## Solutions

### Python
```python
def solution(sequence):
    seq_len = len(sequence)
    # sequences of one element are strictly increasing
    # so if we have two, we can just remove one
    if seq_len < 3: return True
    # if removing duplicates results in removing more than one element 
    # then we can't make this strictly increasing with < 2 removals
    if seq_len - len(set(sequence)) > 1: return False
    if sequence[0] < sequence[1]:
        # first two are good, save them 
        nums = sequence[:2]
        removed = False
        # check next two
        if sequence[2] > sequence[1]:
            # still good
            nums.append(sequence[2])
        else:
            # nope, remove one
            removed = True
    elif sequence[1] < sequence[2]:
        # first two not right, save next two and remove one
        nums = sequence[1:3]
        removed = True
    else:
        # if both were wrong, this isn't going to work
        return False

    # Now check the rest    
    # I originally tried a modified verison of this part
    # w/o the code above, but it doesn't finish in time
    # unless we check the simple cases above
    for i in range(3, len(sequence)):
        if sequence[i] > nums[-1]:
            nums.append(sequence[i])
        elif removed:
            return False
        else:
            nums.pop()
            removed = True
    # so far so good, we know we have not removed more than one
    # so just double-check if the last one was right
    return sequence[-1] != sequence[-2]
```

### JavaScript
Once again, the secret here is to check for too many duplicates in an efficient manner.

My first attempt 

```javascript
if (sequence.filter((item, index) => sequence.indexOf(item) != index).length > 1) {
    return false;
}
```

was not fast enough, so I just tried adding `nums.push(sequence[i])` to the final else clause, but much like in the Python solution, that exceeds the time limit as well.


```javascript
function solution(sequence) {
    var seq_len = sequence.length;
    if (seq_len < 3) {
        return true;
    }
    // check for duplicates
    if (sequence[0] < sequence[1]) {
        var nums = sequence.slice(0,2);
        removed = false;
        if (sequence[2] > sequence[1]) {
            nums.push(sequence[2]);
        } else {
            removed = true;
        }
    } else if (sequence[1] < sequence[2]) {
        nums = sequence.slice(1,3);
        removed = true;
    } else {
        return false;
    }
    
    for (let i = 3; i < seq_len; i++) {
        if (sequence[i] > nums[nums.length - 1]) {
            nums.push(sequence[i]);
        } else if (removed) {
            return false;
        } else {
            nums.pop();
            removed = true;
        }
    } 
    return sequence[seq_len - 1] != sequence[seq_len - 2]
}
```

### C
```c
```