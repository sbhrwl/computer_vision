# Computer Vision

- [CNN Basics](https://github.com/sbhrwl/computer_vision/blob/main/docs/CNN_basics.md)
- [Networks](https://github.com/sbhrwl/computer_vision/blob/main/docs/Networks.md)
- [Tasks](#tasks)
- [Pytorch](#pytorch)
- [Creating own python package](#creating-own-python-package)
- [Deployment](#deployment)
- [Augmentation](#augmentation)
- [Object Detection](#object-detection)
- [Image Segmentation](#image-segmentation)
- [Feature Store](#feature-store)
- [References](#references)

## Tasks
- [General Approach](#general-approach)
- [Task 1 Basic CNN architectures for MNIST datatset](#task-1-basic-cnn-architectures-for-mnist-datatset)
- [Task 2 Basic CNN architectures for CIFAR10 datatset](#task-2-basic-cnn-architectures-for-cifar10-datatset)
- [Task 3 Basic CNN architectures for Flower datatset](#task-3-basic-cnn-architectures-for-flower-datatset)
- [Task 4 Basic Image Classifier](#task-4-basic-image-classifier)
- [Task 5 Convnet architectures for MNIST datatset](#task-5-convnet-architectures-for-mnist-datatset)
- [Task 6 VGG architectures for CIFAR10 datatset](#task-6-vgg-architectures-for-cifar10-datatset)
- [Task 7 Inception architectures for CIFAR10 datatset](#task-7-inception-architectures-for-cifar10-datatset)
- [Task 8 Resnet architectures for CIFAR10 datatset](#task-8-resnet-architectures-for-cifar10-datatset)
- [Task 9 DenseNet architectures for CIFAR10 datatset](#task-9-densenet-architectures-for-cifar10-datatset)
- [Task 10 EfficientNet architectures for CIFAR10 datatset](#task-10-efficientnet-architectures-for-cifar10-datatset)

## General Approach
### [Step 1: Data Preparation](https://github.com/sbhrwl/computer_vision/blob/main/src/core/data_preparation.py)
  - Load dataset
  - Split dataset to create Train, Validation and Test sets
  - Preprocess features
    - Rescale features to have values within 0 - 1 range, ex: [0,255] --> [0,1]
      ```
      X_train = train_features.astype('float32') / 255
      X_test = test_features.astype('float32') / 255
      ```
  - Preprocess labels
    - One Hot Encode Labels
      ```
      y_train = np_utils.to_categorical(train_labels, num_classes)
      y_test = np_utils.to_categorical(test_labels, num_classes)
      ```
  - Reshape features
    ```
    # Monochrome image with 1 Channel
    # width * height * channel: 28 * 28 * 1
    # input image dimensions 28x28 pixel images.

    img_rows, img_cols = 28, 28

    X_train = train_features.reshape(train_features.shape[0], img_rows, img_cols, 1)
    X_test = test_features.reshape(test_features.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)
    ```
  - [Parameters yaml](https://github.com/sbhrwl/computer_vision/blob/main/parameters.yaml): Configuring training parameters
    - Configure data set: 
      ```
      dataset: cifar10_original  # mnist cifar10_original cifar10_resize cifar100 custom_dataset
      ```
### [Step 2: Build Model Architectures](https://github.com/sbhrwl/computer_vision/tree/main/src/networks)
Refer **hyperlink** for each task heading to get information about underlying network architecture used for performing the task.
  
### [Step 3: Model Training](https://github.com/sbhrwl/computer_vision/blob/main/src/training.py)
  - Compile the model
  - Setup Callbacks
    - Early Stopping call back
    - Check pointer call back to save best found weights
  - Start Training
    ```
    history = model.fit(X_train, y_train,
                      batch_size=32,
                      epochs=1,
                      validation_data=(X_validation, y_validation),
                      callbacks=[early_stopping_cb, check_pointer],
                      verbose=2,
                      shuffle=True)
    ```
  - [Parameters yaml](https://github.com/sbhrwl/computer_vision/blob/main/parameters.yaml): Configuring training parameters
    - Configure Model to train on:
      ```
      model: dense_net_transfer_learning
      ```
  - **Training times** are on a Computer with 16GB RAM and 2 cores and 4 Logical processors

## [Task 1 Basic CNN architectures for MNIST datatset](https://github.com/sbhrwl/computer_vision/blob/main/src/cnn_starters/mnist/model_architectures.py)
  | Model | kernel size | Padding | Parameters | Epochs | Batch size | Accuracy | Training time |
  | ----- | ----------- | --------| -----------| ------ | ---------- | -------- | ------------- |
  | 1conv_1max_pool | 3x3 | same | 402,442 | 1 | 32 | 97.82% | 25 sec |
  | 2conv_1max_pool | 3x3 | same | 822,346 | 1 | 32 | 98.08% | 2 min 6 sec |
  | 3conv_1max_pool | 3x3 | same | 1,699,018 | 1 | 32 | 98.60% | 6 min 56 sec |
  | 1conv_1max_pool_dropout | 3x3 | same | 201,498 | 1 | 32 | 96.06% | 17 sec |
  | alternate_1conv_1max_pool | 3x3 | same | 220,234 | 1 | 32 | 98.10% | 44 sec |

## [Task 2 Basic CNN architectures for CIFAR10 datatset](https://github.com/sbhrwl/computer_vision/blob/main/src/cnn_starters/cifar10/model_architectures.py)
  | Model | kernel size | Padding | Parameters | Epochs | Batch size | Accuracy | Training time |
  | ----- | ----------- | --------| -----------| ------ | ---------- | -------- | ------------- |
  | 1conv_1max_pool | 3x3 | same | 525,898 | 1 | 32 | 54.08% | 32 sec |
  | 2conv_1max_pool | 3x3 | same | 1,068,682 | 1 | 32 | 60.42% | 2 min 9 sec |
  | 3conv_1max_pool | 3x3 | same | 2,258,958 | 1 | 32 | 65.42% | 7 min 48 sec |
  | 1conv_1max_pool_dropout | 3x3 | same | 263,066 | 1 | 32 | 46.30% | 20 sec |
  | alternate_1conv_1max_pool | 3x3 | same | 282,250 | 1 | 32 | 50.64% | 56 sec |

## [Task 3 Basic CNN architectures for Flower datatset](https://colab.research.google.com/drive/1bxCs_T6PbcKh7v9FccGUEBj_rOjh861C?usp=sharing)
  | Model | kernel size | Padding | Parameters | Epochs | Accuracy | Training time |
  | ----- | ----------- | ------- | ---------- | ------ | -------- | ------------- |
  | Alternate 3 conv and Max pool |  3x3 | same | 2,534,885 | 10 | 58.75% | 20 mins |
  | Data Augmentation with Rotation, Flipping and Zoom  |  3x3 | same | 4,032,101 | 10 | 66.16% | 30 mins |
  ```
  data_augmentation=Sequential([
    layers.experimental.preprocessing.RandomFlip('horizontal',input_shape=(180,180,3)),
    layers.experimental.preprocessing.RandomFlip('vertical',input_shape=(180,180,3)),
    layers.experimental.preprocessing.RandomZoom(0.3),
    layers.experimental.preprocessing.RandomRotation(0.4)
  ])
  ```
  
## [Task 4 Basic Image Classifier](https://github.com/sbhrwl/computer_vision/blob/main/src/cnn_starters/custom_classifier/model_architectures.py)
  | Model | kernel size | Padding | Parameters | Epochs | Accuracy | Training time |
  | ----- | ----------- | ------- | ---------- | ------ | -------- | ------------- |
  | Alternate 3 conv and Max pool |  3x3 | same | 646,273 | 1 | 50.00% | 13 sec |

## [Task 5 Convnet architectures for MNIST datatset](https://github.com/sbhrwl/computer_vision/blob/main/src/networks/convnet_mnist_architectures.py)
  | Changes to Existing Model | Parameters | Epochs | Batch size | Accuracy | Training time |
  | ------------------------- | ---------- | -------| ---------- | -------- | ------------- |
  | Original | 11,450 | 1 | 128 | 86.65% | 1 min 39 sec |
  | Replaced 16 channels with 8 in the Conv layers | 6,340 | 1 | 128 | 93.72% | 1 min 26 sec |
  | Added a Max pool layer after image dimensions has been reduced to 8 | 8,298 | 1 | 128 | 95.88% | 1 min 33 sec |
  | Added a 1x1 to reduce dimension from 16 to 10 | 6,332 | 1 | 128 | 95.45% | 1 min 21 sec |
  | Added a 1x1 to reduce dimension from 16 to 10 | 6,332 | 2 | 128 | 98.14% | 2 min 20 sec |
  
## [Task 6 VGG architectures for CIFAR10 datatset](https://github.com/sbhrwl/computer_vision/blob/main/src/networks/vgg_architectures.py)
Read comments mentioned under "Usage" in the vgg_model_training.py

  | VGG Model | Parameters | Epochs | Batch size | Accuracy | Training time |
  | --------- | ---------- | -------| -----------| ---------| ------------- |
  | Transfer Learning Custom Dataset | 50,178 out of 14,719,818 | 1 | 1000 | 53.08% | 7 mins 6 sec |
  | Transfer Learning CIFAR10 Dataset | 5,130 out of 14,719,818 | 1 | 1000 | 11.68% | 6 mins 51 sec |
  | VGG 16 scratch CIFAR10 Dataset | 33,638,218 | 1 | 1000 | 10.5% | 58 mins |
  | VGG 19 scratch CIFAR10 Dataset | 38,947,914 | 1 | 1000 |  10% | 1 hour 17 mins |  
  - Training on CIFAR10 with image size 224x224 gives below message and then process terminates
    ```
    W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 12845056000 exceeds 10% of free system memory.
    ```
  
## [Task 7 Inception architectures for CIFAR10 datatset](https://github.com/sbhrwl/computer_vision/blob/main/src/networks/inception_architectures_tf.py)
  | Inception Model | Parameters | Epochs | Batch size | Accuracy | Training time |
  | ----------------| ---------- | -------| -----------| -------- | ------------- |
  | Transfer Learning CIFAR10 Dataset | 31,214,954 | 1 | 32 | 10% | 19 mins |
  | Transfer Learning CIFAR10 Dataset Layers added after mixed 7 layer | 28,322,826 | 1 | 32 | 54.60% | 29 sec |
  | [Inception scratch](https://www.analyticsvidhya.com/blog/2018/10/understanding-inception-network-from-scratch/) | 7,188,302 | 1 | 256 | 10.43% | 4 min 41 sec |
  
  - [Inception scratch training](https://colab.research.google.com/drive/10OMWzHiPGZA55PMUTJTFt8sn4T_p0hU5?usp=sharing)
    - Change 1:
      ```
      x = AveragePooling2D(pool_size=(7,7), strides=1, padding='valid',name='avg_pool_5_3x3/1')(x)
      ```
      To
      ```
      x = GlobalAveragePooling2D(name='avg_pool_5_3x3/1')(x)
      ```
    - Change 2: As colab crashes with CIFAR 10 resized to 224x224x3
      ```
      input_layer = Input(shape=(224, 224, 3))
      ```
      To
      ```
      input_layer = Input(shape=(128, 128, 3))
      ```
      
      - Another option would to use CIFAR10(32, 32, 3)
        - Use model.add(UpSampling2D()) to increase image size to 256
        - Followed by using repeated Conv2d block with kernel size of 3x3 to reduce image to 224x224
  
## [Task 8 Resnet architectures for CIFAR10 datatset](https://github.com/sbhrwl/computer_vision/blob/main/src/networks/resnet_architectures.py)
  | Resnet | Parameters | Epochs | Batch size | Accuracy | Training time |
  | ----------------| ---------- | -------| -----------| -------- | ------------- |
  | Transfer Learning CIFAR10 Dataset | 571,210 out of 24,163,786 | 1 | 256 | 21.77% | 2 mins 24 sec |
  | Transfer Learning (convnet) CIFAR10 Dataset | 20,490 out of 23,608,202 | 1 | 256 | 26.74% | 2 mins 24 sec |
  | Transfer Learning (skip_bn) CIFAR10 Dataset | 580,746 out of 24,115,850 | 1 | 256 | 57.74% | 5 hours 20 mins 24 sec |
  | [Scratch training CIFAR10 Dataset](https://pylessons.com/Keras-ResNet-tutorial/) | 23,555,082 | 1 | 256 | 10.47% | 10 min 11 sec |
  | Transfer Learning CIFAR100 Dataset | 603,876 out of 24,138,980 | 1 | 256 | 59.13% | 5 hours 42 min 44 sec |
  - Longest Training 
  <img src="https://github.com/sbhrwl/ComputerVision/blob/main/artifacts/images/resnet_cifar100_training.png">

## [Task 9 DenseNet architectures for CIFAR10 datatset](https://github.com/sbhrwl/computer_vision/blob/main/src/networks/densenet_architectures.py)
  | DenseNet | Parameters | Data Augmentation | Epochs | Batch size | Accuracy | Training time |
  | -------- | ---------- | ----------------- | ------ | ---------- | -------- | ------------- |
  | Transfer Learning CIFAR10 Dataset | 307,018 out of 7,347,338 | None | 1 | 256 | 50.91% | 2 mins 28 sec |
  | Transfer Learning CIFAR10 Dataset (Convnet) | 10,250 out of 7,347,338 | None | 1 | 256 | 56.84% | 2 mins 22 sec |

## [Task 10 EfficientNet architectures for CIFAR10 datatset](https://github.com/sbhrwl/computer_vision/blob/main/src/networks/efficientnet_architectures.py)
  | EfficientNet | Parameters | Data Augmentation | Epochs | Batch size | Accuracy | Training time |
  | ------------ | ---------- | ----------------- | ------ | ---------- | -------- | ------------- |
  | Transfer Learning CIFAR10 Dataset | 373,066 out of 6,951,633 | None | 1 | 256 | 10.05% | 1 mins 37 sec |
  | Transfer Learning CIFAR10 Dataset (Convnet) | 12,810 out of 6,588,049 | None | 1 | 256 | 9.95% | 1 mins 35 sec |

## Pytorch
- [Pytorch Basics](https://colab.research.google.com/drive/1-cd9S754YuFrqnVtm4AqerIGSCbcoCVJ?usp=sharing)
- [Fashion MNIST](https://colab.research.google.com/drive/19rEgaf0ufCGAdgzkxTQrHtz3E7KBjPR3?usp=sharing)
- [Custom Dataset](https://colab.research.google.com/drive/1n0fINUZZBXWWPVQFawLdOc_AqC4uTkL6?usp=sharing)
- [Transfer Learning](https://colab.research.google.com/drive/1Suewp8p6h0EUcFC5RQ5YnHB3AjDCXB5j?usp=sharing)

## [Creating own python package](https://github.com/sbhrwl/computer_vision/blob/main/docs/Creating_python_package.md)

## [Deployment](https://github.com/sbhrwl/computer_vision/blob/main/docs/Deployment.md)

## [Augmentation](https://github.com/sbhrwl/computer_vision/blob/main/docs/Augmentation.md)

## [Object Detection](https://github.com/sbhrwl/social_distance_violations/blob/main/docs/object_detection/Object_detection.md)

## [Image Segmentation](https://github.com/sbhrwl/social_distance_violations/blob/main/docs/image_segmentation/Image_segmentation.md)

## Feature store
- can you please explain feature store?
For example, we have some data and we are trying to build multiple models for different use cases using the same dataset, how would a feature store be useful in this case?
how is it used in industry?

- could you please also tell, how do we build model via transfer learning starting from layer3 of ResNet model using "Pytorch"

## References
- Kernels
  - [Kernels](https://setosa.io/ev/image-kernels/)
  - [Kernels as Edge Detector](https://aishack.in/tutorials/image-convolution-examples/)
- Convolution Visualisation
  - [2D visulaisation](https://www.cs.ryerson.ca/~aharley/vis/conv/flat.html)
  - [Tensor playground](https://tensorspace.org/html/playground/lenet.html)
  - [CNN explainer](https://poloclub.github.io/cnn-explainer/)
  - [ConvNetJS](https://cs.stanford.edu/people/karpathy/convnetjs/)
  - [NB](https://jovian.ai/paulbindass/convolutional-neural-network-world)
- [Callbacks](https://github.com/niconielsen32/NeuralNetworks/blob/main/CustomCallbacks.ipynb)
- [Train VGG, Inception and ResNet from scratch](https://machinelearningmastery.com/how-to-implement-major-architecture-innovations-for-convolutional-neural-networks/)
- [Neural networks repository](https://github.com/niconielsen32/NeuralNetworks)
- [Computer Vision repository](https://github.com/niconielsen32/ComputerVision)
- [Workload with GPUs](https://analyticsindiamag.com/webinar-alert-accelerating-data-science-workloads-with-gpus/)
- [Monk](https://clever-noyce-f9d43f.netlify.app/#/introduction)
  - [Monk GitHub](https://github.com/Tessellate-Imaging/monk_v1)
  - [Monk Blog](https://medium.com/@monkai/plant-disease-classification-with-monk-3a4d7ba419b9)
  - [Monk Colab](https://colab.research.google.com/drive/1HilR4pPZjgti0eLGzNc2ScvqR3kY2ihj?usp=sharing)
