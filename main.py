from PIL import Image
import numpy as np

def get_first_colored_index(row):
    for i, pixel in list(enumerate(row)):
        if not pixel[-1] == 0:
            return i
    return None

def trim_leading_transparent(row):
    i = get_first_colored_index(row)
    if i is not None:
        return row[i:]
    return []

def array2img(array):
    img_array = np.array(array).astype(np.uint8) 
    return Image.fromarray(img_array)
        
def run():
    path = "input/a.png"
    
    img = Image.open(path)
    width, height = img.size
    
    array = np.asarray(img)     
    pixel_map = array.tolist()
    
    for i, row in list(enumerate(pixel_map)):
        row = list(reversed(row))
        row = trim_leading_transparent(row)
        row = list(reversed(row))
        row = trim_leading_transparent(row)
        
        
        if len(row) < width:
            row_img = array2img([row])
            row_img_resized = row_img.resize((width, 1))
            
            row = np.asarray(row_img_resized).tolist()[0]
            
        pixel_map[i] = row

    img_stretched = array2img(pixel_map)
    img_stretched.show()
    
if __name__ == "__main__":
    run()
