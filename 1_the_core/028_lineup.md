Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Lineup

To prepare his students for an upcoming game, the sports coach decides to try some new training drills. To begin with, he lines them up and starts with the following warm-up exercise: when the coach says `'L'`, he instructs the students to turn to the left. Alternatively, when he says `'R'`, they should turn to the right. Finally, when the coach says `'A'`, the students should turn around.

Unfortunately some students (not all of them, but at least one) can't tell left from right, meaning they always turn right when they hear `'L'` and left when they hear `'R'`. The coach wants to know how many times the students end up facing the same direction.

Given the list of commands the coach has given, count the number of such commands after which the students will be facing the same direction.

Example

For `commands = "LLARL"`, the output should be `solution(commands) = 3`.

Let's say that there are `4` students, and the second one can't tell left from right. In this case, only after the second, third and fifth commands will the students face the same direction.

## Notes
If only one of them has to get it wrong, I can arbitrarily decide there are two students - one who does it right, one who does not - and I can simulate this pretty easily. Also, when the command is `'A'` all I have to do is check to see if they are all lined up - I don't actually have to simulate turning around as it makes no material difference.

If I assume positions...

0 - facing front
1 - facing left
2 - facing back
3 - facing right

when the command is not `'A'`, I can just subtract from one student and add to the other.

## Solutions

### Python
```python
def solution(commands):
    a, b, count = 0, 0, 0
    for command in commands:
        if command != 'A':
            a, b = (a + 1) % 4, (b - 1) % 4
            print(command, a, b)
        if a == b: count += 1
    return count
```

### JavaScript
```javascript
function solution(commands) {
    let a = 0, b = 0, count = 0;
    for (let i = 0; i < commands.length; i++) {
        if (commands[i] != 'A') {
            a = (((a + 1) % 4) + 4) % 4;
            b = (((b - 1) % 4) + 4) % 4;
            console.log(a,b);
        }
        if (a == b) {
            count += 1
        }
    }
    return count
}
```

### C
```c
int solution(char * commands) {
    int a = 0, b = 0, count = 0;
    for (int i = 0; i < strlen(commands); i++) {
        if (commands[i] != 'A') {
            a = (((a + 1) % 4) + 4) % 4;
            b = (((b - 1) % 4) + 4) % 4;
        }
        if (a == b) {
            count += 1;
        }
    }
    return count;
}
```