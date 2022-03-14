# Report for Module-3 Challenge
# 1.	Overview the task.
This task is about computation of vote results from the US congressional race from Colorado. Although the results can be done using excel, this exercise can be done using Python because it has the power to automate the results.  If this exercise is successful, the codes developed here can be applied not only other Congressional districts but also for US senate seats. The task in this exercise is to report is to report total vote caste, total votes for each county, percentage of votes from each county, county with largest voter turnout, total number of votes for each candidate, the percentage of vote for each candidate, and the winner of the election based on the popular vote. 

### The purpose of the report is
1. 	To write a python code script that generates results (in particular the votes per county and county with largest vote) and print the outcomes in command line
2. To analyze total votes per county and county with largest voter turnout
3. To analyze vote results of each candidate

# 2.	Data and Method of analysis
## 2.1.	Data
 I used a csv data file of three congressional candidates was obtained from Bootcamp for this exercise. 
## 2.2.	Method. 
Python 3.76  is used to generate the county level and candidate level results. The python codes are run in Visual Studio (VS).  Since the script at candidate level were done as practice during the reading of the module and is given as starter code, I will explain here the codes used to generate the county level election results and some changes I made with the given starter code.
The starter code uses the “with open(file_load)” method to open and read the data. When I  run my codes with this method, it gives me error messages despite using the correct indentation and also codes. Thus I replace “with open method” shown in fig-1 shown below by alternative method without using the “with open method” . The alternative method is shown in shown in fig-2.
### Fig-1: “with open” method to open and read data

![fig-1](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/fig-1(with%20open).png)

 ### Fig-2: Alternative method to open and read data
 
 ![fig-2](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/fig-2(alternative%20method).png)
 
 The alternative method requires closing of the data at the end while the “with open approach” does not need close the data. The data can be closed as shown in Fig-3
 ### Fig-3: data closing code with the alternative method.

![fig-3](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/fig-3(close%20data).png)

In what follows, I will explain codes used to obtain total votes for each county, percentage of votes in each county and county with the largest voter turnouts.
To obtain the total votes at each county, we first need to extract the county name from each row using the for loop and list indexing method. And inside the for loop, we will use the if condition and append list method to get list of counties as follows. When using the if condition there should be four-tab space indentation from the “for” loop and also four tab space indentation with in the if-condition.  For example, the if condition should be  in vertical line to the “r” letter in the “row” word in the figure below. 

![fig-4](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/fig-4(couty%20name%5Brow%5D).png)

Once the list of counties is created, we can trac the county votes by first setting the values in the county votes dictionary with a zero value.  Then we can increase the values by one for each row using the for loop using “county_votes[county_name] +=1” code as shown in the fig below. Because this must be done for every loop, it should be outside the if-condition but within the for loop.

![figure-5](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/Fig-5(append).png)

To get the county votes and county vote percentages, we have to use for loop to get county from the county dictionary as follows

![fig-6](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/fig-6%20county%20votes%20and%20percent.png)

Within the above for loop, we use the   if statement to get the county with largest voter turnout. The following code is used to determine the winning county.

![fig-7](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/fig-7%20winning%20county.png)

The results were in a text file by first creating a file path variable, open the file and write on it using the write method show below. Again here, the with open method is not used.   

![fig-8](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/fig-8%20file%20to%20save.png)

![fig-9](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/fig-10%20file%20open(write).png)

# 3.	Result 
## 3.1.	Total votes, County Votes, Percentage of county votes and County with largest voter turnout 
##### Total Vote
- Total vote:369,711
##### County vote count 
- Jefferson: 38855 
- 	Denver: 306,055 
- 	Arapahoe:   24,80
###### County vote  percentage
- Jefferson: 10.5%(
- Denver: 82.8% 
- Arapahoe: 6.7%
###### County with largest voter turnout
•	 Denver: 82.8%(306,055 votes),  



## 3.2.	Individual Candidate vote count, percentage each candidates vote and winner of the vote
- 	Name of candidates: Charles Casper Stockham, Diana Degettee, Raymon Anthony Doane
##### Candidate vote count 
- 	Charles Casper Stockham: 85,213 
- Diana Degettee:272,892
- Raymon Anthony Doane,11,606
##### Candidate vote percentage
- Charles Casper Stockham: 23.1%
-	Diana Degettee:73.8%
- Raymon Anthony Doane:3.1%
##### Winner of the vote
-	Candidate name: Diana Degettee
-	Vote count: 272,892
- Vote percentage: :73.8%
# 4.	Election-Audit Summary
The county and individual candidate vote results are shown in the Fig-4 below. The total votes from the three counties is 369,711. Off which,10.5%(38855 votes), 82.8%(306,055 votes),  and 6.7% (24,801) of the votes are from Jefferson, Denver, and Arapahoe counties, respectively. Denver is the county with the largest (82.8%) voter turnout and Arapahoe is the least (6.7%).


In terms of individual candidates, there were three candidates (Charles Casper Stockham, Diana Degettee, Raymon Anthony Doane) in the three counties. Charles Casper Stockham got 23.1% (85,213) of the total votes from the three counties, Diana Degettee got 73.8%(272,892) of the total votes, and Raymon Anthony Doane got 3.1%(11,606) of the total votes. From these individual candidates, we can see that based on the popular vote, Diana Degettee got who got 73.8% of the votes in the three states is the winner of the Congressional race in the three counties of the state of Colorado. 
As stated in section-1(overview of the project), one of the advantages of using the python is that it can automates the results and the codes can be applied to other elections such as US Senate election without making major change in the codes written above. 
Fig-4: Election vote results

![fig-10](https://github.com/nebil2016/Election_Analysis1/blob/main/Resources/fig-11%20election%20results.png)

