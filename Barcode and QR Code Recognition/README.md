# Barcode & QR Code Classification

## Goal
The main goal of this project is to classify images of barcodes, QR codes, and product labels using both traditional machine learning (SIFT + SVM) and deep learning (CNN). This classification can be useful for automated product identification, inventory management, and retail automation.

## Dataset
Dataset structure:
- **/barcode/0** -> Class 0 (Product label images)
- **/barcode/1** -> Class 1 (Barcode images)
- **/qrcode/qr_dataset** -> Class 2 (QR code images)

The dataset consists of PNG images and corresponding text files for reference.

## Description
This project implements both traditional and deep learning models for classification:
1. **SIFT + SVM Model:** Uses Scale-Invariant Feature Transform (SIFT) for feature extraction and Support Vector Machine (SVM) for classification.
2. **CNN Model:** A convolutional neural network trained on grayscale images for barcode, QR code, and product label classification.

## What I Had Done
1. Loaded and preprocessed the dataset (grayscale conversion, resizing, and normalization).
2. Extracted features using the **SIFT** algorithm for the traditional ML approach.
3. Trained an **SVM** classifier using the extracted features.
4. Designed and trained a **CNN** model for classification.
5. Compared model accuracies and visualized results using Matplotlib.

## Models Used
1. **SIFT + SVM:**
   - SIFT extracts key feature points.
   - SVM is trained on the extracted features with a linear kernel.
   - Chosen because SIFT is robust to lighting and scale variations, and SVM performs well on smaller datasets.

2. **CNN (Convolutional Neural Network):**
   - A simple CNN architecture with two convolutional layers followed by fully connected layers.
   - Chosen because CNNs are powerful for image classification and can learn spatial hierarchies of features.

## Libraries Needed
- OpenCV (`cv2`)
- NumPy (`numpy`)
- PyTorch (`torch`, `torchvision`)
- Matplotlib (`matplotlib`)
- Scikit-learn (`sklearn`)
- PIL (`PIL`)

## Accuracies
| Model        | Accuracy |
|-------------|----------|
| SIFT + SVM  | 99.85%      |
| CNN         | 100%      |


## Conclusion
This project demonstrates that deep learning (CNN) performs better on barcode and QR code classification tasks compared to traditional SIFT + SVM, which is limited by manual feature extraction. The CNN model generalizes better and provides higher accuracy.

## Your Name
T Aditya aka Mikeyzgoat  
GitHub: [Mikeyzgoat](https://github.com/mikeyzgoat)  


