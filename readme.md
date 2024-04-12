# Grad-CAM visualization and CNN based Grape Leaf Disease Classification using Six-Wheeler Rover </br>  </br> 



## This project is a part of a research paper titled: 
"Enhancing Agriculture through Real-Time Grape Leaf Disease Classification on Edge Device with Lightweight CNN Architecture and Grad-CAM" (Under Review)



## Abstract
<div style="text-align: justify">
A major threat to agriculture, crop diseases have an impact on marketability, yields, and quality. Our work tackles this problem by utilizing edge computing and machine learning to create a lightweight convolutional neural network (CNN) model called MobileNetV3 Large that is ideal for real-time grape leaf disease classification on edge devices. Our model achieves improved efficiency and effectiveness by incorporating innovations such as the squeeze-and-excitation structures and the h-swish activation function. The reliability of the model is ensured by custom layers, such as dropout layers, which reduce overfitting. Our model surpasses current techniques after thorough evaluation, averaging 99.42% test accuracy with good precision, recall, and F1 score. Our model is tested and shown to be able to predict images in 90 milliseconds with a 1-watt power consumption on the Nvidia Jetson Nano. Furthermore, CNN's decision-making process can be influenced by the identification of crucial image regions through the use of Grad-CAM visualization techniques. Our research advances autonomous farming practices by enabling real-time disease detection on edge devices. This will empower researchers, agronomists, and farmers to effectively monitor and mitigate plant diseases, thereby improving global food security.
</div>
</br/>

### Installation of Tensorflow 2.4 on Jetson Nano
Installing Tensorflow in Jetson Nano was quite a difficult task. Most of the time, you will face dependency problems as different versions of each library are mismatched. To have a hassle-free installation, you can follow the following commands in a freshly booted Jetson Nano(Jetpack 4.6.1)


There is a website where you can get to know the process of flashing Ubuntu 20.04 on Jetson Nano [here](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image). It will install Python 3.8 as well as different important machine-learning libraries like Pytorch and TensorFlow without any version conflict. Make sure to take a look at the process on this webpage. It's easy. You can find the image here.  ![Example Image](images/example.png)
Password: "jetson"

After Boot

```bash
    $ sudo apt-get update
    $ sudo apt-get upgrade
```



#### Final Check
Open a terminal and type to check the version
```bash
    $ pip3 show tensorflow
    $ pip3 list | grep tensorflow               
```


### Installing a lightweight IDE (VS Code)
```bash
    $ git clone https://github.com/JetsonHacksNano/installVSCode.git
    $ cd installVSCode
    $ ./installVSCode.sh
```
Run VS Code....
```bash
    $ code-oss
```
More details on VS code installation can be found [here](https://jetsonhacks.com/2019/10/01/jetson-nano-visual-studio-code-python/).
