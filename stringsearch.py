#function to check if small string is there in big string
from tkinter import Y


def check(string, sub_str):
    if (string.find(sub_str)==-1):
        print("NO")

    else:
           print("YES")


x = "This is a rainy season. This season is very useful for the food grain production in india. For india tobe able to self reliant in food grain productionit is very important that this season delivers healthy rinfall.In india rainfall is very much influenced by westerly winds that are also called as monsoon"
y = "hypnotyse"
check(x,y)