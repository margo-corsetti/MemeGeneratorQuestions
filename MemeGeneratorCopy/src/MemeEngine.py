from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class MemeEngine():
    def __init__(self, out_path="W:\\Udacity\\Intermediate Python\\MemeGeneratorCopy\\src\\GeneratedMeme"):
        self.out_path = out_path

    @classmethod
    def make_meme(cls, img_path, text, author, width=500,out_path="W:\\Udacity\\Intermediate Python\\MemeGeneratorCopy\\src\\GeneratedMeme"):
        #cls.img_path = img_path
            #cls.text = text
            #cls.author = author
            #cls.width = width
            #cls.out_path
        img_path = img_path
        out_path = out_path
        print("imgpath")
        print(img_path)
        print("make_meme ran")


        def generate_image(img_path):#img_path=None, text=None, author=None, width=500):#out_path, crop=None, width=500, text=None, author=None): #img_path, out_path, crop=None, width=500, text=None, author=None):
            """Create an Image With Text

            Arguments:
                in_path {str} -- the file location for the input image.
                out_path {str} -- the desired location for the output image.
            Returns:
                str -- the file path to the output image.
            """
            img = Image.open(img_path)#in_path)
            print(img_path)

            #if crop is not None:
            #    img = img.crop(crop)

            #if width is not None:
            #    ratio = width/float(img.size[0])
            #    height = int(ratio*float(img.size[1]))
            #    img = img.resize((width, height), Image.NEAREST)

            width = float(img.size[0])
            height = float(img.size[1])
            ratio = height/width
            #print(width)
            #print(height)
            #print(ratio)

            if width is not None:
                if width > 500:
                    factor = width/500
                    new_width = int(width / factor)
                    new_height = int(new_width * ratio)
                    img = img.resize((new_width, new_height), Image.NEAREST)

            if text is not None and author is not None:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("arial.ttf", 15)
                #font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
                draw.text((10, 30), text, font=font, fill='white')


            img.save(out_path)
            #width = img.size[0]
            #height = img.size[1]
            #ratio = float(height / width)
            #print(width)
            #print(height)
            #print(ratio)
            return out_path

        img_outpath = generate_image(img_path)



    '''
    if __name__=='__main__':
        print(make_meme.generate_image('./_data/photos/dog/xander_1.jpg',
                                './_data/photos/dog_edited/out.jpg',
                                (450, 900, 900, 1300),
                                200, 'WOOOOF', 'Dr. Bork'))
    '''
