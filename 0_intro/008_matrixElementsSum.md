# Matrix Elements Sum
After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

## Notes
Create a sequence of Boolean values to indicate that all the top floor is okay unless there is a ghost. Then, check each floor - if this "column" of rooms has been ruled out already, skip it. If not, check the price. If there is a price, add it. If not, rule this column out for lower floors. 

## Solutions

### Python
```python
def solution(matrix):
    cost = 0
    countit = [True] * len(matrix[0])
    for floor in matrix:
        for i, price in enumerate(floor):
            if countit[i]:
                if price:
                    cost += price
                else:
                    countit[i] = False
    return cost
```

### JavaScript
```javascript
function solution(matrix) {
    var cost = 0;
    var countit = Array(matrix[0].length).fill(true);
    matrix.forEach(function(row) {
        for (let i = 0; i < row.length; i++) {
            if (countit[i]) {
                if (row[i] > 0) {
                    cost += row[i];
                } else {
                    countit[i] = false;
                }
            }
        }        
    })
    return cost;
}
```

### C
Since we have to iterate over the array to built the counit array (I think), I'll just do it inside the exsiting loop. See comment below.

```c
int solution(arr_arr_integer matrix) {
    int price;
    int cost = 0;
    bool countit[matrix.arr[0].size];
    for (int i = 0; i < matrix.size; i++) {
        for (int j = 0; j < matrix.arr[0].size; j++) {
            // if we're on the first row, we need an entry in counit
            if (i == 0) {
                countit[j] = true;
            }
            price = matrix.arr[i].arr[j];
            if (countit[j]) {
                if (price > 0) {
                    cost += price;
                } else {
                    countit[j] = false;
                }
            }
        }
    }
    return cost;
}
```