from PIL import Image

filename = "derick"

img = Image.open(f"{filename}.png")
width,height = img.size
pxlst = list(img.getdata())

pixels = []
pxindex = 0
row = []
for px in pxlst:
    row.append(px)
    pxindex += 1
    if pxindex >= width:
        pxindex = 0
        pixels.append(row)
        row = []

brightMatrix = []
brightrow = []
for rgbrow in pixels:
    for tup in rgbrow:
        m = min(tup)
        M = max(tup)
        avg = (m+M)/2
        brightrow.append(avg)
    brightMatrix.append(brightrow)
    brightrow = []

with open (f"{filename}.txt","w") as out:
    for r in brightMatrix:
        for val in r:
            if (0<= val) and (val <=25.5):
                print(". ",end="",file=out)
            elif (25.5 < val) and (val <= 51):
                print(", ",end="",file=out)
            elif (51.0 <= val) and (val < 76.5):
                print(": ",end="",file=out)
            elif (76.5 <= val) and (val < 102.0):
                print("- ",end="",file=out)
            elif (102.0 <= val) and (val < 127.5):
                print("= ",end="",file=out)
            elif (127.5 <= val) and (val < 153.0):
                print("+ ",end="",file=out)
            elif (153.0 <= val) and (val < 178.5):
                print("* ",end="",file=out)
            elif (178.5 <= val) and (val < 204.0):
                print("# ",end="",file=out)
            elif (204.0 <= val) and (val < 229.5):
                print("% ",end="",file=out)
            elif (229.5 <= val) and (val < 255.0):
                print("@ ",end="",file=out)
        print("",file=out)
    
