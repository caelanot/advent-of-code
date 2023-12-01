#region Coordinates
type
  Coordinate* = object
    x*: int = 0
    y*: int = 0

proc `+=`*(a: var Coordinate, b: Coordinate) =
  a.x += b.x
  a.y += b.y

proc `-=`*(a: var Coordinate, b: Coordinate): Coordinate =
  a.x -= b.x
  a.y -= b.y

proc `+`*(a: Coordinate, b: Coordinate): Coordinate =
  Coordinate(x: a.x + b.x, y: a.y + b.y)

proc `-`*(a: Coordinate, b: Coordinate): Coordinate =
  Coordinate(x: a.x - b.x, y: a.y - b.y)
#endregion

#region Directions
const
  directions4* = [
    Coordinate(x: 0, y: 1), # Up
    Coordinate(x: 1, y: 0), # Right
    Coordinate(x: 0, y: -1), # Down
    Coordinate(x: -1, y: 0) # Left
  ]

  directionsCorner* = [
    Coordinate(x: 1, y: 1), # UR
    Coordinate(x: 1, y: -1), # BR
    Coordinate(x: -1, y: -1), # BL
    Coordinate(x: -1, y: 1) # UL
  ]

  directions8* = [
    Coordinate(x: 0, y: 1), # Up
    Coordinate(x: 1, y: 1), # UR
    Coordinate(x: 1, y: 0), # Right
    Coordinate(x: 1, y: -1),
    Coordinate(x: 0, y: -1),
    Coordinate(x: -1, y: -1),
    Coordinate(x: -1, y: 0),
    Coordinate(x: -1, y: 1)
  ]
#endregion

