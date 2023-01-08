import csv
import xml.dom.minidom as xml


class xmlParser:
    def __init__(self, xmlFileName, excelFileName):
        self.__xmlFileName = xmlFileName
        self.__xml = None
        self.__readXML()
        self.createExcelFile(excelFileName)

    def __readXML(self):
        try:
            self.__xml = xml.parse(self.__xmlFileName).documentElement
            print(f"{self.__xmlFileName} parsed successfully\n")
        except Exception as error:
            print(f"Something went wrong while trying to parse xml file {self.__xmlFileName}\n"
                  f"Error: {error}\n")
            exit(-1)

    @staticmethod
    def sanitizeField(string):
        return " ".join(line.strip() for line in string.splitlines())

    def createExcelFile(self, excelFileName):
        try:
            with open(excelFileName, 'w', newline='') as excelWorkbook:
                print(f"{excelFileName} created successfully.")
                csvWriter = csv.writer(excelWorkbook)

                csvWriter.writerow(['Book_id', 'Author_Name', 'Title', 'Genre', 'Price', 'Publish_date', 'Description'])

                for book in self.__xml.getElementsByTagName('book'):
                    csvWriter.writerow(
                        [
                            book.getAttribute('id'),
                            self.sanitizeField(book.getElementsByTagName('author')[0].firstChild.data),
                            self.sanitizeField(book.getElementsByTagName('title')[0].firstChild.data),
                            book.getElementsByTagName('genre')[0].firstChild.data,
                            book.getElementsByTagName('price')[0].firstChild.data,
                            book.getElementsByTagName('publish_date')[0].firstChild.data,
                            self.sanitizeField(book.getElementsByTagName('description')[0].firstChild.data)
                        ]
                    )

                print(f"Data successfully written to {excelFileName}.")
        except Exception as error:
            print(f"Something went wrong while trying to open/create a file {excelFileName}."
                  f"\nError: {error}\n")
            exit(-1)


if __name__ == "__main__":
    parser = xmlParser("compiler.xml", "200901013_Assign_03.csv")
