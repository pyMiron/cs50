def strip_string(string_chars=' '):
    def do_string(string):
        return string.strip(string_chars)

    return do_string()

strip1 = strip_string(' ')
strip2 = strip_string(' !?,.;')
print(strip1(' hello python!.. '))
print(strip2(' hello python!.. '))
