from solution import crawler
import os


if __name__ == "__main__":
    # loop thru files from the same derictory
    for i in os.listdir():
        if '.html' in i:
            print(i)

    def ChooseFile():
        # enter the file name if it is in the same directory if not enter the path
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
