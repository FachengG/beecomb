from utils.finalize import Clean_up
from utils.initial import Set_up


class Test_db_functions:
    def test_set_up(self):
        set_up = Set_up()
        assert set_up.init_db() is True

    def test_clean_up(self):
        clean_up = Clean_up()
        assert clean_up.purge_db() is True
