# -*- coding:utf-8 -*-
from march import March
from sub import Sub
from time import sleep


def main():
    "远征debug"
    Sub.start()
    while True:
        March.start()
        sleep(60 * 15)


if __name__ == "__main__":
    main()
