import json
import pandas as pd

class DataCO2:

    def __init__(self, country_name, country_code, year, co2_number):
        self.__country_name = country_name
        self.__country_code = country_code
        self.__year = year
        self.__co2_number = co2_number

    def __get__(self, instance, owner):
        instance.country_name = self.__country_name
        instance.country_code = self.__country_code
        instance.years = self.__year
        instance.co2_number = self.__co2_number
        return instance

    def check_null(self):
        if self.__co2_number:
            # self.save()
            pass


class ExcelFile:
    START_YEAR = 1960
    END_YEAR = 2014

    def __init__(self, dir_excel):
        self.dir_excel = dir_excel

    def open_file(self):
        excel_file = pd.ExcelFile(self.dir_excel)
        data = excel_file.parse('Data', index=False)
        return data

    def get_all_country_name(self):
        data = self.open_file()
        list_country = []
        for row_dict in data.to_dict(orient='records'):
            list_country.append(row_dict['Country Name'])
        return list_country

    def handl(self):
        data = self.open_file()
        start_year = self.START_YEAR
        end_year = self.END_YEAR
        datas = []
        for row_dict in data.to_dict(orient='records'):
            for years in range(start_year, end_year, 1):
                default_dict_data = {
                    'country_name': row_dict['Country Name'],
                    'country_code': row_dict['Country Code'],
                    'year': start_year,
                    'co2_number': row_dict['{}'.format(start_year)],
                }
                datas.append(default_dict_data)
                start_year += 1 if start_year != end_year else end_year
                if start_year == end_year:
                    start_year = 1960
                    break
        return datas

    def get_year(self):
        years = []
        for year in range(self.START_YEAR,self.END_YEAR,1):
            years.append(year)
        return years

abc = ExcelFile('API_EN.ATM.CO2E.PC_DS2_en_excel_v2_10134430.xls')
# for i in abc.handl():
#     print(type(i))
