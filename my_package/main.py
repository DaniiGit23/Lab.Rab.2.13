#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from my_package import *


def main():
    """
    Основная функция
    """
    data = file_io.input_data()
    utils.get_birthdays(data)


if __name__ == '__main__':
    main()
