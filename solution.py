from bs4 import BeautifulSoup 
import json
import os 


class crawler:
    def __init__(self,Htmlfile):
        self.type = "html_file"
        self.Data = []
        self.HtmlFile = Htmlfile
        self.index = {
            'Hname':'Hotel Name',
            'Hadd':'Hotel Addresse',
            'Hsummary':'Hotel Summary Array',
            'HsummaryText':'Hotel Summary as Text',
            'Htype':'Room categories array',
            'RoomCat':'Room categories',
            'Ahotel':'Alternative hotels',
            'Hstars':'Hotel Rating stars',
            'HreviewPts':'Hotel Review points'
        }
        self.dom = self.getDom()
    # getDom function grab the html from html file or website depending on the type
    def getDom(self):
        if self.type == 'html_file':
            with open(self.HtmlFile,encoding="utf8") as file:
                soup = BeautifulSoup(file,'lxml')
        return soup
    def Test(self):
        print(self.dom.title)
        return 1
    def getHeaderData(self):
        try:
            self.Hname = self.dom.find(id="hp_hotel_name").get_text().strip()
            self.Hadd = self.dom.find(id="hp_address_subtitle").get_text().strip()
            self.itemHeader= self.dom.select('h1.item')[0]
            self.Itag = self.itemHeader.find_all('i')[0]
            self.Hstars = self.Itag['class'][2].split('_')[2]
            self.Rpts = self.dom.select('span.js--hp-scorecard-scoreval')[0].get_text()
            return 1
        except:
            return print('Error in the Header Part !')
            return 0
    def getBodyData(self):
        try:
            #code goes here
            self.Hsummary = self.dom.find(id="summary")
            self.HsummaryText = ''
            for i in self.Hsummary.find_all('p'):
                self.HsummaryText = self.HsummaryText + str(i.get_text())
            return 1
        except:
            print('Error in the Body Part ! ')
            return 0
    def getBodyfooter(self):
        try:
            self.Htype = self.dom.find_all(attrs="ftd")
            self.HtypeArray = []
            for i in self.Htype:
                self.HtypeArray.append(i.get_text().strip())
            return 1
        except:
            print('Error in the RC !')
            return 0
    def getFooter(self):
        try:
            self.FooterData = self.dom.find_all(attrs='althotel_link')
            self.FooterDataText = []
            for i in self.FooterData:
                self.FooterDataText.append(i.get_text().strip())
            return 1
        except:
            print('Error in the Footer !')
            return 0
    def DumpData(self):
        try:
            self.Data.append({'Hname':self.Hname,'Haddresse':self.Hadd,'Hstars':self.Hstars,'HreviewPts':self.Rpts,'description':self.HsummaryText,'roomcat':self.HtypeArray,'Ahotel':self.FooterDataText})
        except:
            print('Error in The dump !')
            return 0 
    def DisplayData(self):
        return self.Data
    def DumptoJson(self,new_data, filename='data.json'):
        try:
            with open(filename,'r+') as file:
                file_data = json.load(file)
                file_data.append(new_data)
                file.seek(0)
                json.dump(file_data, file)
                print('Data been Scraped !')
                input('Press Enter To Exit !')
                return 1
        except:
            try:
                f = open(filename,'w')
                f.write('[]')
                f.close()
                self.DumptoJson(new_data,filename)
            except:
                print('Error Data entery  (DumptoJson Function) !')
                return 0

#loop thru files from the same derictory
for i in os.listdir():
        if '.html' in i:
            print(i)
def ChooseFile():
    #enter the file name if it is in the same directory if not enter the path
    file = input('Enter File name : ')
    if not os.path.isfile(file):
        return ChooseFile()
    if '.html' not in file:
        print('Enter html file !')
        return ChooseFile()
    return file


web = crawler(ChooseFile())
web.getFooter()
web.getBodyfooter()
web.getBodyData()
web.getHeaderData()
web.DumpData()

web.DumptoJson(web.DisplayData()[0])
