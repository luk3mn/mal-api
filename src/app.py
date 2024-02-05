from utils.processing import Processing


etl = Processing()
data = etl.extract()
print(data)

# with open('./top-anime.csv', 'w') as csv_file:
#     csv_file.write(data)
