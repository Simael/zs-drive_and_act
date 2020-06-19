# ZS-Drive&Act

## Overview
Benchmark protocol for zero-shot driver behavior recognition on the Drive&Act dataset.
The protocol was proposed in our paper [Activity-Aware Attributes for Zero-Shot Driver Behavior Recognition](http://openaccess.thecvf.com/content_CVPRW_2020/html/w54/Reiss_Activity-Aware_Attributes_for_Zero-Shot_Driver_Behavior_Recognition_CVPRW_2020_paper.html).
For the Drive&Act dataset, please visit [https://www.driveandact.com/](https://www.driveandact.com/).

## Notes on the splits
For evaluating Zero-Shot methods on the Drive&Act dataset, we generated 10 random splits along the 34 mid-level classes (also called semantic actions or fine-grained activities).

To this end, for each split, we took the 34 classes and partitioned them into 14 classes for training, 10 classes to validate and tune hyperparameters on and 10 classes to test the final model.

In Zero-Shot learning terms, therefore, we have 14 seen classes to train on, 10 unseen classes to tune on and 10 unseen classes to test a final model on.

All split information is found in textfiles, with the following naming convention:

- Training classes for split n: midlevel_seen_classes_[n].txt
- Validation classes for split n: midlevel_unseen_classes_val_[n].txt
- Testing classes for split n: midlevel_unseen_classes_test_[n].txt

All 10 random splits are found in the [splits folder](https://github.com/Simael/zs-drive_and_act/tree/master/splits).

## Driver activities with Attributes
In the [paper](http://openaccess.thecvf.com/content_CVPRW_2020/html/w54/Reiss_Activity-Aware_Attributes_for_Zero-Shot_Driver_Behavior_Recognition_CVPRW_2020_paper.html) we also derive attributes from the hierarchical annotations of Drive&Act.
The binary attributes can be found in the [folder of the same name](https://github.com/Simael/zs-drive_and_act/tree/master/attributes).
We provide three files to load the attribtues:

- attribute_matrix.csv contains the 37 binary values for the 34 classes. Each class occupies a row in this matrix.
- classes.txt contains the names of the 34 classes, each line corresponds to the class of the corresponding row in the attribute matrix.
- attributes.txt contains the names of the 37 attribtues. Each line corresponds to the respective column of the attribute matrix.

For an example on how to load the attributes into vectors, please see [here](https://github.com/Simael/zs-drive_and_act/blob/master/semantic_embedding_utils.py).

## List of ZS-Drive&Act classes
The following list comprises all ZS-Drive&Act classes:

- closing_bottle
- closing_door_inside
- closing_door_outside
- closing_laptop
- drinking
- eating
- entering_car
- exiting_car
- fastening_seat_belt
- fetching_an_object
- interacting_with_phone
- looking_or_moving_around (e.g. searching)
- opening_backpack
- opening_bottle
- opening_door_inside
- opening_door_outside
- opening_laptop
- placing_an_object
- preparing_food
- pressing_automation_button
- putting_laptop_into_backpack
- putting_on_jacket
- putting_on_sunglasses
- reading_magazine
- reading_newspaper
- sitting_still
- taking_laptop_from_backpack
- taking_off_jacket
- taking_off_sunglasses
- talking_on_phone
- unfastening_seat_belt
- using_multimedia_display
- working_on_laptop
- writing

For semantic embeddings based on words such as the word2vec embeddings we employed the following pre-processing:

1) Drop the underscores.
2) For the activity "looking or moving around (e.g. searching)" we drop the extension "(e.g. searching)".
3) Compute the word2vec embedding for each word in the class name individually.
4) For class names with multiple words, average the word embeddings of the individual words.

## Pre-training on Kinetics-600
When pre-training activity recognition models on large-scale datasets, it has to be ensured, that the classes of such datasets do not overlap with the target classes of the Zero-Shot Learning dataset, e.g. Drive&Act.

To achieve this, we provide the names of the manually selected classes in the [Kinetics-600 dataset](https://arxiv.org/abs/1808.01340), that do not overlap with Drive&Act.
Pre-training on [these 550 classes](https://github.com/Simael/zs-drive_and_act/blob/master/kinetics_600_excluding_drive_and_act.txt) does not violate the Zero-Shot condition for this benchmark.
