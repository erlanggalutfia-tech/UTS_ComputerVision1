import cv2
import numpy as np

# Buat kanvas dan gambar stickman
canvas = np.zeros((400, 400, 3), dtype=np.uint8)
white = (255, 255, 255)

cv2.circle(canvas, (200, 100), 30, white, 2)
cv2.line(canvas, (200, 130), (200, 250), white, 2)
cv2.line(canvas, (200, 160), (150, 200), white, 2)
cv2.line(canvas, (200, 160), (250, 200), white, 2)
cv2.line(canvas, (200, 250), (160, 320), white, 2)
cv2.line(canvas, (200, 250), (240, 320), white, 2)
cv2.putText(canvas, "Stickman Gor", (120, 370),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2, cv2.LINE_AA)

# === Resize (ubah ukuran) ===
resized = cv2.resize(canvas, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite("stickman_resize.png", resized)

# === Crop (potong sebagian gambar) ===
# Ambil bagian tengah dari gambar asli
cropped = canvas[80:300, 100:300]
cv2.imwrite("stickman_crop.png", cropped)

print("Hasil resize disimpan sebagai stickman_resize.png")
print("Hasil crop disimpan sebagai stickman_crop.png")
