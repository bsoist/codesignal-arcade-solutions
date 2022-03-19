def solution(image):
    def blur(i, j):
        return (
            image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] +
            image[i][j-1] + image[i][j] + image[i][j+1] +
            image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]
        ) // 9
    height, width = len(image), len(image[0])
    new_image = []
    for row in range(1,height-1):
        new_row = []
        for col in range(1, width-1):
            new_row.append(blur(row, col))
        new_image.append(new_row)
    return new_image