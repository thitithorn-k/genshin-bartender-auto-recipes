import imutils as imutils
import cv2
import function.recipe as recipe
import function.game_screen as game_screen

drink_name_images = []


for i in range(21):
    img = cv2.imread(f'resources/drinks/{i}.png')
    drink_name_images.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))


def match_drink_id(img):
    try:
        most_match = 0
        most_match_drink_id = 0
        for drink_index, drink_image in enumerate(drink_name_images):
            res = cv2.matchTemplate(img, drink_image, cv2.TM_CCOEFF_NORMED)
            max_res = cv2.minMaxLoc(res)[1]
            if max_res > most_match:
                most_match = max_res
                most_match_drink_id = drink_index
        # print(most_match, most_match_drink_id)
        if most_match < 0.6:
            return -1
        return most_match_drink_id
    except:
        return -1


def cut_order(screen_img):
    try:
        # img = cv2.imread('genshin_bartender/08.png')
        img_gray = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)
        img720 = imutils.resize(img_gray, width=1280)
        order_img_gray = img720[130:130 + 400, 130:130 + 280]
        _, order_img_thresh = cv2.threshold(order_img_gray, 210, 255, cv2.THRESH_BINARY)
        order_img_contours, _ = cv2.findContours(order_img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        c = max(order_img_contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        order_img_crop = order_img_gray[y:y + h, x:x + w]
        _, order_img_crop_thresh = cv2.threshold(order_img_crop, 190, 255, cv2.THRESH_BINARY)
        order_img_thresh_crop_border = cv2.copyMakeBorder(order_img_crop_thresh, 10, 10, 100, 100, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        # cv2.imshow('test11', order_img_thresh_crop_border)
        return order_img_thresh_crop_border
    except:
        return -1


def get_recipe():
    game_screen_img = game_screen.get_screen()
    order_image = cut_order(game_screen_img)
    return recipe.get_recipe(match_drink_id(order_image))
