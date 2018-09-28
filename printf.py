# -*- coding:UTF-8 -*-
while True:
    sentence = raw_input("Sentence:")
     
    screen_width = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_margin = (screen_width - box_width)//2
    inner_margin = (box_width-text_width-2)//2
    print
    print (' ' * left_margin + '+' + '-' * (box_width-2)    + '+')
    #print (' ' * left_margin + '|' + ' ' * (box_width-2)    + '|')
    print (' ' * left_margin + '|' + ' ' * inner_margin     + sentence + inner_margin * ' '+'|')
    #print (' ' * left_margin + '|' + ' ' * (box_width-2)    + '|')
    print (' ' * left_margin + '+' + '-' * (box_width-2)    + '+')
    print
