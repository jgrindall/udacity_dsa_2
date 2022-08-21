## Running the project:

Note: python3 -> 'py' for Windows


- To install:
                        
            > git clone https://github.com/jgrindall/udacity_dsa_1.git


- To run some unit tests:

            > python3 -m doctest -v tests.txt


- Task0

            > python3 Task0.py

This is O(1)


- Task2
            
            > python3 Task1.py

Creating the lists is O(n).

Performing the set union is also O(n) since checking if elements exist in a Python set is O(1).

Overall, this is O(n).


            
- Task 2

            > python3 Task2.py

Creating the 'count' object is O(n).

Creating the .items() list is O(n).

Sorting the array is O(n logn).

Overall, this is O(n logn).


- Task 3
            
            > python3 Task3.py
            


For Part A, 'get_receiving_from_area' is O(n), the map operation is also O(n), and the sort is O(n logn) so this is O(n logn) overall.

For Part B, the filter operation is O(n), and the final calculation is O(1), so this is O(n) overall. 



- Task 4
            
            > python3 Task4.py

Creating the three lists is O(n).

The set difference operations are also O(n).

The final sort is O(n logn).

Overall, this is O(n logn)


