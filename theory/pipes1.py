"""
A pipe is a connection between two processes in Python.
It is used to send data between them.
"""
from multiprocessing import Pipe


def main():
    c1, c2 = Pipe()
    """
    In a unidirectional pipe created with Pipe() without specifying duplex=True, conventionally, one end of the 
    pipe (c1) is used for sending data, while the other end (c2) is used for receiving data. However, Python doesn't 
    inherently prevent you from sending data through c2 or receiving data through c1 in this context. You can 
    technically use either end for sending or receiving data.

    When you use duplex=True, you explicitly create a bidirectional pipe, where both ends (c1 and c2) can be used for 
    both sending and receiving data. This is a feature provided by Python's multiprocessing module for scenarios where 
    bidirectional communication is needed.

    So, to clarify, in both cases (duplex=True and duplex=False, i.e., the default), you can technically use either end 
    of the pipe for sending or receiving data, but it's a convention to use c1 for sending and c2 for receiving in the 
    default unidirectional case.
    """
    c1.send("data")
    print(f"Data to be received: {c2.poll()}")
    obj = c2.recv()  # this is blocking, if there is nothing sent, use it in combination with poll()
    print(obj)
    print("Data to be received: ", c2.poll())

    """In Python, the symbol ... is called an ellipsis. It is used as a placeholder to indicate an incomplete code 
    snippet or data structure. It's often used in contexts such as slicing multidimensional arrays or indicating an 
    unfinished block of code.

Additionally, in NumPy, the ellipsis (...) can be used to index arrays with an arbitrary number of dimensions. It's 
particularly useful when working with high-dimensional arrays."""


if __name__ == "__main__":
    main()
