from unittest import TestCase
from mak.gnuoy.utils.config import Config

class ConfigTests(TestCase):
    def test_fromDict(self):
        config = Config()
        config.clear()
        settings = dict({
            "Section_1": {
                "key_1": 1
            }
        })
        config.fromDict(settings)
        self.assertEqual(config.get("Section_1", "key_1"), "1")

    def test_setAndGet(self):
        config = Config()
        config.clear()
        config.set("Section_2", "key_2", "value_2")
        self.assertEqual(config.get("Section_2", "key_2"), "value_2")
