# Neural Style Transfer Using GANs

## Overview
This project implements **Neural Style Transfer (NST)** using **Generative Adversarial Networks (GANs)** to apply artistic styles to images while preserving their original content. The model takes two images as input:
- **Content Image**: The original image whose structure needs to be retained.
- **Style Image**: The artistic image whose patterns and colors will be transferred to the content image.

The result is a visually transformed image that blends the content with the artistic style.

## Features
- Implements **Neural Style Transfer (NST)** using TensorFlow and GANs.
- Uses a **pre-trained VGG19** model to extract content and style features.
- Supports **custom input images** for both content and style.
- Generates high-quality stylized images.
- Adjustable style intensity using hyperparameters.

## Technologies Used
- **Python**
- **TensorFlow / Keras**
- **OpenCV**
- **NumPy & Matplotlib**

## Installation
To run the project, install the required dependencies:
```sh
pip install tensorflow opencv-python numpy matplotlib
```

## Usage
1. **Prepare Input Images**
   - Choose a content image and a style image.
   - Save them in the `input_images/` folder.

2. **Run the Script**
```sh
python neural_style_transfer_with_gan.py --content content.jpg --style style.jpg --output result.jpg
```

3. **Adjust Style Intensity**
   - Modify the `style_weight` parameter in the script to control the strength of the applied style.

## Example Output
Original Content Image → Styled Image
![Neural Style Transfer with GAN](https://github.com/user-attachments/assets/240421dc-d8dd-429a-a9d0-01b2cae9c061)




## Results
- The model successfully applies artistic styles while preserving the content’s structure.
- Allows experimenting with different art styles on the same content image.

## Future Improvements
- Enhance model performance using **custom-trained GANs**.
- Implement **real-time style transfer** using optimized deep learning models.
- Improve efficiency with **faster neural networks**.


