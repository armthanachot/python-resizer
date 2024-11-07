from PIL import Image
import cairosvg

def png_to_svg(input_file, output_file):
    # Open the PNG file using Pillow
    img = Image.open(input_file)
    
    # Ensure the image has an alpha channel (transparency)
    img = img.convert('RGBA')
    
    # Save as temporary PNG to ensure it's properly formatted
    temp_png = 'temp_image.png'
    img.save(temp_png, format='PNG')

    # Convert the PNG to SVG using cairosvg
    with open(temp_png, 'rb') as png_file:
        png_data = png_file.read()
        cairosvg.svg2svg(bytestring=png_data, write_to=output_file)

    print(f"SVG saved at: {output_file}")

# Example usage
png_to_svg('./source/mybp-logo.png', './source/mybp-logo.svg')