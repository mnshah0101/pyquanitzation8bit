
# 8-Bit Image Quantization with Custom K-Means

## Introduction

This Python script is designed to perform 8-bit color quantization on images using a custom K-Means clustering implementation. Color quantization is the process of reducing the number of distinct colors in an image while preserving its visual quality. In this script, we aim to convert an image into an 8-bit color palette, effectively limiting it to 256 unique colors.

## Features

- 8-bit color quantization: Reduce the number of colors in an image to 256 or fewer.
- Custom K-Means implementation: Clusters the colors into a representative palette.
- Output image: Generates a quantized image using the custom color palette.

## Usage

To use the script, follow these steps:

1. **Installation**:
   - Ensure you have Python installed (Python 3 recommended).
   - Install required libraries if not already installed: `numpy`, `PIL` (Pillow).

2. **Running the Script**:
   - Execute the script using the command-line with the following syntax:
     ```bash
     python Main.py input_image.png
     ```

   - Replace `input_image.png` with the path to your input image.

3. **Viewing the Results**:
   - The script will generate an 8-bit quantized version of the input image.
   - Open the output image to see the results.

## Planned Features

In the future, we plan to enhance this script by adding dithering techniques to further improve the visual quality of the quantized images. Dithering is a method to reduce artifacts and smooth transitions in the quantized images.

## Contributions

Contributions to this project are welcome! If you have suggestions, improvements, or want to collaborate on implementing dithering, please feel free to open an issue or create a pull request.

## License

This script is provided under the [MIT License](LICENSE). You are free to use, modify, and distribute it according to the terms of the license.

## Author

- Moksh Shah
- mokshnshah.me

Feel free to provide your contact information and other relevant details. This README is a starting point, and you can expand on it based on your project's
