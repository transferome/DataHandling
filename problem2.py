"""  A solution to problem 2  """

# the same function to read in the data from problem1.py


def read_data(filename, header=True):
    """Read in each line of the file as a list, split by tabs, but first
    removing the new line character at the end of each line
    The function returns a list of lists, with each sublist being a line of data"""
    if header:
        with open(filename) as file:
            data = [line.rstrip('\n').split('\t') for line in file][1:]
    # return the data when function is "called"
        return data
    else:
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
    for line in filedata:
        frequencies = line[2:]
        rounded = [round(float(s), 3) for s in frequencies]
        round_list.append(rounded)
    return round_list


def organize_columns(roundedata):
    # print(roundedata[0])
    column_indexes = range(0, len(roundedata[0]))
    column_frequencies = list()
    for column in column_indexes:
        # print(column)
        temp_freq_list = list()
        for row in roundedata:
            freq = row[column]
            temp_freq_list.append(freq)
        column_frequencies.append(temp_freq_list)
    return column_frequencies


def sum_columns(organizedata):
    for column in organizedata:
        total = sum(column)
        if not total == 1:
            print(total)


if __name__ == '__main__':
    dat = read_data('3R_dgrp_frequencies.txt', header=True)
    rdat = rounded_dat(dat)
    odat = organize_columns(rdat)
    sum_columns(odat)
