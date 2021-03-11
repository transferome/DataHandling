"""A Solution to the First Problem
(The triple quotes are a multiline comment that is used to
outline modules, classes, and functions)
I'm going to solve these using functions, to show how they help
organize your code
The problem:
Make a new file, that keeps the first two columns,
but then only the frequency columns where the region
is greater than 10874354"""


def read_file(filename):
    """Read in each line of the file as a list, split by tabs, but first
    removing the new line character at the end of each line
    The function returns a list of lists, with each sublist being a line of data"""
    with open(filename) as file:
        data = [line.rstrip('\n').split('\t') for line in file]
    # return the data when function is "called"
    return data


def index_header(filedata):
    """In this case the first item in filedata is a list, which contains the
    header information.  This function is going to return a list of tuples,
    where the first element in the tuple is the index of a column name,
    and the second element is the column name
    I'm going to return the enumerate object as a list because of a more complicated
    aspect of how 'enumerate' objects work
    But the enumerate object and the list version are the same information,
    it is only represented differently"""
    return list(enumerate(filedata[0]))


def find_indexes(indexed_header):
    """This function will take the enumerated(indexed) header
    information, and find the indexes for which the region value is greater
    than 10874354
    I already know I want the first two columns, so I can reduce
    the header information I want to deal with using indexed_header[2:]
    I then have an indexed list of only the region column names.
    The region information is a string of two numbers, so the information I really want to
    test is the first number in the string.
    1. The first thing I'll do is iterate through my abbreviated indexed_header,
    and create a new list which is the indexes and only the first number in the string
    converted to an integer
    2. I'm then going to iterate through the new list, creating another new list which
    only keeps the indexes for which the region is over the desired number """
    region_index_list = list()
    for idx, column in indexed_header[2:]:
        # making new tuple that is the index, and then first number
        new_info = (idx, int(column.split('-')[0]))
        # add this to the new list
        region_index_list.append(new_info)
    keep_index_list = list()
    # Iterating through the indexes and first numbers
    for idx, number in region_index_list:
        if number > 10874354:
            # only appending the index because column name will no longer matter
            keep_index_list.append(idx)
    # return the list of indexes (now only a list of integers, not a list of tuples)
    return keep_index_list


def subset_data(foundindex, filedata):
    """In this case, since the header information has the regions in
    ascending order.  Everything from the first id number in the
    foundindex list will be kept for the data, as well as id's 0, and 1
    which represent the first and second column
    What I'll do is iterate through the file data, taking the first two elements
    of each rows data, and all elements after the first index in the foundindex list.
    I'll combine the two lists of information, and then join them together with tabs, and finally
    and a new line"""
    new_data = list()
    for line in filedata:
        # starting info (remember the 2 is up to but not including)
        starting_info = line[0:2]
        # gets all information from the first element of found index to the end of the list
        ending_info = line[foundindex[0]:]
        # combine the lists, makes one list from the two lists information
        combined_info = starting_info + ending_info
        # join the lists together with a '\t', which also turns the lists into a string
        new_line = '\t'.join(combined_info)
        # add a newline character to the end, while adding it to the new data list
        new_data.append('{}\n'.format(new_line))
    return new_data


if __name__ == '__main__':
    # the if name = main is a special statement, essentially it means the code above
    # can be reused without the code below necessarily being executed
    dat = read_file('3R_dgrp_frequencies.txt')
    indexer = index_header(dat)
    found_indexes = find_indexes(indexer)
    new_dat = subset_data(found_indexes, dat)
    # print the first 5 lines of the newly created data to investigate
    print(new_dat[0:5])
