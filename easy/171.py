def titleToNumber(column: str) ->int:
    output = 0
    for s in column:
        output = output*26 + (ord(s) - 64)
    print(output)


titleToNumber('AA')
