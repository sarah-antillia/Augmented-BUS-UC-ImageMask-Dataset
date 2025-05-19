# Copyright 2025 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# 2025/05/15
# MaskGrayscaler.py

import os
import cv2
import glob
import shutil
import numpy as np
import traceback

#from GrayScaleImageWriter import GrayScaleImageWriter

class MaskGrayscaler:

  def __init__(self, images_dir, masks_dir, 
                  output_images_dir, output_masks_dir):
    W = 512
    H = 512
 
    image_files = glob.glob(images_dir + "/*.jpg")
    mask_files  = glob.glob(masks_dir  + "/*.jpg")
    for image_file in image_files:
      # Resize to (512x512)
      image = cv2.imread(image_file)
      image = cv2.resize(image, (W, H))
      basename = os.path.basename(image_file)
      output_image_file = os.path.join(output_images_dir, basename)
      cv2.imwrite(output_image_file, image)
      print("Saved {}".format(output_image_file))

    for mask_file in mask_files:
      mask = cv2.imread(mask_file)
      mask = cv2.resize(mask, (W, H))
      b, g, r = cv2.split(mask)
      #gray = 0.299 * r + 0.587 * g + 0.114 * b  # BT.601
      gray = 0.6 * r + 0.4 * g #+ 0.114 * b  # BT.601

 
      basename = os.path.basename(mask_file)

      output_mask_file = os.path.join(output_masks_dir, basename)
      cv2.imwrite(output_mask_file, gray)    
      print("Saved {}".format(output_mask_file))


if __name__ == "__main__":

  try:
    images_dir = "./BUS-UC-master/images"
    masks_dir  = "./BUS-UC-master/masks"
    output_dir        = "./BUS-UC-Grayscale-master"
    output_images_dir = output_dir + "/images"
    output_masks_dir  = output_dir + "/masks"

    if os.path.exists(output_dir):
      shutil.rmtree(output_dir)
    os.makedirs(output_dir)  
    
    os.makedirs(output_images_dir)
    os.makedirs(output_masks_dir)

    # Create Benign image and green-colored mask files 
    MaskGrayscaler(images_dir, masks_dir, 
                  output_images_dir, output_masks_dir)
    
  except:
    traceback.print_exc()

    pass

    