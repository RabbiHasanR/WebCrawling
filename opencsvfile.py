import csv

file_name='books.csv'
# field_names=['Name','Author','Publisher','Price','Category']
# book1=['Computer Programming Part 1','Tamim Shahriar Subeen','Onnorokom Prokashoni','240.00','Programming']
# book2=['Computer Programming Part 2','Tamim Shahriar Subeen','Dimik Prokashoni','250.00','Programming']
# book3=['Lear Programming with Python','Tamim Shahriar Subeen','Dimik Prokashoni','200.00','Programming']
#
# book_list=[book1,book2,book3]

'''
create books.csv file  
'''
# with open(file_name,'w') as csvf:
#     csv_writer=csv.writer(csvf,delimiter=',',quotechar="\"",quoting=csv.QUOTE_MINIMAL)
#     csv_writer.writerow(field_names)
#     for book in book_list:
#         csv_writer.writerow(book)

'''
create books_list.csv file  
'''
field_names=['Name','Author','Publisher','Price','Category']
book1={"Name":"Computer Programming,Part 1","Author":"Tamim Shahriar Subeen","Publisher":"Onnorokom Prokashoni","Price":"240.00"}
book2={"Name":"Computer Programming,Part 2","Author":"Tamim Shahriar Subeen","Publisher":"Onnorokom Prokashoni","Price":"250.00"}
book3={"Name":"Learn Programming with Python","Author":"Tamim Shahriar Subeen","Publisher":"Onnorokom Prokashoni","Price":"200.00"}

book_list=[book1,book2,book3]
file_name_2='books_list.csv'
with open(file_name_2,'w') as csvf:
    csv_writer=csv.DictWriter(csvf,fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(book_list)