# Stock Fetcher Test
In this project, I am doing just a test between Java and Python api call.
    There is a simple API which the client or request has to call and the return type 
    is JSON data of stocks, now what i have done is that, write the data to a file line by line.

    And then we will just see the time taken and compare.

## First Test: (Java without Parallel Stream):
*Java*:

![java test](./images/Screenshot%202023-01-31%20at%2010.36.55%20PM.png)

__*It takes around 3.5 seconds.*__

*Python*:
![python test](./images/Screenshot%202023-01-31%20at%2010.41.53%20PM.png)

__*It takes around 3.8 seconds.*__

## Second Test: (Used parallel stream in java):
*Java*:

![java test 2](./images/Screenshot%202023-01-31%20at%2010.51.28%20PM.png)

__*It took 3.6 seconds*__

*Python*:

![python test 2](./images/Screenshot%202023-01-31%20at%2010.52.31%20PM.png)

__*It took around 3.8 seconds*__

__In test 2, I have deleted the already created files and re run with small change in java file,
changed the stream from sync to async and parallel__