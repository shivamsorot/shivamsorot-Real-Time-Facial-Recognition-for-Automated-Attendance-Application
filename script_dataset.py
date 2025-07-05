from mtcnn import MTCNN
import cv2
import os
import numpy as np

# Initialize the MTCNN model
detector = MTCNN()

# Create the main dataset directory
dataset_dir = "dataset"
os.makedirs(dataset_dir, exist_ok=True)

def detect_face_mtcnn(image):
    """
    Detect face using MTCNN.
    Returns the bounding box of the detected face.
    """
    results = detector.detect_faces(image)
    if len(results) > 0:
        x, y, w, h = results[0]['box']
        return x, y, w, h
    return None

def capture_images():
    # Initialize webcam
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # Set width
    cam.set(4, 480)  # Set height
    
    # Ask for the user's name
    name = input("Enter the name of the person: ").strip()
    
    # Create a folder for the user inside the main dataset directory
    person_dir = os.path.join(dataset_dir, name)
    os.makedirs(person_dir, exist_ok=True)
    
    print(f"Capturing images for {name}. Look into the camera.")
    count = 0  # Image counter
    
    # Variable to store the first detected face bounding box
    first_face_box = None
    
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame. Exiting...")
            break
        
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect face using MTCNN
        if first_face_box is None:
            # Detect the first face in the initial frame
            first_face_box = detect_face_mtcnn(frame)
        
        if first_face_box:
            x, y, w, h = first_face_box
            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Crop and save the detected face in grayscale
            face = gray_frame[y:y+h, x:x+w]
            
            # Increment image counter
            count += 1
            
            # Save the captured image in the person's directory
            img_path = os.path.join(person_dir, f"{name}_{count}.jpg")
            cv2.imwrite(img_path, cv2.resize(face, (224, 224)))  # Resize to a standard size
            
            # Show the frame with the detected face
            cv2.imshow('Capturing Images', frame)
        
        # Break the loop if 50 images are captured
        if count >= 50:
            print(f"Successfully captured 50 images for {name}.")
            break
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting the process.")
            break
    
    # Release resources
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images()