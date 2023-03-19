# Find-Most-Accesses-in-Time-Range-Python
We would like to run a giveaway for an arbitrary product in the future. We will do this by specifying a resource in our website and looking at which IP address accessed it the most for a given time period. You can assume that we can associate IP addresses with individuals for this program.

You are asked to parse the logs file given a date and a duration in seconds for a resource and
expected to find the (IP Address, Access Count, First Access Time) tuples for the given time
period in descending access count order. You must ignore requests that don’t make a GET
request to the specified resource. Your program should accept these parameters from the
command line, so invocation of your program will be in the following form.

# Command:
>> python task2.py <date> <duration> <resource>

To calculate the Access Time (in seconds) of the dates in your logs use the following conversion.

Notice that your dates have the DD/MM/YY:hh:mm:ss format.
AccessTime =DD∗86400+MM∗2628288+(YY−1970)∗31536000+hh∗3600+mm∗60+ss

# Example Input:
5.78.198.52 - - [22/Jan/2019:03:56:32 +0330] "GET /games/hollow_knight HTTP/1.1" ...
5.78.198.52 - - [22/Jan/2019:03:56:32 +0330] "GET /games/hollow_knight HTTP/1.1" ...
2.177.12.140 - - [22/Jan/2019:03:57:32 +0330] "GET /image/shiba.jpg HTTP/1.1" ...
2.177.12.140 - - [23/Jan/2019:03:56:31 +0330] "GET /games/hollow_knight HTTP/1.1" ...
2.177.12.140 - - [23/Jan/2019:03:56:32 +0330] "GET /games/hollow_knight HTTP/1.1" ...

# Console Command:
python task2.py 22/Jan/2019:03:56:32 86400 /games/hollow_knight

# Example Output:
5.78.198.52 2 1549807280→AccessTime(22/Jan/2019:03:56:32)
2.177.12.140 1 1549893679→AccessTime(23/Jan/2019:03:56:31)

Notice that last request of 2.177.12.140 is excluded from our list, as:
AccessTime(23/Jan/2019:03:56:32) == AccessTime(22/Jan/2019:03:56:32) + 86400. You should only consider access times that is less than date + duration.
You are ALLOWED to use existing sorting functions and any data structure to keep track of these accesses.
Your python script should have the name task2.py and should read its inputs froma file called log_task2.txt under the same directory and write it’s results to a file called output_task2.txt.
