#!/usr/bin/env python

from pathlib import Path

import nibabel as nib
import numpy as np
import argparse


def cube(output: Path) -> None:
    data = np.zeros((40, 40, 40))
    data[19:21, 19:21, 17] = 1
    data[18:22, 18:22, 18] = 1
    data[17:23, 17:23, 19] = 1
    data[16:24, 16:24, 20] = 1
    data[17:23, 17:23, 21] = 1
    data[18:22, 18:22, 22] = 1
    data[19:21, 19:21, 23] = 1

    affine = np.eye(4)
    affine *= 0.859375
    affine[:, 3] = -20
    affine[3, 3] = 1

    img = nib.Nifti1Image(data, affine)
    nib.save(img, output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path, metavar='cube.nii')
    options = parser.parse_args()
    cube(options.output)


if __name__ == '__main__':
    main()
