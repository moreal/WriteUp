from PIL import Image

lines = open('flag.txt','r', encoding="UTF8").readlines()

im_map = {}
for line in lines:
    arr = line.strip().split(':')
    pos, color = arr[0], arr[1].split(')')[0] + ')'
    color = eval(color)
    im_map[pos] = color

width = 0; height = 0

for pos in im_map:
    x, y = map(int, pos.split(','))
    if x > width:
        width = x

    if y > height:
        height = y

print(width, height)

# Result
# width = 1366
# height = 570

im = Image.new('RGB', (int(width), int(height)), color=(0,0,0))
pixels = im.load()

for pos, color in im_map.items():
    x, y = map(int, pos.split(','))
    pixels[x, y] = color

im.show()
im.save("KK.png")