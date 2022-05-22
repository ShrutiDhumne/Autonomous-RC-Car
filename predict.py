from convert_data_to_array import conv_image_to_array_pred
def predict(model,img):
    x = conv_image_to_array_pred(img)
    y_new = model.predict(x)
    return y_new
