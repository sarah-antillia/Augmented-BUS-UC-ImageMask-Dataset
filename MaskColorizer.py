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
# MaskColorizer.py

import os
import cv2
import glob
import shutil
import numpy as np
import traceback

from GrayScaleImageWriter import GrayScaleImageWriter

class MaskColorizer:

  def __init__(self, images_dir, masks_dir, mask_color,
                  output_filename_prefix, 
                  output_images_dir, output_masks_dir):
    W = 512
    H = 512
    writer = GrayScaleImageWriter(colorize=True, black="black", white=mask_color, verbose=False)

    image_files = glob.glob(images_dir + "/*.png")
    mask_files  = glob.glob(masks_dir  + "/*.png")
    for image_file in image_files:
      # Resize to (512x512)
      image = cv2.imread(image_file)

      image = cv2.resize(image, (W, H))
      basename = os.path.basename(image_file)
      nameonly = basename.split(".")[0]
      output_image_file = os.path.join(output_images_dir, output_filename_prefix + nameonly + ".jpg")
      cv2.imwrite(output_image_file, image)
      print("Saved {}".format(output_image_file))

    for mask_file in mask_files:
      mask = cv2.imread(mask_file)
      #print(mask.shape)
      mask = cv2.cvtColor(mask,  cv2.COLOR_BGR2GRAY)

      basename = os.path.basename(mask_file)
      nameonly = basename.split(".")[0]

      output_mask_file = os.path.join(output_masks_dir, output_filename_prefix + nameonly + ".jpg")
      writer.save_resized(mask, (W, H), output_masks_dir, output_filename_prefix + nameonly  )
    
      print("Saved {}".format(output_mask_file))


if __name__ == "__main__":

  try:
    images_dir = "./BUS_UC/Benign/images"
    masks_dir  = "./BUS_UC/Benign/masks"
    mask_color = "green" 
    output_filename_prefix = "B_"
    output_dir        = "./BUS-UC-master"
    output_images_dir = output_dir + "/images"
    output_masks_dir  = output_dir + "/masks"

    if os.path.exists(output_dir):
      shutil.rmtree(output_dir)
    os.makedirs(output_dir)  
    
    os.makedirs(output_images_dir)
    os.makedirs(output_masks_dir)

    # Create Benign image and green-colored mask files 
    MaskColorizer(images_dir, masks_dir, mask_color,
                  output_filename_prefix, 
                  output_images_dir, output_masks_dir)
    
    
    images_dir = "./BUS_UC/Malignant/images"
    masks_dir  = "./BUS_UC/Malignant/masks"
    mask_color = "red"
    output_filename_prefix = "M_"

    # Create Malignant image and red-colored mask files 
    MaskColorizer(images_dir, masks_dir, mask_color,
                  output_filename_prefix, 
                  output_images_dir, output_masks_dir)
  

  except:
    traceback.print_exc()

    pass

    