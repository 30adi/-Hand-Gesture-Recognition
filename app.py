from flask import Flask, render_template, Response
import cv2
import cv2
import numpy as np
print('k')
def nothing(x):
    pass

image_x, image_y = 64,64

from tensorflow.keras.models import load_model
clas = load_model('Trained_model.h5')

##cv2.namedWindow("Trackbars")
##
##cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
##cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
##cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
##cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
##cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
##cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

#cv2.namedWindow("test")

img_counter = 0

img_text = ''
app = Flask(__name__)
print('k')
camera = cv2.VideoCapture(0)  # use 0 for web camera


def gen_frames():  # generate frame by frame from camera
    img_text = ''
    from tensorflow.keras.models import load_model
    clas = load_model('Trained_model.h5')
    def predictor():
       import numpy as np
       from tensorflow.keras.preprocessing import image
       


       test_image = image.load_img('1.png', target_size=(64, 64))
       test_image = image.img_to_array(test_image)
       test_image = np.expand_dims(test_image, axis = 0)
       #print(classifier)
       
       result = clas.predict(test_image)
       
       if result[0][0] == 1:
              return 'A'
       elif result[0][1] == 1:
              return 'B'
       elif result[0][2] == 1:
              return 'C'
       elif result[0][3] == 1:
              return 'D'
       elif result[0][4] == 1:
              return 'E'
       elif result[0][5] == 1:
              return 'F'
       elif result[0][6] == 1:
              return 'G'
       elif result[0][7] == 1:
              return 'H'
       elif result[0][8] == 1:
              return 'I'
       elif result[0][9] == 1:
              return 'J'
       elif result[0][10] == 1:
              return 'K'
       elif result[0][11] == 1:
              return 'L'
       elif result[0][12] == 1:
              return 'M'
       elif result[0][13] == 1:
              return 'N'
       elif result[0][14] == 1:
              return 'O'
       elif result[0][15] == 1:
              return 'P'
       elif result[0][16] == 1:
              return 'Q'
       elif result[0][17] == 1:
              return 'R'
       elif result[0][18] == 1:
              return 'S'
       elif result[0][19] == 1:
              return 'T'
       elif result[0][20] == 1:
              return 'U'
       elif result[0][21] == 1:
              return 'V'
       elif result[0][22] == 1:
              return 'W'
       elif result[0][23] == 1:
              return 'X'
       elif result[0][24] == 1:
              return 'Y'
       elif result[0][25] == 1:
              return 'Z'
       


    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        
        #print('k')
        frame = cv2.flip(frame,1)
##        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
##        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
##        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
##        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
##        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
##        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        img = cv2.rectangle(frame, (425,100),(625,300), (0,255,0), thickness=2, lineType=8, shift=0)

        lower_blue = np.array([0,10,60])
        upper_blue = np.array([20,150,255])
        imcrop = img[102:298, 427:623]
        hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        cv2.putText(frame, img_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
        #cv2.imshow("test", frame)
        cv2.imshow("mask", mask)
        
        #if cv2.waitKey(1) == ord('c'):
        #print('kk')
        img_name = "1.png"
        save_img = cv2.resize(mask, (image_x, image_y))
        cv2.imwrite(img_name, save_img)
        #print("{} written!".format(img_name))
        img_text = predictor()
        ret, buffer = cv2.imencode('.jpg', frame)
        
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        if cv2.waitKey(1) == 27:
            break

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
