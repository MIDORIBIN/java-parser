CLASS_NAME = r'(class|interface)'
ACCESS_MODIFIER = r'public|private|protected'
STATIC = r'( +static)?'
WARD = r'(\w+)'
ZERO_BLANK = r' *'
ONE_BLANK = r' +'
ANYTHING = '(?: +(.*))?'
PARENTHESES = '\((.*)\)'

# public +(class|interface) +(\w+)
CLASS_NAME_LINE = r'public' + ONE_BLANK + CLASS_NAME + ONE_BLANK + WARD

# *public | private | protected
ACCESS_MODIFIER_LINE = ZERO_BLANK + ACCESS_MODIFIER

# *(public | private | protected)(+static)? +(\w+) + (\w+)(.*);
VARIABLE_LINE = ZERO_BLANK + '(' + ACCESS_MODIFIER + ')' + STATIC + ONE_BLANK + WARD + ONE_BLANK + WARD + '([^\(]*);'

# *(public | private | protected)(+static)?(?: +(.*))? +(\w+) *\((.*)\)
METHOD_LINE = ZERO_BLANK + '(' + ACCESS_MODIFIER + ')' + STATIC + ANYTHING + ONE_BLANK + WARD + ZERO_BLANK + PARENTHESES
