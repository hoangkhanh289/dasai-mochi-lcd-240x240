from PIL import Image
import os


def process_image(input_file, output_folder, step_degree, total_images, crop_size=240):
    os.makedirs(output_folder, exist_ok=True)

    img = Image.open(input_file).convert("RGB")
    w, h = img.size

    for i in range(total_images):
        angle = i * step_degree
        rotated = img.rotate(angle, resample=Image.BICUBIC, expand=True)

        rw, rh = rotated.size
        rleft = (rw - crop_size) // 2
        rtop = (rh - crop_size) // 2
        rright = rleft + crop_size
        rbottom = rtop + crop_size
        cropped = rotated.crop((rleft, rtop, rright, rbottom))

        output_path = os.path.join(output_folder, f"frame_{i:03d}.jpg")
        cropped.save(output_path, format="JPEG", quality=95)

    print(f"Đã tạo {total_images} ảnh trong thư mục '{output_folder}'.")


# Cấu hình
process_image(
    "E:/tool/SD/analog_mode/mode_3/Untitled2.png",
    "E:/tool/SD/analog_mode/mode_3/hour",
    -0.5,
    720,
)
process_image(
    "E:/tool/SD/analog_mode/mode_3/Untitled.png",
    "E:/tool/SD/analog_mode/mode_3/minute",
    -6,
    60,
)
