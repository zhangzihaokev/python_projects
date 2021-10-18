# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:10:49 2016

@author: kevinzhang
"""
#CSE 231 section 730, 06/12/2016
def get_input_descriptor():
    file_name = input('Select a file: ')#prompts user to enter a file
    while file_name != 'GOOG.txt' and file_name != 'APPL.txt' and file_name != 'INTC.txt' and file_name != 'MSFT.txt':
        file_name = input('Invalid, try again: ')
    fp = open(file_name, 'r') #open user selected file
    return fp

def get_data_list(fp, c):
    result = []  
    for line in fp:
        line = line.strip()
        line_1st = line.split(',') #reads each line and turns the string into list on comma
        data = line_1st[c] #isolates the desired column
        tups = (line_1st[0], data) #creats a tuple with the date and column data
        result.append(tups) #creates a list of tuples 
    return result

def average_data(list_of_tuples):
    current_month = '' #keeps track of which month it is
    new_list = []
    count_jun = 0 #counts the days in each month
    count_jul = 0
    count_aug = 0
    count_sep = 0
    count_oct = 0
    count_nov = 0
    count_dec = 0
    count_jan = 0
    count_feb = 0
    count_mar = 0
    count_apr = 0
    count_may = 0
    data_sum_jun = 0 #sums the data of each month
    data_sum_jul = 0
    data_sum_aug = 0
    data_sum_sep = 0
    data_sum_oct = 0
    data_sum_nov = 0
    data_sum_dec = 0
    data_sum_jan = 0
    data_sum_feb = 0
    data_sum_mar = 0
    data_sum_apr = 0
    data_sum_may = 0
    for i in list_of_tuples:
        date = i[0]
        dat = i[1]
        if date[4:6] == '06': #checks each string in the tuple for the date
            current_month = 'June 2014'
            j = float(dat)
            count_jun += 1 #adds a day 
            data_sum_jun += j #adds a data entry
            avg_jun = data_sum_jun/count_jun #averages the data
            jun_data = (avg_jun, current_month) #creates a tuple with the average and date
        if date[4:6] == '07':
            current_month = 'July 2014'
            j = float(dat)
            count_jul += 1
            data_sum_jul += j
            avg_jul = data_sum_jul/count_jul
            jul_data = (avg_jul, current_month)
        if date[4:6] == '08':
            current_month = 'August 2014'
            j = float(dat)
            count_aug += 1
            data_sum_aug += j
            avg_aug = data_sum_aug/count_aug
            aug_data = (avg_aug, current_month)
        if date[4:6] == '09':
            current_month = 'September 2014'
            j = float(dat)
            count_sep += 1
            data_sum_sep += j
            avg_sep = data_sum_sep/count_sep
            sep_data = (avg_sep, current_month)
        if date[4:6] == '10':
            current_month = 'October 2014'
            j = float(dat)
            count_oct += 1
            data_sum_oct += j
            avg_oct = data_sum_oct/count_oct
            oct_data = (avg_oct, current_month)
        if date[4:6] == '11':
            current_month = 'November 2014'
            j = float(dat)
            count_nov += 1
            data_sum_nov += j
            avg_nov = data_sum_nov/count_nov
            nov_data = (avg_nov, current_month)
        if date[4:6] == '12':
            current_month = 'December 2014'
            j = float(dat)
            count_dec += 1
            data_sum_dec += j
            avg_dec = data_sum_dec/count_dec
            dec_data = (avg_dec, current_month)
        if date[4:6] == '01':
            current_month = 'January 2015'
            j = float(dat)
            count_jan += 1
            data_sum_jan += j
            avg_jan = data_sum_jan/count_jan
            jan_data = (avg_jan, current_month)
        if date[4:6] == '02':
            current_month = 'February 2015'
            j = float(dat)
            count_feb += 1
            data_sum_feb += j
            avg_feb = data_sum_feb/count_feb
            feb_data = (avg_feb, current_month) 
        if date[4:6] == '03':
            current_month = 'March 2015'
            j = float(dat)
            count_mar += 1
            data_sum_mar += j
            avg_mar = data_sum_mar/count_mar
            mar_data = (avg_mar, current_month)
        if date[4:6] == '04':
            current_month = 'April 2015'
            j = float(dat)
            count_apr += 1
            data_sum_apr += j
            avg_apr = data_sum_apr/count_apr
            apr_data = (avg_apr, current_month)      
        if date[4:6] == '05':
            current_month = 'May 2015'
            j = float(dat)
            count_may += 1
            data_sum_may += j
            avg_may = data_sum_may/count_may
            may_data = (avg_may, current_month)
    month_data = [jun_data, jul_data, aug_data, sep_data, oct_data, nov_data,\
    dec_data, jan_data, feb_data, mar_data, apr_data, may_data]
    new_list.append(month_data) #creates a list of average/date tuples
    return new_list[0]
    
def main():
    fp2 = get_input_descriptor() #calls get_input_descriptor
    col = int(input('Select a column: ')) #prompts user to select a colmun
    r = get_data_list(fp2, col)
    avg_list = average_data(r) #calls average_data
    print('\n Lowest 6 for column', col)
    for i in sorted(avg_list)[0:6]: #sorts and prints the first 6 rows of data (lowest)
        print('Date: ', '{:>15}'.format(i[1]), 'Value: ', '{:>.2f}'.format(i[0]))
    print('\n Highest 6 for column', col)
    for i in sorted(avg_list)[6:]: #sorts and prints the last 6 rows of data (highest)
        print('Date: ', '{:>15}'.format(i[1]), 'Value: ', '{:>.2f}'.format(i[0]))
    fp2.close()
main() #calls main