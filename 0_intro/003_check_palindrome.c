bool solution(char * inputString) {
    for (int i = 0, n = strlen(inputString); i < n / 2; i++) {
        if (inputString[i] != inputString[n-i-1]) {
            return false;
        }
    }
    return true;
}
