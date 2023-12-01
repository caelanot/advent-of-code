import strutils
import sequtils

proc numbers*(str: string): seq[int] =
  ## Parses the input as a list of numbers
  str.splitlines.map(parseInt)

proc chunks*(str: string): seq[string] =
  ## Splits input by blank lines
  str.split("\n\n")