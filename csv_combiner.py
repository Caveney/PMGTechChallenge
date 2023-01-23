import pandas as pd
import sys
import os

#takes any number of CSV files
def csvcombiner(args):
    #removes the python program file from the list of csv files
    args.pop(0)
    #checks to make sure files were passed in
    if(len(args) == 0):
        sys.stdout.write("No files detected")
        return("No files detected")

    else:
        list = [None]
        i = 0

        #for each CSV file it turns it into a dataframe and adds a column named
        #filename and inserts filename into each tuple
        for x in args:
            #read file in and turn into dataframes
            df = pd.read_csv(args[i])
            df["filename"] = os.path.basename(x)
            list.append(df)
            i += 1

        #Combines all dataframes together
        concat = pd.concat(list)

        #converts dataframe to a csv 
        concat.to_csv("combined.csv", index=False)
        sys.stdout.write("combined.csv")
        return("combined.csv")



if __name__ == '__main__':
    csvcombiner(sys.argv)