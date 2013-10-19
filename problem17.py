#!/usr/bin/env python

FORMATTER = {
    1000: 'one thousand',
    100: {(i + 1) * 100: word + ' hundred' for i, word in enumerate(('one', 'two', 'three',
                                         'four', 'five', 'six',
                                         'seven', 'eight', 'nine'))},
    20: {(i + 2) * 10: word for i, word in enumerate(('twenty', 'thirty', 'forty',
                                                     'fifty', 'sixty', 'seventy',
                                                     'eighty', 'ninety'))},
    10: {i + 10: word for i, word in enumerate(('ten', 'eleven', 'twelve', 'thirteen',
                                               'fourteen', 'fifteen', 'sixteen',
                                               'seventeen', 'eighteen', 'nineteen'))},
    0: {i + 1: word for i, word in enumerate(('one', 'two', 'three', 'four', 'five',
                                             'six', 'seven', 'eight', 'nine'))}
}


def convert_num(number):
    word = []
    if number >= 1000:
        return FORMATTER[1000]
    hundreds, tens = divmod(number, 100)
    if hundreds:
        word.append(FORMATTER[100][hundreds * 100])
    if hundreds and tens:
        word.append('and')
    if tens in range(10, 20):
        word.append(FORMATTER[10][tens])
    else:
        tens, ones = divmod(tens, 10)
        if tens:
            word.append(FORMATTER[20][tens * 10])
        if ones:
            word.append(FORMATTER[0][ones])
    return ' '.join(word)


def main():
    total_letters = 0
    for number in range(1, 1001):
        total_letters += len(convert_num(number).replace(' ', ''))
    print(total_letters)


if __name__ == "__main__":
    main()
