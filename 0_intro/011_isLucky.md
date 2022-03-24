# Is Lucky
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

## Notes
Just make two different lists of digits and sum each and compare. 

Another approach would be to put the digits in an array and then run two concurrent sums - one from the back, one from the front - and then compare the sums.

We are gauranteed an even number of digits, so no need to fret about floats v. ints.

## Solutions

### Python
Easy to convert to a str and so the sums. Iterating over the digits 3+ times, though.
```python
def solution(n):
    digits = str(n)
    mid = len(digits) // 2
    return sum(digits[:mid]) == sum(digits[mid:])
```

### JavaScript
```javascript
function solution(n) {
    var digits = '' + n;
    var a = 0, b = 0;
    for (let i = 0; i < digits.length / 2; i++) {
        a += digits[i] * 1;
        b += digits[digits.length - i - 1] * 1;
    }
    return a === b;
}
```

### C
Trying to think of a good way to keep from looping too many times on this one. 

Find out how many digits, make an array, put the digits in and then count up like in JavaScript.

Or maybe divide the digits in half and use that somehow. The number is guaranteed to be 2, 4, or 6 digits - since the number of digits is even and n < 10^6

I got **way too hung up** on the idea that modding by 1000000 on a four digit number gives zero which doesn't affect the sum, etc. I spent way too much time trying to find something more elegant. 

I'm still not really loving what I have. 


```c
bool solution(int n) {
    if (n < 100) {
        return n % 10 == n / 10;
    } 
    int one_half = 0;
    int other_half = 0;
    int digits = 2;
    if (n > 10000) {
        digits = 3;
    }
    for (int i = 0; i < 2; i++) {
        // do this first so it only matters once
        // the first time I'm just swapping zeros
        // the second time I am flipping the halves
        other_half = one_half;
        one_half = 0;
        for (int j = 0; j < digits; j++) {
            one_half += n % 10;
            n /= 10;
        }
    }
    return one_half == other_half;
}
```