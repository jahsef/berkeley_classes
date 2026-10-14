from pytest_grader import points


@points(0)
def dictionaries_wwpd():
    """What Would Python Display?

    >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
    >>> pokemon['pikachu']
    LOCKED: d96dd3d1eabdb8e7
    >>> len(pokemon)
    LOCKED: 54e79f12274ed53e
    >>> 'mewtwo' in pokemon
    LOCKED: d023210721f7195e
    >>> 'pikachu' in pokemon
    LOCKED: 5d6fbef7bcf69be5
    >>> 25 in pokemon
    LOCKED: cb2facda0e4d7646
    >>> 148 in pokemon.values()
    LOCKED: 59aa3fdf59d4b4b5
    >>> pokemon.get('mew', 100000)
    LOCKED: b30051027649f5e0
    >>> pokemon.get('mewtwo', 10)
    LOCKED: c6db3be215c08fbf
    >>> {pokemon[k]: k for k in pokemon if len(k) < 5}
    LOCKED: 0c73e1ca85bf1bbd
    >>> min(pokemon, key=len)
    LOCKED: 83aa6e3cf3255a27
    >>> pokemon[min(pokemon, key=len)]
    LOCKED: 4e01426c80bb53cc
    """
