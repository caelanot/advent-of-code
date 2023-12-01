import std/[
  appdirs,
  dirs,
  files,
  httpclient,
  monotimes,
  paths,
  strformat,
  strscans,
  strutils,
  tables,
  times,
]

proc p(path: string): Path = Path(path)
proc `$`(path: Path): string = path.string
proc `/`(path: Path, sub: string): Path = path / Path(sub)

proc readFile(path: Path): string = readFile($path)
proc writeFile(path: Path, content: string) = writeFile($path, content)

proc recursiveWriteFile*(path: Path, content: string) =
  ## Same as `syncio.writeFile`, but will recursively create directores up to `path`
  ## if they do not exist. Will not error if a file already exists at `path`.
  createDir(path.parentDir)
  path.writeFile(content)

template timed(code: untyped): Duration =
  block:
    let start = getMonoTime()
    code
    let finish = getMonoTime()
    (finish - start)

proc getCookie(): string =
  ## Reads the user's AoC session cookie. Location is decided by `getConfigDir()`.
  let cookiePath = getConfigDir() / "aocd-nim" / "session"

  # Create a file if it doesn't exist yet, so the user can quickly paste their
  # session cookie there.
  if not fileExists cookiePath:
    cookiePath.recursiveWriteFile("")

  result = readFile(cookiePath).strip()

  if result == "":
    raise newException(IOError, fmt"Please write your AoC cookie to '{cookiePath}'.")

  var token: string
  if not result.scanf("session=$+", token):
    raise newException(
      ValueError,
      fmt"Session token should be of format 'session=128_CHAR_HEX_NUMBER', " &
      fmt"but got '{result}' instead."
    )

  if token.len != 128:
    raise newException(
      ValueError,
      fmt"Session token should be a 128 character long hexadecimal number, " &
      fmt"but got '{token}' which is {token.len} characters long."
    )

  try:
    discard parseHexInt(token)
  except ValueError:
    raise newException(
      ValueError,
      fmt"Session token should be a hexadecimal number, " &
      fmt"but could not parse' {token}' as a hexadecimal."
    )

proc getInput(year, day: int): string =
  ## Fetches the users input for a given year and day.
  ## Will cache the input after the first time this proc is called.
  let cachedInputPath = getCacheDir(p"aocd-nim") / $year / fmt"{day}.txt"
  if fileExists cachedInputPath:
    return readFile(cachedInputPath)

  echo fmt"Downloading input for year {year}, day {day}."
  let client = newHttpClient()
  defer: client.close()
  client.headers["cookie"] = getCookie()

  result = client.getContent(fmt"https://adventofcode.com/{year}/day/{day}/input")
  result.stripLineEnd
  cachedInputPath.recursiveWriteFile(result)

proc printResults(day: int, answers: OrderedTable[int, string], time: Duration) =
  echo "Day " & $day
  for partNum, answer in answers.pairs:
    echo fmt" Part {partNum}: {answer}"
  echo fmt" Time: {time.inMilliseconds:.4} ms"

template day*(year, day: int, solution: untyped): untyped =
  let input: string = getInput(year, day)
  var answers: OrderedTable[int, string]

  let time = timed:
    let input {.inject.} = input

    template part(partNum: int, answer: untyped): untyped =
      answers[partNum] = $(proc (): auto = answer)()

    solution

  printResults(day, answers, time)
