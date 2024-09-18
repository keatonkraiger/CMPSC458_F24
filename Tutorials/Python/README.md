# Python ModerGL Tutorials

This tutorial introduces the basics of programming with OpenGL for Penn State's CMPSC 458: Fundamentals of Computer Graphics course (Fall 2024). Note that this directory is specifically for Python users, though we encourage students to look at the C++ tutorial as well since many of the underlying concepts are the same.

## Using Python

In this course, we'll be providing students the option of using classic OpenGL with C++ or using Python with ModernGL. ModernGL is a Python wrapper for OpenGL. 

## Getting Started

We encourage students to use a virtual environment for all projects. This will help keep your system clean and avoid conflicts with other projects. We specifically recommend using Anaconda, though you can use any virtual environment you like.

### Anaconda

We'll assume that you will be using Anaconda for your virtual environment. If you don't have Anaconda installed, you can download it [here](https://www.anaconda.com/products/distribution). Setup and installation instructions can be found [here](https://docs.anaconda.com/anaconda/install/). 

Installation can vary depending on your operating system, so make sure to follow the instructions for your specific OS.

### Creating a Virtual Environment

To create a virtual environment, you can run the following command in your terminal:

```bash
conda create --name graphics python=3.10 -y
```

This will create a new virtual environment called `graphics` with Python 3.10 installed. You can activate the environment by running:

```bash
conda activate graphics
```

### Package Installation

Projects will use a few different packages which you will need to install. We've provided a `requirements.txt` file in each project directory which you can use to install the necessary packages. You can install the packages by running:

```bash
pip install -r requirements.txt
```

## Tutorial 1

In this first tutorial we will be getting comfortable with running python programs and exectuting a simple OpenGL program. We encourage you to first look at the C++ tutorial and its documentation to get a better understanding of the underlying concepts. You can then look through the Python code to see how it compares.

### Running the Code

To run the code, you can simply run the following command in your terminal:

```bash
python tutorial_1.py
```


