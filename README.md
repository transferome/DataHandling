# DataHandling
code to solve different data processing problems

# Current Problems

1. Make a new file, that keeps column the first two columns, but then only the frequency columns where the region is greater than 10874354
   (removing columns from a dataframe)

2.  Read in the data, and round all of the frequency values to the thousandths place.  (If frequency is 0.003987, round to 0.004).  After rounding all the frequency values, within each region, determine if the frequencies of all the DGRP lines sums to 1.  (Checking if columns sum to 1 within a region).
3. Only keep data for dgrp lines with the following numbers ... '177', '189', '208',  '315',  '639', '818'
            (Keep a certain subset of rows
4.  Find the mean frequency of each dgrp line along the chromosome.  Add a new column to the data which is the mean frequency for each of the lines.
5.  If a dgrp line has a mean frequency of less than 0.05, remove it from the data


# scopes Folder
The two scripts within this folder illustrate how 'assignment' of objects
to a name, defines the scope in which that name lives, and thus where
the object can be 'referenced'