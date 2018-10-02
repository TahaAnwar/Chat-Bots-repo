
#real time detection with sift  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


import numpy as np
import cv2
img = cv2.imread("thecropp.jpg", 0) # queryiamge
 
cap = cv2.VideoCapture(0)
 
# Features
sift = cv2.xfeatures2d.SIFT_create()
#surf = cv2.xfeatures2d.SURF_create(1000)
kp_image, desc_image = sift.detectAndCompute(img, None)
 
# Feature matching
index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)
 
while True:
    _, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # trainimage
 
    kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)
    matches = flann.knnMatch(desc_image, desc_grayframe, k=2)
 
    good_points = []
    for m, n in matches:
        if m.distance <0.6* n.distance:
            good_points.append(m) 
 
    # Homography
    if len(good_points) > 10:
        query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
 
        matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
 
        # Perspective transform
        h, w = img.shape
        pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, matrix)
 
        homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)
 
        cv2.imshow("Homography", homography)
       # print(len(good_points))
    else:
        cv2.imshow("Homography", frame)
       # print(len(good_points))
 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
 
 
cap.release()
cv2.destroyAllWindows()









#Real Time Object Detection And Tracking with Orb xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



import numpy as np
import cv2 as cv
img = cv2.imread("thecropp.jpg", 0)          # queryImage

cap = cv2.VideoCapture(0)
 
# Features

kp_image, desc_image = sift.detectAndCompute(img, None)
 
# Initiate ORB detector
orb = cv.ORB_create(4000)
# find the keypoints and descriptors with SIFT
kp_image, desc_image = orb.detectAndCompute(img, None)

# FLANN parameters
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6,  
                   key_size = 12,   
                   multi_probe_level = 1)
search_params = dict(checks=50)   # or pass empty dictionary like this: dict() or {}
flann = cv.FlannBasedMatcher(index_params,search_params)

while True:
    _, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # trainimage
 
    kp_grayframe, desc_grayframe = orb.detectAndCompute(grayframe, None)
    matches = flann.knnMatch(desc_image, desc_grayframe, k=2)
    try:
        good_points = []
        for m, n in matches:
            if m.distance <0.6* n.distance:
                good_points.append(m) 

        # Homography
        if len(good_points) > 10:
            query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
            train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)

            matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
            matches_mask = mask.ravel().tolist()

            # Perspective transform
            h, w = img.shape
            pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
            dst = cv2.perspectiveTransform(pts, matrix)

            homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)

            cv2.imshow("Homography", homography)
            #print(len(good_points))
        else:
            cv2.imshow("Homography", frame)
            #print(len(good_points))
    except:
        cv2.imshow("Homography", frame)
        
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
