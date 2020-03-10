# Minimum Weight Spanning Tree

## Table of Contents

- [Author](#author)
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## Author <a name = "author"></a>
Jack Liu

liudun199903@gmail.com
## About <a name = "about"></a>

This is a little program that determines a minimum weight spanning tree in a weighted connected graph. The program will read input_file, solve the MWST problem for the connected weighted graph it encodes, and create output_file containing the solution.

The first two lines of an input file will contain single integers 𝑛 and 𝑚, giving the number of vertices and the number of edges in 𝐺, respectively. The vertices will be labeled by the set 𝑉 = {1, 2, 3, … , 𝑛}. The next 𝑚 lines will each contain two integers (vertex labels) and one real number, separated by spaces, giving the end vertices and weight of an edge in 𝐺. The edge labels will be determined by the position of an edge in this list. In general, a triple 𝑥, 𝑦, 𝑤 on line 𝑖 + 2 defines an edge with label 𝑖 (for 1 ≤ 𝑖 ≤ 𝑚).

Each of the 𝑚 + 2 lines of the input file will end in a Unix newline character. The following example defines the weighted graph on page 2.
```
7
11
1 2 6
1 4 3
2 3 5
2 5 8
3 5 1
3 7 4
4 5 7
4 6 9
5 6 6
5 7 5
6 7 2
```

An output file will contain 𝑛 lines. The first 𝑛 − 1 lines will give the edges of an MWST in the following
format.
```
label: (end1, end2) weight
```
The last line will give the
total weight of the spanning tree. A possible output file for the above example is then
```
   5: (3, 5) 1.0
  11: (6, 7) 2.0
   2: (1, 4) 3.0
   6: (3, 7) 4.0
   3: (2, 3) 5.0
   1: (1, 2) 6.0
Total Weight = 21.00
```
Note that a valid output file for this project is not unique, since there may be more than one MWST for a given graph, and the edge list may be given in any order. Also the pair (𝑥, 𝑦) denotes an unordered pair which could also be specified as (𝑦, 𝑥). Other than these variations, an output file must match the above format exactly. In particular the label will be right justified in a field of width 4, followed by a colon, then a space, then (𝑥, 𝑦) or (𝑦, 𝑥), then the weight 𝑤 rounded to one decimal place. The last line will begin at column 1, and the weight will be rounded to 2 decimal places. 

## Getting Started <a name = "getting_started"></a>

Before running this, please make sure that Python 3 is installed on your environment.

The ```Makefile``` in the repo is just a fake one that copies the code and rename it without the file extension. It is there to comply with the grading policy and make the life of the grader easier.

## Usage <a name = "usage"></a>

You can either run it with Python 3 interpreter
```
python3 MWST.py in_file out_file
```
or give it the execution permission and run it directly (It still goes through the interpreter, but you won't have to type it out.)
```
chmod +x MWST.py
./MWST.py in_file out_file
```

Test cases can be found in the directory ```test_cases```.

## Credit

The information in [About](#about) and the ```test_cases``` are provided by CSE 102 (Prof. Patrick Tantalo) at UC Santa Cruz