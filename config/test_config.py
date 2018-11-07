import unittest
from config import Config


class TestConfigClass(unittest.TestCase):

    def test_init(self):
        try:
            newconfig = Config()
        except Exception as e:
            self.fail("error raised unexpectedly when config object created: {}".format(e))


if __name__ == "__main__":
    unittest.main()
