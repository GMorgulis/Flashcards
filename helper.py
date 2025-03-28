#breaks up the string so that it fits on the screen
def break_up(input_string):
    result = []
    i = 0
    while i < len(input_string):
        if i + 50 < len(input_string) and input_string[i + 50] != ' ':
            j = i + 50
            while j > i and input_string[j] != ' ':
                j -= 1
            if j == i: 
                result.append(input_string[i:i+50] + '—')
                i += 50
            else:
                result.append(input_string[i:j] + '\n')
                i = j + 1
        else:
            result.append(input_string[i:i+50] + '\n')
            i += 50

    return ''.join(result)
