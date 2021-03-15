"""  A solution to problem 2  """

# the same function to read in the data from problem1.py


def read_file(filename):
    """Read in each line of the file as a list, split by tabs, but first
    removing the new line character at the end of each line
    The function returns a list of lists, with each sublist being a line of data"""
    with open(filename) as file:
        data = [line.rstrip('\n').split('\t') for line in file]
    # return the data when function is "called"
    return data


def rounded_dat(filedata):
    """Header information cannot be rounded, or the first two columns.
    Iterate through data lines, excluding the first line, and then
    excluding columns 1 and 2 (index 0 and 1), then rounding information and
    storing it in a list"""
    round_list = list()
    # the [1:] will make sure I don't include the header line
    for line in filedata[1:]:
        frequencies = line[2:]
        rounded = [round(float(s), 3) for s in frequencies]
        round_list.append(rounded)
    return round_list


if __name__ == '__main__':
    dat = read_file('3R_dgrp_frequencies.txt')
    rdat = rounded_dat(dat)
