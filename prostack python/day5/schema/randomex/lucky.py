from random import choice,choices

enames=["shiva","sai","RG","SG","PG","NM","Gandhi","priya"]

luck_ename=choice(enames)
print(luck_ename)

luck_draw_list=choices(enames,k=3)
print(luck_draw_list)