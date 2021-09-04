from rest_solve import client


def test_get():
    res = client.get('/solve')

    assert res.status_code == 200


def test_post():
    data = {"table":
            [
                [1, 2, 3, 4, 0, 6, 7, 8, 9],
                [4, 0, 6, 0, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 0, 6],
                [2, 3, 4, 0, 6, 7, 8, 9, 1],
                [0, 6, 7, 8, 9, 1, 0, 3, 4],
                [8, 9, 1, 2, 3, 4, 0, 6, 7],
                [0, 4, 0, 6, 7, 8, 9, 1, 2],
                [6, 7, 8, 9, 1, 2, 3, 4, 0],
                [9, 0, 2, 3, 4, 0, 6, 7, 8]
            ]
            }
    res = client.post('/solve', json=data)

    assert res.status_code == 200
    assert res.get_json() == {"table":
                              [
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                  [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                  [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                  [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                  [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                  [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                  [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                  [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                  [9, 1, 2, 3, 4, 5, 6, 7, 8]
                              ]
                              }