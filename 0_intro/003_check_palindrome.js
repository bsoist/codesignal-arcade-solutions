function solution(inputString) {
    for (let i = 0, n = inputString.length, e = Math.floor(n/2); i < e; i++) {
        if (inputString[i] != inputString[n-i-1]) {
            return false;
        }
    }
    return true;
}