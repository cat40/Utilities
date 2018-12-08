import re
import sys

# some constants
point_pattern = re.compile(r'\(xy -?\d+\.?\d* -?\d+\.?\d*\)')

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
    modified_point = '(xy '
    point = point[4:]
    number1 = point.split(' ')[0]
    modified_point += format(float(number1) * multiplier, '.6f')
    number2 = point.split(' ')[1][:-1]
    modified_point += ' ' + format(float(number2) * multiplier, '.6f') + ')'
    return modified_point


if __name__ == '__main__':
    fname = sys.argv[1]
    data = load_file(fname)
    data = split_data(data)
    for item in data:
        if re.match(point_pattern, item):
            pass
