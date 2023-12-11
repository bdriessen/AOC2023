
# read input file into a list of lists of numbers separated by blank lines

def read_input_file():
    with open("input.txt") as f:
        # Read lines from file
        lines = f.read().split("\n")
        # return list of lines
        print(lines)
    return lines


def convert(line):
    # Search for substring "one" and replace with "1"
    line = line.replace("one", "1")
    # Search for substring "two" and replace with "2"
    line = line.replace("two", "2")
    # Search for substring "three" and replace with "3"
    line = line.replace("three", "3")
    # Search for substring "four" and replace with "4"
    line = line.replace("four", "4")
    # Search for substring "five" and replace with "5"
    line = line.replace("five", "5")
    # Search for substring "six" and replace with "6"
    line = line.replace("six", "6")
    # Search for substring "seven" and replace with "7"
    line = line.replace("seven", "7")
    # Search for substring "eight" and replace with "8"
    line = line.replace("eight", "8")
    # Search for substring "nine" and replace with "9"
    line = line.replace("nine", "9")
    return line

def convert2(line):
    # Search for substring "oneight" and replace with "1ight"
    cline = line

    cline = cline.replace("eightwo", "8wo")
    cline = cline.replace("eighthree", "8hree")
    cline = cline.replace("threeight", "3ight")
    cline = cline.replace("fiveight", "5ight")
    cline = cline.replace("nineight", "9ight")
    cline = cline.replace("oneight", "1ight")
    cline = cline.replace("sevenine", "7ine")
    cline = cline.replace("twone", "2ne")
    return cline

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def find_alfa_digit(line):
    # find the first occurances of "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    # return the index of the first occurance
    s = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first_index = 1000
    last_index = -1
    first_number = -1
    last_number = -1

    for i in range(len(s)):
        index = line.find(s[i])
        if index != -1 and index < first_index:
            first_index = index
            first_number = i+1
            # print("first_index = ", first_index, "number = ", number)
    for i in range(len(s)):
        index = line.rfind(s[i])
        if index != -1 and index > last_index:
            last_index = index
            last_number = i+1
            # print("first_index = ", first_index, "number = ", number)
    print(first_number, last_number)
    return first_number, last_number

def find_digit_left(line):
    index = -1
    for c in line:
        index += 1
        if c.isdigit():
            return int(c), index
    return -1, -1
def find_digit_right(line):
    index = -1
    for i in range(len(line), 0, -1):
#        print("fdr:", i, line[i-1])
        if line[i-1].isdigit():
            return int(line[i-1]), i-1
    return -1, -1

def find_alfa_digit_left(line):
    s = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    index = 0
    num = []
    ind = []
    while index < len(line):
        for i in range(len(s)):
            if line[0:index].find(s[i]) != -1:
                num.append(i+1)
                ind.append(index-len(s[i]))
#                print("i = ", i, "index = ", index, "line = ", line[0:index])
        index += 1

    print(num, ind)

    # find minumum index and corresponding number
    min_index = 1000
    min_number = -1
    for i in range(len(ind)):
        if ind[i] < min_index:
            min_index = ind[i]
            min_number = num[i]
    return min_number, min_index

def find_alfa_digit_right(line):
    s = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    index = len(line)
    num = []
    ind = []
    while index > 0:
        for i in range(len(s)):
            if line[(index-1):].find(s[i]) != -1:
                num.append(i+1)
                ind.append(index-1)
        index -= 1
    # find maximum index and corresponding number
    max_index = -1
    max_number = -1
    for i in range(len(ind)):
        if ind[i] > max_index:
            max_index = ind[i]
            max_number = num[i]
    return max_number, max_index


# main program
def main():
    s = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # read the input file
    input = read_input_file()

    total = 0
    for line in input:
        left_num, left_index = find_digit_left(line)
        if left_index == -1:
            left_index = 1000

        print(left_num, left_index)
        right_num, right_index = find_digit_right(line)
        print(right_num, right_index)
        left_num_alfa, left_index_alfa = find_alfa_digit_left(line)
        print(left_num_alfa, left_index_alfa)
        right_num_alfa, right_index_alfa = find_alfa_digit_right(line)
        print(right_num_alfa, right_index_alfa)
        if left_index_alfa < left_index:
            left_num = left_num_alfa
        if right_index_alfa > right_index:
            right_num = right_num_alfa
        print("Line result: ", left_num, right_num)
        total += 10*left_num + right_num
        print("Total: ", total)

        # first_index, number = 1000, -1
        # cline = line
        # dline = line
        # # change the line by changeing the words to numbers
        # first_number, last_number = find_alfa_digit(cline)
        # if first_number != -1:
        #     cline = cline.replace(s[first_number-1], str(first_number), 1)
        # if last_number != -1:
        #     cline = rreplace(cline, s[last_number-1], str(last_number), 1)
        #
        # # find digits in the dline
        # x = []
        # for i in range(len(dline)):
        #     if dline[i].isdigit():
        #         x.append(int(cline[i]))
        # num = 0
        # if len(x) == 0:
        #     if first
        # if len(x) == 1:
        #     num = x[0]+10*x[0]
        # if len(x) >= 2:
        #     num = 10*x[0]+x[-1]
        # print(line, cline, num)
        # total += num
    print(total)


# start main program
main()


