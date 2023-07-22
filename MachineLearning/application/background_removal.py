!pip install rembg

from rembg import remove
from PIL import Image

input_path = 'pita.jpg'
output_path = 'pita_witout_bg.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

show = Image.open(output_path)
show.show()
