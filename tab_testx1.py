#!/usr/bin/python
#-*- coding: UTF-8 -*-

from cardobj.cardset import cardset


def main ():
    print("cardset obj start get13 test ...")
    cardpack = cardset(0);
    #print(cardpack.cardsetflag)
    cardpack.Shuffling();
    print(cardpack.cardsetflag);
    print("card0number=",cardpack.packcount());
    #print(cardpack.drawx1())
    #print(cardpack.drawx5())
    print(cardpack.drawx13())
    print(cardpack.drawx13())
    print(cardpack.drawx13())
    print(cardpack.drawx13())
    print("card0number=",cardpack.packcount());
    print(cardpack.cardsetflag);

if __name__ == '__main__':
    main()