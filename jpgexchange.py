from PIL import Image
jpg=Image.open('bbq.jpg')
L=jpg.convert('L')
width,height=L.size
nwidth=int(width/4)
nheight=int(height/8)
L=L.resize((nwidth,nheight))
t=''
bianma='@%#+=-:.'

for row in range(nheight):
    for column in range(nwidth):
        t=t+bianma[int((L.getpixel((column,row)))/256*8)]
    t+='\n'
with open ('zhuanhuantu.txt','w') as f:
    f.write(t)


