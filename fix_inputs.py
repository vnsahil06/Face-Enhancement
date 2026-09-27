import cv2
import os

input_dir = "inputs"
output_dir = "inputs_fixed"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)

    if not filename.lower().endswith(
        (".png", ".jpg", ".jpeg", ".bmp", ".webp")
    ):
        continue

    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)

    if img is None:
        print("Skipped:", filename)
        continue

    # Convert grayscale to 3-channel BGR
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # Convert BGRA to BGR
    elif len(img.shape) == 3 and img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, img)

    print("Fixed:", filename)

print("All images are ready.")