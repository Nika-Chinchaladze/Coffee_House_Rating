import csv


class ReadCSV:
    def __init__(self):
        self.file_name = "csv/cafe-data.csv"

    def read_csv(self):
        with open(self.file_name, mode="r", newline="", encoding="utf-8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            list_data = [row for row in csv_data]
            csv_file.close()
        return list_data

    def append_csv(self, new_data):
        with open(self.file_name, mode="a", newline="", encoding="utf-8") as csv_file:
            writer_tool = csv.writer(csv_file)
            writer_tool.writerow(new_data)
            csv_file.close()
        return "done"
