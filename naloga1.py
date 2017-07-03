def pascal(n):
    """
    Yield gre do vrstice n Pascalovega trikotnika.

    The first row is row 0.
    """
    def newrow(row):
        "Izračuna novo vrstico"
        prev = 0
        for x in row:
            yield prev + x
            prev = x
        yield 1

    prevrow = [1]
    yield prevrow
    for x in range(n):
        yield prevrow
        prevrow = list(newrow(prevrow))
        
