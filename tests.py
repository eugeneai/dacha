import nose
import os, sys, codecs
if os.name=='nt':
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

class TestBasic:
    def test_test(self):
        print ("Test of console output")
        print ("Тестирование вывода в консоль")
        assert True


if __name__=="__main__":
    pass
    nose.main()
