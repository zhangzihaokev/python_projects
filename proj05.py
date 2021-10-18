#CSE 231 online section 730, 06/19/2016



fpres = open_pres()
fp_priv = open_priv()
fp_govt = open_govt()  

# The lists dem and rep will show the years in which each respective party is 
# in power. Their lengths are also used to calculate the democrat and republican 
# monthly averages. 
dem = [] 
rep = []
pres_dict = {} #This dictionary holds the presidents and the years they were in office
for line in fpres:
    line1 = line.strip().split(',') #Splits full name into three strings
    pres_name = (line1[0]).split()
    pres_year = (line1[-2]).split('-')
    pres_year_int = [int(x) for x in pres_year] 
    pres_dict[pres_name[2]] = [pres_year_int[0], pres_year_int[1] - 1]
    
    if line1[-1] == ' Democrat': #Using the last item in the list to identify dem or rep
        dem_in_power = line1[-2].split('-')
        j = [int(x) for x in dem_in_power]
        k = j[0]
        while k < j[1]: #Counts every year from start to end of presidency
            k += 1
            dem.append(k-1) #Omits the last year of the presidency
    else:
        rep_in_power = line1[-2].split('-')
        j = [int(x) for x in rep_in_power]
        i = j[0]
        while i < j[1]:
            i += 1
            rep.append(i-1)


y = []
for line_p in fp_priv:
    line1_p = line_p.strip().split(',')
    line1_int_p = [int(x) for x in line1_p] #Turn string values into integers
    y.append(line1_int_p)     
pres_priv = {}  #This dictionary has the president's name as key and first and last month data as values
for key,value in pres_dict.items(): #From the dictionary generated above
    for j in y:
        if value[0] == j[0]: #Matches the first year of presidency to the year in data set
            first_month_p = j[1] #Sets the first month data of that first year
        if value[1] == j[0]: #Matches the last year of presidency to the year in data set
            last_month_p = j[-1] #Sets the last month data of the last year
    pres_priv[key] = [first_month_p, last_month_p] 
#Exact same as above only with government data
v = []
for line_g in fp_govt:
    line1_g = line_g.strip().split(',')
    line1_int_g = [int(x) for x in line1_g]
    v.append(line1_int_g)     
pres_govt = {}  
for key,value in pres_dict.items():
    for j in v:
        if value[0] == j[0]:
            first_month_g = j[1]
        if value[1] == j[0]:
            last_month_g = j[-1]
    pres_govt[key] = [first_month_g, last_month_g]




            
          
D_priv = {} #Dictionary that has the year as key and list of data as value
D_govt = {}
for line in fp_priv:
    line_1 = line.strip().split(',')
    date = line_1[0] #Isolates the year
    D_priv[date] = line_1[1:] #Creates the dictionary
    priv_data_tup = sorted(D_priv.items()) #Creates a tuple with year and data
for line in fp_govt:
    line_2 = line.strip().split(',')
    date = line_2[0]
    D_govt[date] = line_2[1:]
    govt_data_tup = sorted(D_govt.items())
   

dem_priv_tot = 0 #Counts the total private employment in dem and rep years
rep_priv_tot = 0
for tups in priv_data_tup:
    if int(tups[0]) in dem: #Check to see if it's dem year or rep year
        priv_data_int = [int(x) for x in tups[1]]
        dem_priv_avg = sum(priv_data_int)/len(tups[1]) #Averages for a particular year
        dem_priv_tot += dem_priv_avg #Adds the previous average to the total
    if int(tups[0]) in rep: 
        priv_data_int = [int(x) for x in tups[1]]
        rep_priv_avg = sum(priv_data_int)/len(tups[1])
        rep_priv_tot += rep_priv_avg
dem_govt_tot = 0
rep_govt_tot = 0
for tups in govt_data_tup:
    if int(tups[0]) in dem:
        govt_data_int = [int(x) for x in tups[1]]
        dem_govt_avg = sum(govt_data_int)/len(tups[1])
        dem_govt_tot += dem_govt_avg
    if int(tups[0]) in rep:
        govt_data_int = [int(x) for x in tups[1]]
        rep_govt_avg = sum(govt_data_int)/len(tups[1])
        rep_govt_tot += rep_govt_avg
      
avg = average(dem, rep, dem_priv_tot, rep_priv_tot, dem_govt_tot, rep_govt_tot)
table()

def average(dem, rep, dem_priv_tot, rep_priv_tot, dem_govt_tot, rep_govt_tot):
    '''Calculates the average monthly private and government employment by party '''
    try:
        dem_priv_avg = dem_priv_tot/len(dem)
        rep_priv_avg = rep_priv_tot/len(rep)
        dem_govt_avg = dem_govt_tot/len(dem)
        rep_govt_avg = rep_govt_tot/len(rep)
    except ZeroDivisionError:
        dem_priv_avg == 'none'
        rep_priv_avg == 'none'
        dem_govt_avg == 'none'
        rep_govt_avg == 'none'   
    return dem_priv_avg, rep_priv_avg, dem_govt_avg, rep_govt_avg
def table():      
    '''Prints the table with all relevant data'''
    print('Private employment average per month (millions)')
    print('{:16}{:<.0f}'.format('Democratic:', dem_priv_tot/len(dem)))
    print('{:16}{:<.0f}'.format('Republican:', rep_priv_tot/len(rep)))
    print()
    print('Government employment average per month (millions)')
    print('{:16}{:<.0f}'.format('Democratic:', dem_govt_tot/len(dem)))
    print('{:16}{:<.0f}'.format('Republican:', rep_govt_tot/len(rep)))
    print()
    print('Private employment by president (millions)')
    print('{:14}{:16}{:15}{:15}{:15}'.format('President', 'First Month', 'Last Month', 'Difference', 'Percentage'))
    for key,value in pres_priv.items():
        print('{:14}{:<16}{:<15}{:<15}{:<15.1f}'.format(key, value[0], value[1], value[1] - value[0], ((value[1] - value[0])/value[0])*100))
    print() #Previous line will display the first and last month data, difference and percent change
    print('Government employment by president (millions)')
    print('{:14}{:16}{:15}{:15}{:15}'.format('President', 'First Month', 'Last Month', 'Difference', 'Percentage'))
    for key,value in pres_govt.items():
        print('{:14}{:<16}{:<15}{:<15}{:<15.1f}'.format(key, value[0], value[1], value[1] - value[0], ((value[1] - value[0])/value[0])*100))

def open_pres():
    '''Prompts user until presidents file is entered'''
    file = input('Enter presidents file: ')
    while file != 'presidents.txt':
        file = input('Invalid, try again: ')
    fpres = open(file, 'r')
    return fpres
def open_priv():
    '''Prompts user until private employment file is entered'''
    file = input('Enter private employment file: ')
    while file != 'private_employment.txt':
        file = input('Invalid, try again: ')
    fp1 = open(file, 'r')
    with fp1 as f1:
        fp_priv = f1.readlines()[4:-1] #Skips the first 3 lines of file and the last
    return fp_priv
def open_govt():
    '''Prompts user until government employment file is entered'''
    file = input('Enter government employment file: ')
    while file != 'government_employment.txt':
        file = input('Invalid, try again: ')
    fp2 = open(file, 'r')
    with fp2 as f2:
        fp_govt = f2.readlines()[4:-1]
    return fp_govt
    
