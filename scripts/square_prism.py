#!/usr/bin/env python

from pathlib import Path

import nibabel as nib
import numpy as np
import argparse


def create_rectangular_prism(output: Path) -> None:
    data = np.zeros((40, 40, 40))
    data[10:30, 19:21, 19:21] = 1
    data[10:30, 19:21, 15:25] = 1
    data[10:30, 18:22, 16:24] = 1
    data[10:30, 17:23, 17:23] = 1
    data[10:30, 16:24, 18:22] = 1
    data[10:30, 15:25, 19:21] = 1

    affine = np.eye(4)
    affine *= 0.859375
    affine[:, 3] = -20
    affine[3, 3] = 1

    img = nib.Nifti1Image(data, affine)
    nib.save(img, output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path, metavar='rectangular_prism.nii')
    options = parser.parse_args()
    create_rectangular_prism(options.output)


if __name__ == '__main__':
    main()
