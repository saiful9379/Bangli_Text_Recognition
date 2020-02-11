# Bangli Optical Character Recognition

Text recognition (optical character recognition) is implement to pytorch. this method we use resnet50 for feature extraction BiLSTM and Attention.



# Environment
- python 3.6
- PyTorch 1.1.0, CUDA 9.0,

You may need pip3 install torch==1.1.0

Requirements : lmdb, pillow, torchvision, nltk, natsort

- pip install lmdb pillow torchvision nltk natsort



# Prepare dataset

At this time, gt.txt should be {imagepath}<space>{label}\n
For example
```
test/word_1.png saiful
test/word_2.png sungargonj
test/word_3.png moniram kazy
```

```pip install fire```


Then go utility folder and check those unique classes that are add in class file or not.

```get_unique.py``` And then split train and val use ```train_val_split.py```

After split run this script,

```python create_lmdb_dataset.py --inputPath dataset/train/img --gtFile dataset/train/gt.txt --outputPath mdb_dataset/train```

or my previous create lmdb_dataset
- [mdb_own_creating](https://drive.google.com/drive/folders/1BtJ7dbn42tCrOBi1PnvfGdUhk4ijVAgi?usp=sharing)

# Training 
```
CUDA_VISIBLE_DEVICES=0 python train.py \
--train_data mdb_dataset/train --valid_data mdb_dataset/val \
--select_data / --batch_ratio 1 \
--Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn
```

# Download pretrain model:
- [model](https://drive.google.com/file/d/1O0EhtSP_m-pQZS5MPqXJzl4SoN79cxl5/view?usp=sharing)

# Test Demo
```
CUDA_VISIBLE_DEVICES=0 python demo.py \
--Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn \
--image_folder demo_image/ \
--saved_model bn_models/TPS-ResNet-BiLSTM-Attn.pth
```


## For Cpu:
```
python demo.py \
--Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn \
--image_folder demo_image/ \
--saved_model saved_models/best_accuracy.pth
```
