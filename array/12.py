def to_roman(num):
    roman = { 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }
    inroman = ''
    while num:
        if num >= 1000:
            inroman+=num//1000*roman[1000]
