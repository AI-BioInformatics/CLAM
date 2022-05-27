import copy
import time
import torch
import torch.nn as nn
import torchvision.models as models
from torchsummary import summary

def run():
    model_ft = models.vgg16(pretrained=True)
    a = [ 224, 224, 3]
    input = torch.IntTensor(a).cuda()
    summary(model_ft.cuda(), (3, 224, 224))

    params = model_ft.named_parameters()
    for name, param in model_ft.named_parameters():             #17-30
        if int(name.split(".")[1]) >=17 and int(name.split(".")[1]) <= 30:

            print(name)

    # set_parameter_requires_grad(model_ft, feature_extract)
    # num_ftrs = model_ft.classifier[6].in_features
    # model_ft.classifier[6] = nn.Linear(num_ftrs, num_classes)
    # input_size = 224

if __name__ == '__main__':
    run()