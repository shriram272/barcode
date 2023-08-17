# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode
# from ultralytics import YOLO
#
# # Load YOLO model using your custom module or library
# model = YOLO('../Yolo-Weights/yolov8n.pt')
#
# # Function to apply LSD on an ROI
# def apply_lsd_on_roi(roi, min_line_length, max_line_length, max_line_gap):
#     # Convert the ROI to grayscale
#     gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#     line = cv2.Canny(gray_roi, 460, 700)
#
#     # Apply the LSD algorithm to detect lines in the ROI
#     lines = cv2.createLineSegmentDetector().detect(line)
#
#     # Draw the detected lines on the ROI
#     for line in lines[0]:
#         x1, y1, x2, y2 = map(int, line[0])
#         # Calculate the length of the line segment
#         length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#         # Draw the line only if its length is within the specified range
#         if min_line_length <= length <= max_line_length:
#             cv2.line(roi, (x1, y1), (x2, y2), (0, 255, 0), 1)
#
#     return roi, [(x1, y1, x2, y2) for line in lines[0]]
#
# # Function to check if a line is close to multiple lines
# def is_line_close_to_multiple(line, other_lines, max_distance, min_close_lines):
#     close_count = 0
#     for other_line in other_lines:
#         if are_lines_close(line, other_line, max_distance):
#             close_count += 1
#             if close_count >= min_close_lines:
#                 return True
#     return False
#
# # Function to check if two lines are close within a given distance
# def are_lines_close(line1, line2, max_distance):
#     x1_1, y1_1, x2_1, y2_1 = map(int, line1)
#     x1_2, y1_2, x2_2, y2_2 = map(int, line2)
#     dist_1 = np.sqrt((x2_1 - x1_2)**2 + (y2_1 - y1_2)**2)
#     dist_2 = np.sqrt((x2_2 - x1_1)**2 + (y2_2 - y1_1)**2)
#     return dist_1 <= max_distance or dist_2 <= max_distance
#
# # Load the image using OpenCV
# image_path = '../all_barcode/IMG_20220303_174744.jpg'
# image = cv2.imread(image_path)
#
# cv2.imshow("input image", image)
#
# # Perform object detection using YOLO
# results = model(image_path, conf=0.05)
# min_line_length = 45
# max_line_length = 55
# max_line_gap = 15
# # Maximum gap between lines to be considered as parallel
# max_distance = 25  # Maximum distance to consider lines as close
# min_close_lines = 5  # Minimum number of lines to be close
#
# # Create an image with YOLO-detected objects and black bounding boxes
# yolo_detected_image = image.copy()
# for r in results:
#     boxes = r.boxes
#     for box in boxes:
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         cv2.rectangle(yolo_detected_image, (x1, y1), (x2, y2), (0, 0, 0), 3)
#
# # Set to keep track of decoded barcodes
# decoded_barcodes = set()
#
# # Iterate over the detected objects
# for r in results:
#     boxes = r.boxes
#     for box in boxes:
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#
#         # Extract the ROI from the bounding box
#         roi = image[y1:y2, x1:x2]
#
#         # Apply Pyzbar to the ROI for barcode detection
#         barcodes = decode(roi)
#         for barcode in barcodes:
#             barcode_data = barcode.data.decode('utf-8')
#             if barcode_data not in decoded_barcodes:
#                 print("Detected Barcode:", barcode_data)
#                 decoded_barcodes.add(barcode_data)
#
#             # Draw a red bounding box around the detected barcode
#             barcode_rect = barcode.rect
#             cv2.rectangle(roi, (barcode_rect.left, barcode_rect.top), (barcode_rect.left + barcode_rect.width, barcode_rect.top + barcode_rect.height), (255, 0, 0), 2)
#             roi_with_lines, lines = apply_lsd_on_roi(roi, min_line_length, max_line_length, max_line_gap)
#
#             # Draw green bounding boxes around lines that are close to 3 or more lines
#             for i, line in enumerate(lines):
#                 if is_line_close_to_multiple(line, lines[:i] + lines[i + 1:], max_distance, min_close_lines):
#                     x1, y1, x2, y2 = map(int, line)
#                     cv2.rectangle(roi_with_lines, (x1 - 75, y1 - 75), (x2 + 95, y2 + 95), (0, 255, 255), 2)
#         # Apply LSD to detect lines in the ROI with the specified length range
#         # ...
#
#         # Draw green bounding boxes around lines that are close to 3 or more lines
#         # ...
#
#         # Rotate the ROI by 5 degrees until it reaches the original orientation
#         for angle in range(0, 360, 5):
#             rotated_roi = cv2.warpAffine(roi, cv2.getRotationMatrix2D((roi.shape[1] / 2, roi.shape[0] / 2), angle, 1), (roi.shape[1], roi.shape[0]))
#
#             # Apply Pyzbar to the rotated ROI for barcode detection
#             rotated_barcodes = decode(rotated_roi)
#             for barcode in rotated_barcodes:
#                 barcode_data = barcode.data.decode('utf-8')
#                 if barcode_data not in decoded_barcodes:
#                     print("Detected Barcode (Rotated):", barcode_data)
#                     decoded_barcodes.add(barcode_data)
#
# # Display the image with YOLO-detected bounding boxes (black)
# res = cv2.resize(yolo_detected_image, (1300, 1080))
# cv2.imshow("YOLO Detected Objects", res)
# cv2.waitKey(0)
#
# # Display the final image with all bounding boxes and detections
# re = cv2.resize(image, (1300, 1080))
# cv2.imshow("Image with Bounding Boxes", re  )
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
from pyzbar.pyzbar import decode
from ultralytics import YOLO


import cv2
import numpy as np
from pyzbar.pyzbar import decode
from ultralytics import YOLO

# Load YOLO model using your custom module or library
model = YOLO('../Yolo-Weights/yolov8n.pt')

#Function to apply LSD on an ROI
def apply_lsd_on_roi(roi, min_line_length, max_line_length, max_line_gap):
    # Convert the ROI to grayscale
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    line = cv2.Canny(gray_roi, 470, 700)

    # Apply the LSD algorithm to detect lines in the ROI
    lines = cv2.createLineSegmentDetector().detect(line)
    # Draw the detected lines on the ROI
    for line in lines[0]:
        x1, y1, x2, y2 = map(int, line[0])
        # Calculate the length of the line segment
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        # Draw the line only if its length is within the specified range
        if min_line_length <= length <= max_line_length:
            cv2.line(roi, (x1, y1), (x2, y2), (0, 255, 0), 1)

    return roi, [(x1, y1, x2, y2) for line in lines[0]]


# Function to check if a line is close to multiple lines
def is_line_close_to_multiple(line, other_lines, max_distance, min_close_lines):
    close_count = 0
    for other_line in other_lines:
        if are_lines_close(line, other_line, max_distance):
            close_count += 1
            if close_count >= min_close_lines:
                return True
    return False

# Function to check if two lines are close within a given distance
def are_lines_close(line1, line2, max_distance):
    x1_1, y1_1, x2_1, y2_1 = map(int, line1)
    x1_2, y1_2, x2_2, y2_2 = map(int, line2)
    dist_1 = np.sqrt((x2_1 - x1_2)**2 + (y2_1 - y1_2)**2)
    dist_2 = np.sqrt((x2_2 - x1_1)**2 + (y2_2 - y1_1)**2)
    return dist_1 <= max_distance or dist_2 <= max_distance

# Load the image using OpenCV
image_path = '../all_barcode/IMG_20220303_175451.jpg'
image = cv2.imread(image_path)

# Perform object detection using YOLO
results = model(image_path, conf=0.05)
min_line_length = 45
max_line_length = 55
max_line_gap = 15
max_distance = 25  # Maximum distance to consider lines as close
min_close_lines = 5  # Minimum number of lines to be close

# Create an image with YOLO-detected objects and black bounding boxes
yolo_detected_image = image.copy()
for r in results:
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(yolo_detected_image, (x1, y1), (x2, y2), (0, 0, 0), 3)

# Set to keep track of decoded barcodes
decoded_barcodes = set()

# Iterate over the detected objects
for r in results:
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Extract the ROI from the bounding box
        roi = image[y1:y2, x1:x2]

        # Apply Pyzbar to the ROI for barcode detection
        barcodes = decode(roi)
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            if barcode_data not in decoded_barcodes:
                print("Detected Barcode:", barcode_data)
                decoded_barcodes.add(barcode_data)

                # Draw a blue bounding box around the detected barcode
                barcode_rect = barcode.rect
                cv2.rectangle(image, (x1 + barcode_rect.left, y1 + barcode_rect.top),
                              (x1 + barcode_rect.left + barcode_rect.width, y1 + barcode_rect.top + barcode_rect.height), (255, 0, 0), 2)

        # Apply LSD to detect lines in the ROI with the specified length range
        roi_with_lines, lines = apply_lsd_on_roi(roi, min_line_length, max_line_length, max_line_gap)

        # Draw green bounding boxes around lines that are close to 3 or more lines
        for i, line in enumerate(lines):
            if is_line_close_to_multiple(line, lines[:i] + lines[i + 1:], max_distance, min_close_lines):
                x1, y1, x2, y2 = map(int, line)
                cv2.rectangle(roi_with_lines, (x1 - 75, y1 - 75), (x2 + 95, y2 + 95), (0, 255, 255), 2)

        # Rotate the ROI by 5 degrees until it reaches the original orientation
        for angle in range(0, 360, 5):
            rotated_roi = cv2.warpAffine(roi, cv2.getRotationMatrix2D((roi.shape[1] / 2, roi.shape[0] / 2), angle, 1), (roi.shape[1], roi.shape[0]))

            # Apply Pyzbar to the rotated ROI for barcode detection
            rotated_barcodes = decode(rotated_roi)
            for barcode in rotated_barcodes:
                barcode_data = barcode.data.decode('utf-8')
                if barcode_data not in decoded_barcodes:
                    print("Detected Barcode (Rotated):", barcode_data)
                    decoded_barcodes.add(barcode_data)

                    # Draw a blue bounding box around the detected barcode
                    rotated_barcode_rect = barcode.rect
                    cv2.rectangle(rotated_roi, (rotated_barcode_rect.left, rotated_barcode_rect.top),
                                  (rotated_barcode_rect.left + rotated_barcode_rect.width, rotated_barcode_rect.top + rotated_barcode_rect.height), (255, 0, 0), 2)

            # Apply LSD to detect lines in the rotated ROI with the specified length range
            rotated_roi_with_lines, rotated_lines = apply_lsd_on_roi(rotated_roi, min_line_length, max_line_length, max_line_gap)

            # Draw yellow bounding boxes around lines that are close to 3 or more lines
            for i, rotated_line in enumerate(rotated_lines):
                if is_line_close_to_multiple(rotated_line, rotated_lines[:i] + rotated_lines[i + 1:], max_distance, min_close_lines):
                    x1, y1, x2, y2 = map(int, rotated_line)
                    cv2.rectangle(rotated_roi_with_lines, (x1 - 50, y1 - 50), (x2 + 75, y2 + 75), (0, 255, 255), 2)

# Display the image with YOLO-detected bounding boxes (black)
res = cv2.resize(yolo_detected_image, (1300, 1080))
cv2.imshow("YOLO Detected Objects", res)

# Display the final image with all bounding boxes and detections
re = cv2.resize(image, (1300, 1080))
cv2.imshow("Image with Bounding Boxes", re)
cv2.waitKey(0)
cv2.destroyAllWindows()
