import nose
import os
import sys
import codecs
from models import create_debug_engine, create_session, print_session
import models
from data_t import populate_all

if os.name == 'nt':
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

de = create_debug_engine(True)
create_session(de)
print(models.SESSION)
populate_all(models.SESSION)


class TestBasic:
    def test_test(self):
        print("Test of console output")
        print("Тестирование вывода в консоль")
        assert True


if __name__ == "__main__":
    pass
    nose.main()
