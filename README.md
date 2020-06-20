# AC2
> Towards Understanding Architectural Changes in Python Projects

![](landing_page.png)

## Directory Structure

* [file_map_engine/](.\main\file_map_engine)
  * [ast_engine.py](.\main\file_map_engine\ast_engine.py)
  * [ast_helper.py](.\main\file_map_engine\ast_helper.py)
  * [call_dir.py](.\main\file_map_engine\call_dir.py)
  * [engine.py](.\main\file_map_engine\engine.py)
  * [test.ipynb](.\main\file_map_engine\test.ipynb)
* [static/](.\main\static)
  * [This directory contains the cohesion data for the target repository]
* [target_repo_dir/](.\main\target_repo_dir)
  * [tags.txt](.\main\target_repo_dir\tags.txt)
* [templates/](.\main\templates)
  * [home.html](.\main\templates\home.html)
  * [index.html](.\main\templates\index.html)
* [main.py](.\main\main.py)
* [requirements.txt](.\main\requirements.txt)


## Installation

Clone or download this github repository:

```sh
git clone https://github.com/dheerajrox/AC2.git
```

Get into the main directory:

```sh
cd AC2/src/main
```

Install the requirements:

```sh
pip install -r requirements.txt
```

## Usage example

To start the server use the following command:

```sh
python main.py
```

Then, open your browser to 'http://localhost:5000/'

> #### Enter a Python Github Repository link and press enter to generate annotated graphs in available views.
![](demo_image_1.png)

> #### Compare two different versions of a repository by their respective annotated call graphs and collaboration graphs
![](demo_image_2.png)

## Meta

Developed by:
DHEERAJ VAGAVOLU 
dheerajrox98@gmail.com

Research in Intelligent Software and Human Analytics (RISHA) Lab, Indian Institute of Technology Tirupati

Team:
Dheeraj Vagavolu, A Eashaan Rao and Sridhar Chimalakonda



