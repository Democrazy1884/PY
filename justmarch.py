from time import sleep
from core.scripts import scripts_dict
from core.sub import Sub

March = scripts_dict.get("March_default")

if __name__ == "__main__":
    # TODO 写点真的日常操作
    Sub.start()
    while True:
        March()
        sleep(600)
