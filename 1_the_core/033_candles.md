Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Candles

When a candle finishes burning it leaves a leftover. `makeNew` leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.

You have `solutionNumber` solution in your possession. What's the total number of solution you can burn, assuming that you create new solution as soon as you have enough leftovers?

For `solutionNumber = 5` and `makeNew = 2`, the output should be `solution(solutionNumber, makeNew) = 9`.

## Notes

## Solutions

### Python
```python
def solution(candlesNumber, makeNew):
    leftovers = burned = candlesNumber
    while leftovers >= makeNew:
        burn_now = leftovers // makeNew
        leftovers %= makeNew
        leftovers += burn_now
        burned += burn_now
    return burned
```

### JavaScript
```javascript
function solution(candlesNumber, makeNew) {
    let leftovers, burned, burn_now;
    leftovers = burned = candlesNumber;
    while (leftovers >= makeNew) {
        burn_now = Math.floor(leftovers / makeNew);
        leftovers %= makeNew;
        leftovers += burn_now;
        burned += burn_now;
    }
    return burned;
}
```

### C
```c
int solution(int candlesNumber, int makeNew) {
    int leftovers, burned, burn_now;
    leftovers = burned = candlesNumber;
    while (leftovers >= makeNew) {
        burn_now = leftovers / makeNew;
        leftovers %= makeNew;
        leftovers += burn_now;
        burned += burn_now;
    }
    return burned;
}
```