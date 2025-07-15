import cv2 as cv

def callback_2(event,x,y,flags,params):
    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),2,(0,255,0),-1,cv.LINE_AA)
        font = cv.FONT_HERSHEY_COMPLEX
        cv.putText(img,f'({x},{y})',(x,y),font,0.5,(0,255,0),1,cv.LINE_AA)
        cv.imshow('image',img)
        rect_coord2.append((x,y))
        if len(rect_coord2) >= 2:
            cv.rectangle(img,rect_coord2[0],rect_coord2[1],(255,0,0),1,cv.LINE_AA)
            cv.imshow('image',img)
            x_sl = rect_coord2[0][0]-rect_coord2[1][0]
            y_sl = rect_coord2[0][1]-rect_coord2[1][1]
            print(x_sl)
            print(y_sl)
            sl_ice = img[rect_coord2[0][1]:rect_coord2[1][1],rect_coord2[0][0]:rect_coord2[1][0]]
            # print(sl_ice)
            cv.imwrite('outputimg.jpg',sl_ice)
            rect_coord2.clear()

if __name__ == "__main__":
    img = cv.imread('len_top.jpg')
    cv.imshow('image',img)
    rect_coord2 = []
    cv.setMouseCallback('image',callback_2)
    cv.waitKey(0)
    cv.destroyAllWindows()