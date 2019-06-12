from PIL import Image,ImageDraw,ImageFont
def add_num(img):
    draw=ImageDraw.Draw(img)
    myfont=ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=32)
    fillcolor="#ff0000"
    width,height=img.size
    draw.text((width-40,0),'99',font=myfont,fill=fillcolor)
    img.save('result.png')
    return 0

if __name__== '__main__':
    print(1)
    image=Image.open('img1.png')
    add_num(image)



