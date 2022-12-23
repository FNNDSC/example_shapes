#!/usr/bin/env python

from pathlib import Path

import nibabel as nib
import numpy as np
import argparse


def pyramid(output: Path) -> None:
    data = np.zeros((40, 40, 40))
    data[16:24, 16:24, 18] = 1
    data[17:23, 17:23, 19] = 1
    data[18:22, 18:22, 20] = 1
    data[19:21, 19:21, 21] = 1

    affine = np.eye(4)
    affine *= 0.859375
    affine[:, 3] = -20
    affine[3, 3] = 1

    img = nib.Nifti1Image(data, affine)
    nib.save(img, output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path, metavar='pyramid.nii')
    options = parser.parse_args()
    pyramid(options.output)


if __name__ == '__main__':
    main()
