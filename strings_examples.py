# strings can be created with single or double quotes
girl = 'Sarah'
boy = "Luke"
tupl = girl, boy
tupl
g, b = tupl


# this way you can embed quote types with another
"Someone's"

# blackslah followed by specific characters represent 'escape sequences'
s = 'a\nb\tc'
s
print(s) # s and print(s) are not equivalent
len(s) # escape sequences comprise at least two characters but represent only one byte

# the reason len(s) results in 5 is that the string contains an a, newline, b, tab, and c byte
# basically the backslahes don't count
print('a\\b') # actually backslash
print('a\b') # backspace
print('a\rb') # carriage return, i don't know what this does
print('a\vb') # vertical tab (so a space?)

# good to keep these in mind
myfile = open('C:\new\text.dat', 'w')
myfile = open(r'C:\new\text.dat', 'w') # placing r infront of filename turns it into a raw-string
print(r'C:\new\text.dat')

# basic operations
len('abc') # length
'abc' + 'def' # concatenation
'Ni!' * 4 # repetition

# iterator and membership supported
myjob = 'hacker'
for s in myjob:
    print(x, end=' ')

'k' in myjob
'z' in myjob

# indexing a slicing
S = 'Hummingbird'
S[0], S[-2] # indexing
S[1:4], S[4:], S[:-1]
# [:-1] can be interpreted as [0:(11-1)] so -1 is last item and thus noninclusive

T = S
T is S
W = S[:] # this preforms a top-level copy, basically T is not referring directly to S anymore
# which i'm not sure what that means
W is S

S[1:8:2] # final argument is a stride index, basically steps, default value is 1

S[::2] # Every other item from beginning to end

S[::-1] # Every item stepping in reverse

S[5:1:-1] # First two reversed for negative steps, fetches items 2 to 5 in reverse order

# Immutable, have to modify by reassignment
S[0] = 'x'

S = 'h' + S[1:]
S

# replace method and immutability
S.replace('h', 'H')
S
S.replace('m', 'M')
S1 = S.replace('h', 'H')
S1

# methods
S
S.capitalize()
# capitalize
S.lower()
S.upper()
str = "     this is string example....wow!!!     "
str.rstrip()
str = "88888888this is string example....wow!!!8888888"
str.rstrip('8')
str.lstrip('8')

# index of last occurence of substring
word = 'CatBatSatMatGate'
word.rfind('ate')
word.find('ate')
word = 'Cat Dog Cat Dog Dog'
word.rfind('Cat')
# difference from find
word.find('Cat')

# split, very useful
line = 'Number\tSample\tvar1\tvar2\tvar3\ttype'
line.split('\t')
line = 'Ob1 Ob1 Ob1 Diff Diff Diff Diff'
line.split(' ')

# endswith , startswith
S
S.upper().startswith('H')
S.startswith('humm')
S.endswith('bird')

# join
join_by = 'BIRD!'
join_by.join(['Item1', 'Item2', 'Item3', 'Item4'])
# alternatively
'BIRD!'.join(['Item1', 'Item2', 'Item3', 'Item4'])


## String formattingA
insert1 = 'Flies'
insert2 = 'fruit'

# format is a string method, replacing the {} with respective variable
'{} eat {}!!!'.format(insert1, insert2)

# the preferred method is now to use f strings which are new to python 3.6 and not compatible with
# earlier python versions
f'{insert1} eat {insert2}!!!'

# the second version is obviously easier to read