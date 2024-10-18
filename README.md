# HamiltonianPath_Czaplewski
In this repository is the contents of Jason Czaplewski's Project 1 Hamiltonian Path

NOTE:
For some reason you cannot acces the pdf unless you click the download raw file button so I attached screenshots of the files that are not submitted to gradescope (SS) in order to make sure that you can see them.

Code Development:
When starting the code I broke it down into a few core components; random graph generation, Hamiltonian cycle detection, performance measurement, and data visualization. I initially worked on generating random graphs using the NetworkX library and implementing the brute-force algorithm to check for Hamiltonian cycles by examining all vertex permutations. After making sure they were correct with small manually constructed graphs, I then started timing the execution using the high precision timer (time.perf_counter()). This allowed me to accurately measure the execution times as the vertex sizes increased. To ensure the results were accurate, multiple trials were run for each graph size. I then averaged the results to get rid of the variability introduced by random graph generation. Once the core functionality was in place I used Matplotlib to plot individual and average execution times. Finally, I ran multiple trials across different graph sizes in order to be able to run the code in an effective manner but still see the exponential growth in the graph. 

Issues:
When running the code I kept encountering zero exectution time for many of the random iterations of the trials even at high vertices. I presumed that these were the non hamiltonian paths being graphed however when I tried to go back into the code and remove them it would mess up the randomization. Therefore, on the graph you see the two different y intercepts. The one of the left is the exectution time for each point and the one on the right is the average execution time. I broke these up so that you can visually see the linear growth because without that the slope did not increase in an expected manner.
