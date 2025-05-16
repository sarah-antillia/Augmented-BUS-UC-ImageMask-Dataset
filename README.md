<h2>Augmented-BUS-UC-ImageMask-Dataset (2025/05/17)</h2>

This is a 512x512 pixels Augmented Benign and Malignant ImageMask Dataset derived by us from 
<a href="https://data.mendeley.com/datasets/3ksd7w7jkx/1">
Mendeley Data: BUS_UC</a>
<br>

<br>
<b>Download our dataset</b><br>
You can download our dataset from the google drive 
<a href="https://drive.google.com/file/d/1ObyZhN7up0Crhxsi5dkcu9oUo_zVQCL3/view?usp=sharing">
Augemented-BUS-UC-ImageMask-Data.zip</a>
<br>

<h3>1. Dataset Citation</h3>
We used the following dataset in Mendeley web site<br>
<a href="https://data.mendeley.com/datasets/3ksd7w7jkx/1">
Mendeley Data: BUS_UC</a>
<br><br>

<b>Description</b><br>
The BUS_UC dataset includes 358 benign tumor images and 453 malignant tumor images. 
The resolution of Ultrasound images is 256 × 256 pixels. 
All these images were obtained from the website Ultrasound Cases (ultrasoundcases.info),
 which does not provide ground truth images. 
 Therefore, with the help of an experienced radiologist, benign and malignant tumor images are annotated 
 for segmentation and classification task.
<br>
<br>
<b>Citation </b><br>
If you use this dataset, please cite :<br>

Ahmed Iqbal, Muhammad Sharif,<br> 
"Memory-efficient transformer network with feature fusion for breast tumor segmentation and classification task
", <br>
Engineering Applications of Artificial Intelligence, 2023.<br><br>

<b>Institutions</b><br>
COMSATS Institute of Information Technology - Wah Campus
<br><br>
<b>Categories</b><br>
Breast Cancer, Image Segmentation, Ultrasound, Image Classification
<br><br>
<b>License</b><br>
<a href="https://creativecommons.org/licenses/by/4.0/deed.en">
CC BY 4.0
</a>
<br>

<h3>2. ImageMaskDataset Generation</h3>
<h3>2.1 Download BUS_UC dataset</h3>

If you would like to generate this Augmented dataset by yourself,
please download the master dataset from 
<a href="https://data.mendeley.com/datasets/3ksd7w7jkx/1">
Mendeley Data: BUS_UC</a>
<br>
<br>

<h3>2.2 Generate colored mask files</h3>
  The BUS_UC dataset includes 2 types of images and masks data, Benign and Malignant,
  but those mask files are all white-black image.
Therefore, we created green and red colored mask files from masks in Benign and Malignant dataset.
by using Python script <a href="./MaskColorizer.py">MaskColorizer.py</a><br>

<pre>
python MaskColorizer.py
</pre>
This command generates BUS-UC-master dataset from the original Benign and Malignant datasets<br>
<pre>
./BUS-UC-master
├─images
└─masks
</pre>

<br>
<b>BUS-UC-master mages sample</b><br>
<img src="./asset/BUS-UC-master-images.png" width="1024" height="auto"><br>
<br>
<b>BUS-UC-master masks sample</b><br>
<img src="./asset/BUS-UC-master-masks.png" width="1024" height="auto"><br>
<br>

The number of images and mask files in BUS-UC-master is 811 respectively, and not enough to use a training set of 
a segmentation model.
Therefore, to increase of the number of the dataset, we used an offilne augmention tool <a href="./ImageMaskDatasetGenerator.py">
ImageMaskDataGenerator,py</a>
to augment BUS-UC-master dataset, The tool supports the following data augmentation methods.<br>
<li>hfip</li>
<li>vflip</li>
<li>rotation</li>
<li>shrinking</li>
<li>deformation</li>
<li>distortion</li>
<li>barrel_distortion</li>
<li>pincussion_distortion</li>
<br>


<h3>2.3 Split master</h3>

Please run the following command for Python <a href="./split_augmented_master.py">split_augmented__master.py</a> 
<br>
<pre>
>python split_augmented_master.py
</pre>
This splits Augmented-BUS-UC-master into test, train and valid subdatasets.<br>
<pre>
./Augmented-BUS-UC-ImageMask-Dataset
├─test
│  ├─images
│  └─masks
├─train
│  ├─images
│  └─masks
└─valid
    ├─images
    └─masks
</pre>
<hr>
Train images sample<br>
<img src="./asset/Augmented-BUS-UC-ImageMaskDataset-train-images-sample.png" width=1024 heigh="auto"><br><br>
Train mask sample<br>
<img src="./asset/Augmented-BUS-UC-ImageMaskDataset-train-masks-sample.png" width=1024 heigh="auto"><br><br>


Dataset Statistics <br>
<img src="./Augmented-BUS-UC-ImageMask-Dataset_Statistics.png" width="512" height="auto"><br>
