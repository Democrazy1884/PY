# -*- coding:utf-8 -*-
from core.march import March
from core.sub import Sub
from time import sleep

# from core.page import Main


def main():
    "远征debug"
    Sub.start()
    while True:
        March.start()
        sleep(60 * 15)


if __name__ == "__main__":
    main()
