from PIL import Image


def make_image(data, palette, name="output", resize=1):
    size = (len(data[0]), len(data))
    img = Image.new("RGB", size)
    img.putdata([palette[c] for line in data for c in line])
    new_size = tuple(resize*x for x in size)
    img = img.resize(new_size, Image.NEAREST)
    img.save(f"{name}.png")
    img.close()
