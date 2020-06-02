# -*- coding:utf-8 -*-
from march import March
from sub import substart
from time import sleep


def main():
    substart()
    while True:
        March.start()
        sleep(60)


if __name__ == "__main__":
    main()
