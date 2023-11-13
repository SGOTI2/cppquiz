ogT = """"""
ogT = ogT.replace('"que_desc":',"type:``, question: ")
ogT = ogT.replace('"ans1":', "answers:[")
ogT = ogT = ogT.replace('"ans2":',"")
ogT = ogT.replace('"ans3":',"")
ogT = ogT.replace('"ans4":',"")
ogT = ogT.replace('"true_ans":','],answer:')
ogT = ogT.replace(' ?',"?")
print(ogT)