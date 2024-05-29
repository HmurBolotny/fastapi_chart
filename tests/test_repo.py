# from .. import SqlRepo


class SqlRepo:
    ...


def test_save_data():
    data = {}
    repo = SqlRepo()
    res = repo.create(data)
    assert res == True
