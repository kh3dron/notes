from datetime import datetime

with open ("hist-data.csv") as f:
    lines = f.read().split("\n")

#clean to minute price
clean = []
d = open("smaller_data.txt", "w")


#Starting the data at Jan 1, 2017 - Volume & volatility will never be that low again [IMO]
for x in lines[2625378:]:
    sel = [float(r) for r in x.split(",")]
    d.write(str(int(sel[0])))
    d.write(",")
    d.write(str(sel[7]))
    d.write("\n")

d.close()

