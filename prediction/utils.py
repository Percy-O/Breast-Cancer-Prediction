import mxnet as mx
from mxnet.gluon import nn
import numpy as np
import cv2

class CNN(nn.Block):
    def __init__(self, **kwargs):
        super(CNN, self).__init__(**kwargs)
        with self.name_scope():
            self.conv1 = nn.Conv2D(channels=32, kernel_size=3, activation='relu')
            self.pool1 = nn.MaxPool2D(pool_size=2, strides=2)
            self.conv2 = nn.Conv2D(channels=64, kernel_size=3, activation='relu')
            self.pool2 = nn.MaxPool2D(pool_size=2, strides=2)
            self.flatten = nn.Flatten()
            self.fc1 = nn.Dense(128, activation='relu')
            self.dropout = nn.Dropout(0.5)
            self.fc2 = nn.Dense(2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# Load the model parameters
ctx = mx.gpu() if mx.context.num_gpus() else mx.cpu()
net = CNN()
net.load_parameters('prediction/breast_model.params', ctx=ctx)

def predict(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (50, 50))
    img = img.astype('float32') / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)
    img = mx.nd.array(img).as_in_context(ctx)
    
    output = net(img)
    prediction = mx.nd.argmax(output, axis=1)
    return int(prediction.asscalar())
