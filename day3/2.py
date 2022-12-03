print([lst:=open("input.txt").read().splitlines(),d:=lambda l:l-[96,38][l<91],sum(d(ord((set(a)&set(b)&set(c)).pop()))for a,b,c in [lst[i:i+3]for i in range(0,len(lst),3)])][2])
