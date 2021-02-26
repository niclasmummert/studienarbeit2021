import json
import os

import requests
from PIL import Image
from torch import tensor
from torchvision import transforms


def preprocess(image_file):
    """Preprocess the input image."""
    data_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    if image_file.endswith(".jpg") or image_file.endswith(".JPG"):
        image = Image.open(image_file)
    else:
        image = Image.open(image_file).convert('RGB')
    image = data_transforms(image).float()
    image = tensor(image)
    image = image.unsqueeze(0)
    return image.numpy()

def ml_prediction(image_file):
    input_data = preprocess(image_file)
    input_data = json.dumps({'data': input_data.tolist()})
    scoringUri = "http://b0a60722-39fc-4c04-8707-d5b538ce516e.westeurope.azurecontainer.io/score"
    headers = {"Content-Type": "application/json"}
    resp = requests.post(scoringUri, input_data, headers = headers)
    print(resp.text)
    ret = ""
    if resp.text.__contains__("dirt"):
        ret = "dirtroad"
    elif resp.text.__contains__("stone"):
        ret = "stonepath"
    else:
        ret = "tarmac"
    return ret

# def main():
#     folder = r"C:/Users/nicla/Desktop/stdarbeit/images1"
#     png_files = [folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f]
#     img_iterator = 5
#     out = ml_prediction(png_files[img_iterator])
#     outstring = "Predicted Surface is: " + out
#     print(outstring)

# if __name__ == "__main__":
#     main()
