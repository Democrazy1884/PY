from time import sleep
from core.scripts import scripts_dict
from core.sub import Sub

March = scripts_dict.get("March_default")
Yukari_H = scripts_dict.get("Yukari_H")

if __name__ == "__main__":
    # TODO 写点真的日常操作
    Sub.start()
    while True:
        Yukari_H.run()
        March()
        sleep(1800)
