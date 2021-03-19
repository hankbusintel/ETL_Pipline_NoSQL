
# Get your current folder and subfolder event data
class getDenomCSV():
      
    def __init__(self):
        self.filepath="/event_data"
        self.file_path_list=[]
        self.full_data_rows_list=[]
        
    def __getFileList(self):
        """
            Create a for loop to create a list of files and collect each filepath
            join the file path and roots with the subdirectories using glob
        """
        import os
        import glob
        filepath = os.getcwd() + self.filepath

        for root, dirs, files in os.walk(filepath):
            self.file_path_list = glob.glob(os.path.join(root,'*'))

        
    def __makeFulldataList(self):
        """
            initiating an empty list of rows that will be generated from each file
            extracting each data row one by one and append it to a list.   
        """
        import csv
       
        self.__getFileList()

        # for every filepath in the file path list 
        for f in self.file_path_list:

        # reading csv file 
            with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
                # creating a csv reader object 
                csvreader = csv.reader(csvfile) 
                next(csvreader)

              
                for line in csvreader:
                    #print(line)
                    self.full_data_rows_list.append(line) 

    def makeFullcsv(self):   
        """
            take data from the list load to a csv file.
        """
        import csv
        self.__makeFulldataList()
        csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
            writer = csv.writer(f, dialect='myDialect')
            writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                        'level','location','sessionId','song','userId'])
            for row in self.full_data_rows_list:
                if (row[0] == ''):
                    continue
                writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))



def main():   
    csv=getDenomCSV()
    csv.filepath="/event_data"
    csv.makeFullcsv()

if __name__ =="main":
	main()