#!/usr/bin/python
#-*- coding: UTF-8 -*-

#from socket import SocketType
import random
#print(random.randrange(10, 51))

class cardset():
    ''' define poker a pack of cards
        #total 54 card 0..53 add 2 joker 
        #1 byte [type][number] type(0:RH,1:RD,2:BF,3:BH ), number(1..9,a(Ace),b(Jack),c(Queen),d(King)) , joker(smalljoker:0e,bigjoker:1e)
        #defind suits (0:RH:hearts),(1:RD:diamonds),(2:BF:clubs),(3:BH:spades)
    '''
    card_set = [    
	    0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,
	    0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,0x1c,0x1d,
	    0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2a,0x2b,0x2c,0x2d,
	    0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x3a,0x3b,0x3c,0x3d,
	    0x0e,0x1e]
    ''' cardtype 0..6 '''
    cardtype=[
		[ 0,51], #0 standy 52 card mode
		[ 0,53], #1 2 joker 54 card mode
		[ 0,12], #2 13 card of 0:RH mode hearts
		[13,25], #3 13 card of 1:RD mode diamonds
		[26,38], #4 13 card of 2:BF mode clubs
		[39,51], #5 13 card of 3:BH mode spades
		[52,53]  #6 2 card of joker mode
    ]
    ctype=0;
    cardsize=54;
    cardsetflag=[0]*cardsize;

    def __init__(self,ctype):
        self.ctype=ctype;
        if(self.ctype>6 or self.ctype<0):
           self.ctype=0
        r1=self.cardtype[self.ctype][0]
        r2=self.cardtype[self.ctype][1]+1
        self.cardsetflag = [0]*self.cardsize
        for setinx in range(r1,r2):
            self.cardsetflag[setinx]=1

    def Shuffling(self):    # 洗牌
        ''' restart cardpack buffer'''
        self.cardsetflag = [0]*self.cardsize
        r1=self.cardtype[self.ctype][0]
        r2=self.cardtype[self.ctype][1]+1
        self.cardsetflag = [0]*self.cardsize
        for setinx in range(r1,r2):
            self.cardsetflag[setinx]=1

    def packcount(self):# 計算剩下張數
        ''' conunt '''
        ct=0;
        for v in self.cardsetflag:
            if(v==1):
                ct=ct+1
        return ct

    def drawx1(self):#抽牌1張
        ''' get 1 card'''
        rseed=random.randrange(1, 108);
        #print("1",rseed);
        if(self.packcount()>0):
            rinx=0
            while rseed>0:
                if rinx>=self.cardsize-1:
                    rinx=0
                else:
                    rinx=rinx+1
                if(self.cardsetflag[rinx]==1):
                    rseed=rseed-1
                    if(rseed<=0):
                        self.cardsetflag[rinx]=0
                        cc = self.card_set[rinx]
                        return "0x%0.2X"%cc
        else:
            cc = 0x3f
            return "0x%0.2X"%cc

    def drawx5(self):#抽牌5張
        ''' get 5 card '''
        c5list=[]
        for i in range(5):
            c5list.append(self.drawx1())
        return c5list


    def drawx13(self):#抽牌13張
        ''' get 13 card '''
        c13list=[]
        for i in range(13):
            c13list.append(self.drawx1())
        return c13list


class user_cardbuff():
    cardsize=0;
    cardflag=[];
    carddat=[];
    chkcardbuf=[];
    overcard=[];
    passflag=0;
    
    def __init__(self):
        cardsize=0;
        cardflag=[];
        carddat=[];
        chkcardbuf=[];
        overcard=[];
        passflag=0;
    
    def setchkbuf(self,cklist):
        chkcardbuf=chkcklist;
    
    def dochk(self):
        cnt=0;
        for(i in chkcardbuf):
            if(i in carddat):
                cnt=cnt+1
        
        return cnt
                
    def setover(self,card):
        if(card in carddat):
            carddat.remove(card)
            overcard.append(card)
            return overcard;
        else:
            return 0x00;
        
    def pushoutcard(self,card):
        if(card in carddat):
            carddat.remove(card)
            return card;
        else:
            return 0x00;
        
   
class game_cardbuff():
    cardflag0=0;
    cardflag1=0;
    cardflag2=0;
    cardflag3=0;
    carddat0=[];
    carddat1=[];
    carddat2=[];
    carddat3=[];
    chkcardbuf=[];
    
    def __init__(self):
        cardflag0=0;
        cardflag1=0;
        cardflag2=0;
        cardflag3=0;
        carddat0=[];
        carddat1=[];
        carddat2=[];
        carddat3=[];
        chkcardbuf=[];
    
    
        
        


def main():
    print("cardset obj start test v1.0 20230121 handel  ...")
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

    print("cardset obj start get5 test ...")
    cardpack1 = cardset(1);
    cardpack1.Shuffling();
    print(cardpack1.cardsetflag);
    print("card1number=",cardpack1.packcount());
    print(cardpack1.drawx5())
    print(cardpack1.drawx5())
    print(cardpack1.drawx5())
    print(cardpack1.drawx5())
    print(cardpack1.cardsetflag);
    print("card1number=",cardpack1.packcount());

if __name__ == '__main__':
    main()