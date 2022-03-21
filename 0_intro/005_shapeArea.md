# Shape Area
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. 

See the problem on CodeSignal Arcade for a clarifying picture.

## Notes
Very tempting to use recursion here, but a quick analysis of the pictures suggests a simpler iterative solution.

If n == 1, area == 1.

If n > 1, add 4 * i to n for every i after n, but less than n.


## Solutions

### Python
```python
def solution(n):
    area = 1
    for i in range(1, n):
        area += 4 * i
    return area
```

### JavaScript
```javascript
function solution(n) {
    var area = 1;
    for (let i = 1; i < n; i++) {
        area += 4 * i;
    }
    return area;
}
```

### C
```c
int solution(int n) {
    int area = 1;
    for (int i = 1; i < n; i++) {
        area += 4 * i;
    }
    return area;
}
```