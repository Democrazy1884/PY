from time import sleep, time
from core.scripts import scripts_dict
from core.sub import Sub


if __name__ == "__main__":
    March = scripts_dict.get("March_default")
    Yukari_H = scripts_dict.get("Yukari_H")
    Yukari_H.set_mode("power", 200)
    # TODO 写点真的日常操作
    Sub.start()
    while True:
        timeUse = Yukari_H.run()
        March()
        marchTime = time()
        while True:
            sleep(600)
            March()
            if time() - marchTime > 60 * 60 * 2 - timeUse:
                break
