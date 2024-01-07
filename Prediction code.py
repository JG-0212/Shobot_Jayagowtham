import os
from roboflow import Roboflow
rf = Roboflow(api_key="OGCV1pPJDtCRgU2K1s3r")
project = rf.workspace().project("jg-intern")
model = project.version(2).model

root = os.getcwd()
our_path = "Random testing"
req = os.path.join(root,our_path)
i=0
for file in os.listdir(req):
    pa=os.path.join(req,file)
    model.predict(pa, confidence=40, overlap=30).save("prediction"+str(i)+".jpg")
    #print(file)
    i=i+1
# infer on a local image


# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())