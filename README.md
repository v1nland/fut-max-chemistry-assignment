# FUT max chemistry assignment

This Python module is just a simple wrapper for the C++ code written by Jonker to implement the Jonker-Volgenant algorithm, LAPJV, for the linear assignment problem.

See the important notes below to properly use this algorithm. For a more tolerant, but slower, LAP algorithm see http://github.com/hrldcpr/hungarian

Note that this module depends on the numpy module. You must install numpy before you can compile this module. Numpy can be downloaded from http://numpy.scipy.org

If you have any problems with this module, you should contact me, not Dr. Jonker.

To build this module run:

    > python setup.py build

Then you can either put the file build/lib-<YOUR-PLATFORM>/LAPJV.so in the same directory as the code that will be using it, or you can install it so that all of your python programs can see it:

    > python setup.py install

For the module's documentation, type at a Python prompt:

    >>> help('LAPJV')

For a usage example see fut/bipartite_graph.py
