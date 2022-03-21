# Adjacent Elements Product 
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

## Notes
The input array is gaurenteed to be less than 11 elements, so brute force should do this just fine.

## Solutions

### Python
```python
def solution(inputArray):
    max_product = float('-inf')
    for i in range(1, len(inputArray)):
        max_product = max(max_product, inputArray[i] * inputArray[i-1])
    return max_product
```

### JavaScript
```javascript
function solution(inputArray) {
    maxProduct = -Infinity;
    for (let i = 1; i < inputArray.length; i++) {
        if (inputArray[i] * inputArray[i - 1] > maxProduct) {
            maxProduct = inputArray[i] * inputArray[i - 1];
        }
    }
    return maxProduct;
}
```

### C
No need to deal with type casting. I'll assume the smallest product possible is the minimum possible element * the maximum possible element (since some elements may be < 0>).
```c
int solution(arr_integer inputArray) {
    int max_product = -1000 * 1000;
    int this_product;
    for(int i = 1; i < inputArray.size; i++) {
        this_product = inputArray.arr[i] * inputArray.arr[i - 1];
        if (this_product > max_product) {
            max_product = this_product;
        }
    }
    return max_product;
}
```