from PIL import Image
fi = raw_input("Locate the source file (e.g. /home/doga/Desktop/source.png) : ")
im = Image.open(fi).convert("RGBA")
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im, (0,0), im)
bg.save("Output.jpg", quality=95)
print "Output file saved as Output.jpg"
