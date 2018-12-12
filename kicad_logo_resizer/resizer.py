import re
import sys
import math

# some constants
point_pattern = re.compile(r'(\(xy -?\d+\.?\d* -?\d+\.?\d*\))')

'''
(xy ###.## ###.##)
'''


def load_file(fname):
    '''
    Loads a file at the specified path and returns a multi-line string
    :param fname: path to file
    :return: the file, in one multi-line string
    '''
    with open(fname, 'r') as f:
        return f.read()


def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def split_data(data):
    return re.split(point_pattern, data)


def modify_point(point, multiplier):
    '''
    multiplies all numbers in the point by the multiplier
    Assumes all points of of the form (xy ###.## ###.##)
    :param point: string, point to be modified
    :param multiplier: float, value to multiply the point by
    :return: string, modified point
    '''
    def format_number(n):
        return format(math.floor(n * 10**6) / 10**6, '.6f')
        # return format(round(n, 6), '.6f')
    modified_point = '(xy '
    point = point[4:]
    number1 = point.split(' ')[0]
    modified_point += format_number(float(number1) * multiplier)
    number2 = point.split(' ')[1][:-1]
    modified_point += ' ' + format_number(float(number2) * multiplier) + ')'
    return modified_point


def main(fname, multiplier, fout):
    data = load_file(fname)
    modified_data = ''''''
    data = split_data(data)
    # print(data)
    for item in data:
        if re.match(point_pattern, item):
            modified_data += modify_point(item, multiplier)
            # print('modified point:', modify_point(item, multiplier))
        else:
            # print(item)
            modified_data += item
    with open(fout, 'w') as output:
        output.write(''.join(modified_data))


if __name__ == '__main__':
    fname = sys.argv[1]
    multiplier = float(sys.argv[2])
    fout = sys.argv[3]

