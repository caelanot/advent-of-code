include ../aoc
import nre

2023.day 1:
  part 1:
    var sum = 0
    for line in input.splitLines:
      var p = line.findAll(re"(\d)")
      sum += (p[0]&p[^1]).parseInt
    sum

  part 2:
    var
      sum = 0
      nums = [("one", "1"), ("two", "t2o"), ("three", "t3e"),
              ("four", "4"), ("five", "5e"), ("six", "6"),
              ("seven", "7"), ("eight", "e8t"), ("nine", "n9e")]
    for line in input.splitLines:
      var p = line.multiReplace(nums).findAll(re"(\d)")
      sum += (p[0]&p[^1]).parseInt
    sum