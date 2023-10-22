
from mak.gnuoy.utils.config import Config

if __name__ == "__main__":
    config = Config()

    config.set("Section1", "key1", "value1")
    print(f"{config.get('Section1', 'key1')}")
    config.set("Section1", "key2", "123")
    print(f"{config.get('Section1', 'key1')}")
    config.set("Section2", "key3", "True")
    print(f"{config.get('Section2', 'key3')}")

    config.clear()
    settings = dict({
        "Section3": {
            "key4": 33
        }
    })
    config.fromDict(settings)
    print(f"{config.toDict()}")
    