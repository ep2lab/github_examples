from vectormath import scalar_product, vector_product, matrix_product

def test_scalar_product():
    assert scalar_product([1, 2, 3], [4, 5, 6]) == 32
    assert scalar_product([1, 2], [5, 6])       == 17

def test_vector_product():
    assert vector_product([1, 2, 3], [4, 5, 6]) == [-3, 6, -3]
    assert vector_product([0, 0, 1], [1, 0, 0]) == [0, 1, 0]
    assert vector_product([1, 0, 0], [0, 1, 0]) == [0, 0, 1]
    assert vector_product([1, 1, 1], [1, 1, 1]) == [0, 0, 0]

def test_matrix_product():
    assert matrix_product([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    assert matrix_product([[2, 0], [0, 2]], [[1, 2], [3, 4]]) == [[2, 4], [6, 8]]
    assert matrix_product([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]) == [[58, 64], [139, 154]]
    assert matrix_product([[1]], [[2]]) == [[2]]
    assert matrix_product([[1, 2, 3]], [[4], [5], [6]]) == [[32]]