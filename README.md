# AC2

> Towards Understanding Architectural Changes in Python Projects

![](landing_page.png)

## Directory Structure

- [file_map_engine/](src/main/file_map_engine)
  - [ast_engine.py](src/main/file_map_engine/ast_engine.py)
  - [ast_helper.py](src/main/file_map_engine/ast_helper.py)
  - [call_dir.py](src/main/file_map_engine/call_dir.py)
  - [engine.py](src/main/file_map_engine/engine.py)
  - [test.ipynb](src/main/file_map_engine/test.ipynb)
- [static/](src/main/static)
  - [This directory contains the cohesion data for the target repository]
- [target_repo_dir/](src/main/target_repo_dir)
  - [tags.txt](src/main/target_repo_dir/tags.txt)
- [templates/](src/main/templates)
  - [home.html](src/main/templates/home.html)
  - [index.html](src/main/templates/index.html)
- [main.py](src/main/main.py)
- [requirements.txt](src/main/requirements.txt)

## Cohesion value interpretation (Using lcom)

Score:

- `==1` - indicates a cohesive class, which is the "good" class;
- `>=2` - indicates a problem. The class should be split into so many smaller classes;
- `==0` - happens when there are no methods in a class. This is also a "bad" class.

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
>
> ![](demo_image_0.png)

> #### Compare two different versions of a repository by their respective annotated call graphs and collaboration graphs
>
> ![](demo_image_last.png)


## Results
We have evaluated 10 repositories using AC2. For each repository, we have compared its first release with its subsequent releases. 
[Results](https://github.com/dheerajrox/AC2/tree/master/Results)


## How to Contact?

For more information about the project and support requests, feel free to contact A Eashaan Rao(cs19s501@iittp.ac.in), Dheeraj Vagavolu(cs17b028@iittp.ac.in) and Sridhar Chimalakonda(ch@iittp.ac.in). Please open an issue or pull request if you find any bug or have an idea for enhancement.


Research in Intelligent Software and Human Analytics (RISHA) Lab, Indian Institute of Technology Tirupati

Team:
Dheeraj Vagavolu, A Eashaan Rao and Sridhar Chimalakonda
