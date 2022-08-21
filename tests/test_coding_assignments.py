from src.json_file_methods import JsonFileMethods


def test_coding_assignment():
    assert_array = []
    js = JsonFileMethods()

    # Fetching the number of wicketkeepers in the team
    wk_count = js.get_wicketkeeper_count()
    if wk_count != 1:
        assert_array.append("The team does not have only 1 wicketkeeper")

    # Fetching the number of foreign players in the team
    fp_count = js.get_foreign_players_count()
    if fp_count != 4:
        assert_array.append("The team does not have 4 foreign players")

    assert not assert_array, assert_array
