import os
import re
import sys
import math

# some constants
point_pattern = re.compile(r'(\(xy -?\d+\.?\d* -?\d+\.?\d*\))')
# User inputs:
HORIZONTAL_DISTANCE = 57.4  # In millimeters. Horizontal size of the logo as exported. Only used for estimate of logo size in the file names

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
    path_to_logo = 'C:\\Users\\beuchet\\OneDrive - Rose-Hulman Institute of Technology\\Documents\\MATE\\goat_silkscreen_thick\\'
    maxmul = 64
    muldiv = maxmul/2
    # go from 1/muldiv to 2/1 scale
    for mul in range(1, maxmul):
        mul /= muldiv
        size = HORIZONTAL_DISTANCE * mul
        fin = os.path.join(path_to_logo, 'goat_silkscreen_original.kicad_mod')
        fout = os.path.join(path_to_logo, f'goat_silkscreen_{size:.3f}mm.kicad_mod')
        main(fin, mul, fout)
    # fname = sys.argv[1]
    # multiplier = float(sys.argv[2])
    # fout = sys.argv[3]

