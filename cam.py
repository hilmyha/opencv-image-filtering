import cv2

# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 0
cam = cv2.VideoCapture(cam_port)
cv2.namedWindow("CAM")

img_counter = 0

while True:
    # reading the input using the camera
    result, image = cam.read()
    if not result:
        print("failed to grab image")
        break
    # show the image
    cv2.imshow("CAM", image)

    k = cv2.waitKey(1)
    if k%256 == 27:
      # If
        # ESC pressed
        # Close the CAM window
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
      # Else If
        # SPACE pressed
        # Capture image to local file
        img_path = "UTS/image/"
        img_name = "captured_img.png".format(img_counter)

        # save the image
        cv2.imwrite(img_path + img_name, image)
        print("{} saved!".format(img_name))
        # img_counter += 1

cam.release()

cv2.destroyAllWindows()