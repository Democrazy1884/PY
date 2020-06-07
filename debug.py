# -*- coding:utf-8 -*-
from march import March
from sub import substart
from time import sleep


def main():
    "远征debug"
    substart()
    while True:
        March.start()
        sleep(60 * 15)


if __name__ == "__main__":
    main()
