# odometry

This repository contains visual odometry baselines that you can evaluate on several datasets.
Currently provided methods:
-LS-VO
-Resnet50

Currently supported datasets:
-KITTI
-TUM
-DISCOMAN

# Installation

1. git clone --recursive https://github.com/vul-samsung/odometry
2. conda env update -f conda.yml
3. python download_weights.py

# Preparing datasets:
1. Download datasets from official websites
2. Prepare dataset for training with scriptsprepare_dataset.py
3. Configure paths in env.py

# Training
Start training with scripts/train.py 
