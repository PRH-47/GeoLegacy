# LisBelos

Dlis & Lis files with easy acess.

## Intro

This project aims to ease the workflow with .Lis and .Dlis files. 
Also, it offers a text parser module to work with structured texts, such as AGP files from Petrobrás.

## Install

You can install the files in this project via Makefile.
Or, in case your computer doesn support make syntax, you can run the scripts located in the 
[scripts folder](/scripts).

#### Common Install

There is a common install process with the command:

```sh
make setup_common
```
This process will install all the requirements in the PYTHONPATH

#### Venv Install

There is a virtual enviroment install process with the command:

```sh
make setup_venv
```
This process will install all the requirements in the virtual enviroment.

# Table of Contents

- [GammaScan](#GammaScan)
- [Geofiles](#Geofiles)
- [Lis](#Lis)
- [Dlis](#Dlis)

# GammaScan

Both LisPlaza and DlisPlaza comes with the GammaScan.
It searches all the dataframes in the file for a 'GR' column, and appends it in to list.

```python
gamma1 = Dlis_Plaza.GammaScan()
```
# Geofiles

Here we have some functions to help find georelated files.

```python

from geofiles.searcher import Searcher

# Assign a root folder to be scanned
root = pathlib.Path('data')
dlis_list = Searcher.SearchDlis(root)

```
In the example above, we scanned the root folder, for all the Dlis files.
It is specially usefull when working with a large number of files.

# Lis 

Log Interchange Standard (LIS) is the predecessor to DLIS and was developed by Schlumberger in the late 1970s.

Like DLIS, LIS is a binary (big-endian) format. It it is based on the VAX binary information standard and has an even more awkward syntax than DLIS.

But still, LIS files are still being produced and immense volumes of historical logging information exists in this format. Log I/O is a convenient platform for being able to manage and maintain this information.

A physical LIS file consists of one or more logical LIS files, each containing a set of records (meta-data) of different types as well as an index curve and a set of measurement curves. Each curve may have one or several samples per depth measure, and in addition the curves may be single- or multi-dimensional.

## LisBelo 

The LisBelo object was created to ease the process of merging and flattening the logical files inside the physical one.

A quick look in the object:
[LisBelo Object](/lisbelo/lisbelo.py)

## LisPlaza

The LisPlaza was created to ease the workflown when dealing with a large number of files.

```python

root = pathlib.Path('/Users/giba')
lis_list = Searcher.SearchLis(folder_path= root)

# - Passing the list of paths to the Lis_plaza object
openlist1 = Lis_Plaza(lis_list)

```
[LisBelo Object](/lisbelo/lisplaza.py)

# Dlis 

Digital Log Interchange Standard (DLIS) is a digital well log format introduced as Recommended Practice 66 (RP 66) by the American Petroleum Institute in 1991. RP 66 exists in two versions, V1 and V2. V2 is not commonly used. DLIS is a binary (big-endian) data format.

DLIS is an old format in all possible ways. Available DLIS software is limited and to a large degree orphaned technology. The existence of programming tools for DLIS are absent. There is no easily accessible DLIS format description available, dialects exists, and DLIS is in general very hard to digest.

But still, DLIS is the main storage and communication medium for wellbore logging information. Since logging technology has evolved substantially since the introduction of the format, the amount of information contained may be vast; multi-GB volumes are commonplace.

Note that a physical DLIS file consist of a file header and one or more logical DLIS files, each containing a number of sets (meta-data), one or more frames containing curve data, and possibly a set of encrypted records. A frame contains an index curve and a set of measurement curves. Each curve may be single- or multi-dimensional.

## DlisBelo 

The LisBelo object was created to ease the process of merging and flattening the logical files inside the physical one.

A quick look in the object:
[LisBelo Object](/lisbelo/dlisbelo.py)

## DlisPlaza

The LisPlaza was created to ease the workflown when dealing with a large number of files.

[LisBelo Object](/lisbelo/dlisplaza.py)


