. sed linux util

Examples .
. Base
  | sed -e 's/foo/bar/'
    . |s/| means "set delimeter to /"
. File in place
  . |-i| option
  | sed -i -e 's/foo/bar/' example.md
    . Replace 'foo' on 'bar' at an example.md

Recipes .
  Unescape \n .
  . Replace \n with real return symbol
    | sed -e 's/\\n/\n/g'
  .
  Tabs to spaces .
  | sed -i -e 's/\t/  /g' cypress.json
