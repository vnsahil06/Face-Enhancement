
# Face Enhancement & Image Restoration

### AI-Powered Image Upscaling and Facial Restoration Using Real-ESRGAN and GFPGAN

<p align="center">
  <strong>Enhancing image quality through deep learning-based super-resolution and face restoration.</strong>
</p>

---

## 📌 Overview

**Face Enhancement & Image Restoration** is a Python-based image enhancement project that combines **Real-ESRGAN** and **GFPGAN** to improve the visual quality of low-resolution and degraded images.

The system uses deep learning models to upscale images, restore facial details, and produce enhanced visual outputs.

This project explores how AI-based image restoration can support applications involving low-quality images, facial image preprocessing, and computer vision workflows.

---

## ✨ Key Features

- **AI-Based Image Upscaling:** Increases image resolution using Real-ESRGAN.
- **Face Restoration:** Uses GFPGAN to restore facial details in degraded images.
- **Image Preprocessing:** Handles grayscale and BGRA images by converting them into BGR format.
- **Batch Processing:** Supports processing multiple images from an input directory.
- **Tiled Inference:** Uses tile-based processing to help manage GPU memory usage.
- **Local Execution:** Runs on a local Python environment with CPU or compatible GPU support.

---

## 🧠 Models Used

### 1. Real-ESRGAN

Real-ESRGAN is a deep learning-based image restoration model designed to improve image quality and upscale low-resolution images.

**Role in this project:**
- Upscales images by a factor of 4 using the `RealESRGAN_x4plus` model.
- Improves visual clarity and texture details.
- Supports restoration of images affected by degradation.

### 2. GFPGAN

GFPGAN is a generative facial prior-based face restoration model designed to improve the appearance of degraded facial images.

**Role in this project:**
- Restores facial details in images.
- Improves the visual quality of detected faces.
- Works alongside Real-ESRGAN through the face-enhancement pipeline.

> **Note:** AI-based restoration can generate or alter facial details. Enhanced images should not be treated as verified representations of a person's original appearance.

---

## ⚙️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Deep Learning Framework | PyTorch |
| Image Processing | OpenCV |
| Super-Resolution | Real-ESRGAN |
| Face Restoration | GFPGAN |
| Model Architecture | RRDBNet |
| Package Management | pip |
| Development Environment | Visual Studio Code |

---

## 🔄 System Workflow

```text
        Input Image
             │
             ▼
      Image Preprocessing
             │
             ▼
     Real-ESRGAN Upscaling
             │
             ▼
      Face Enhancement
          (GFPGAN)
             │
             ▼
      Enhanced Image
             │
             ▼
       Output Folder
```

---

## 📂 Project Structure

```text
Face-Enhancement/
│
├── assets/                 # Project assets
├── basicsr/                # BasicSR components
├── gfpgan/                 # GFPGAN components
├── options/                # Model configuration files
├── realesrgan/             # Real-ESRGAN components
├── scripts/                # Supporting scripts
├── tests/                  # Test files
│
├── inputs/                 # Input images
├── inputs_fixed/           # Preprocessed images
├── inputs_human/           # Selected human images
├── results/                # General output images
├── results_human/          # Enhanced human image outputs
│
├── weights/                # Model weights (not tracked by Git)
├── fix_inputs.py           # Input image preprocessing
├── inference_realesrgan.py # Image enhancement script
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup
├── LICENSE                 # Original project license
└── README.md               # Project documentation
```

---

## 💻 Installation & Setup

### Prerequisites

- Python 3.10
- Git
- pip
- Sufficient RAM and disk space
- NVIDIA GPU with compatible CUDA support for GPU acceleration (optional)

### Step 1: Clone the Repository

```bash
git clone https://github.com/vnsahil06/Face-Enhancement.git
cd Face-Enhancement
```

### Step 2: Create a Virtual Environment

```bash
python -m venv face-enhance
```

Activate it on Windows:

```cmd
face-enhance\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Install the project package if required:

```bash
python setup.py develop
```

### Step 4: Download Model Weights

Download the required pretrained model weights from the official model repositories and place them in the appropriate directories.

Expected model files:

```text
weights/
├── RealESRGAN_x4plus.pth
└── GFPGANv1.3.pth
```

The exact model paths depend on the inference configuration.

---

## 🚀 Usage

### 1. Preprocess Input Images

Run the preprocessing script to convert grayscale or BGRA images into a compatible BGR format.

```bash
python fix_inputs.py
```

### 2. Run Image Enhancement

Place the input images in `inputs_human/` and run:

```bash
python inference_realesrgan.py -n RealESRGAN_x4plus -i inputs_human -o results_human --face_enhance --tile 128
```

### Command Explanation

| Argument | Description |
|---|---|
| `-n RealESRGAN_x4plus` | Selects the Real-ESRGAN model |
| `-i inputs_human` | Input image directory |
| `-o results_human` | Output directory |
| `--face_enhance` | Enables face restoration |
| `--tile 128` | Processes images in smaller tiles to reduce memory usage |

### 3. View Results

Enhanced images are saved in:

```text
results_human/
```

---

## 📊 Applications

- Image quality enhancement
- Facial image restoration
- Low-resolution image preprocessing
- Computer vision research
- Image restoration experimentation

---

## ⚠️ Limitations

- Restoration quality depends on the input image and degradation level.
- Very low-quality images may not recover accurate facial details.
- AI enhancement may introduce artificial features or change identity-related details.
- GPU memory limitations may require smaller tile sizes.
- Visual enhancement does not guarantee improved face recognition accuracy.

---

## 🔮 Future Enhancements

- Integration with a web-based image enhancement interface.
- Real-time image enhancement support.
- Automated image quality assessment.
- Before-and-after image comparison.
- Integration with face detection and recognition pipelines.
- Evaluation of enhanced images using objective quality metrics and face recognition tests.

---

## 📚 References & Acknowledgments

This project builds upon the following open-source research and implementations:

- **Real-ESRGAN:** [GitHub Repository](https://github.com/xinntao/Real-ESRGAN)
- **GFPGAN:** [GitHub Repository](https://github.com/TencentARC/GFPGAN)
- **BasicSR:** [GitHub Repository](https://github.com/XPixelGroup/BasicSR)

The original projects and their respective authors retain credit for their work. Please refer to the original repositories for research details, licensing, and model documentation.

---

## 📄 License

This repository includes code derived from existing open-source projects.

Please refer to the included `LICENSE` file and the original repositories for applicable license terms.

---

## 👨‍💻 Author

**Sahil**

GitHub: [@vnsahil06](https://github.com/vnsahil06)

**Project:** Face Enhancement & Image Restoration