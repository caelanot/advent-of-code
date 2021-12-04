from aocd import data


def play_game(d1, d2, recursive=False):
    seen = set()

    while d1 and d2:
        state = (tuple(d1), tuple(d2))
        if state in seen:
            return 1, d1, d2
        seen.add(state)

        c1, c2 = d1[0], d2[0]
        d1, d2 = d1[1:], d2[1:]
        if len(d1) >= c1 and len(d2) >= c2 and recursive:
            winner, _, _ = play_game(d1[:c1], d2[:c2], True)
            if winner == 1:
                d1.extend([c1, c2])
            else:
                d2.extend([c2, c1])
        else:
            if c1 > c2:
                d1.extend([c1, c2])
            else:
                d2.extend([c2, c1])
    return 1 if d1 else 2, d1, d2


player1_deck, player2_deck = data.split('\n\n')
player1_deck = [*map(int, player1_deck.splitlines()[1:])]
player2_deck = [*map(int, player2_deck.splitlines()[1:])]

_, d1, d2 = play_game(player1_deck, player2_deck)
windeck = d1 + d2
score1 = 0
for index, card in enumerate(windeck[::-1]):
    score1 += (index + 1) * card

_, d1, d2 = play_game(player1_deck, player2_deck, recursive=True)
windeck = d1 + d2
score2 = 0
for index, card in enumerate(windeck[::-1]):
    score2 += (index + 1) * card


print(score1)
print(score2)
