requirements and needs.

# 8-Bit Image Quantization with Floyd-Steinberg Dithering and Custom K-Means

## Introduction

This Python script performs a dual process of color quantization and dithering on images using a custom K-Means clustering implementation. Color quantization is the process of reducing the number of distinct colors in an image, while dithering aids in preserving the visual quality of the original image by reducing artifacts and smoothing transitions. Specifically, we've now implemented the capability to perform Floyd-Steinberg-Dithering. The final output is an 8-bit color palette image, limiting it to 256 unique colors.

## Features

- 8-bit color quantization: Reduce the number of colors in an image to 256 or fewer.
- Floyd-Steinberg Dithering: Newly included feature for image smoothing and artifact reduction.
- Custom K-Means implementation: Clusters the colors into a representative palette.
- Output image: Generates a quantized, dithered image using the custom color palette.

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
   - The script will generate a quantized, dithered version of the input image.
   - Open the output image to see the results.

## Planned Features

At this time, we do not have any planned new features. We will continue to maintain and improve the current features based on feedback and findings from usage.

## Contributions

Contributions to this project are welcome! If you have suggestions, improvements, or want to collaborate on further enhancing the script, please feel free to open an issue or create a pull request.

## License

This script is provided under the [MIT License](LICENSE). You are free to use, modify, and distribute it according to the terms of the license.

## Author

- Moksh Shah
- mokshnshah.me
