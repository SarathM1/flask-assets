from models import db, Asset
import random
from faker import Factory
import datetime
fake = Factory.create()
# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake Entries

choice_list = {
        'location' = ['neyyar', 'leela', 'gayathri'],
        'processor' = ['i3', 'i5', 'i7'],
        'ram' = ['4', '8', '16'],
        'project_name' = ['tag', 'trc', 'delphi', 'hils']
        }

def random_alphanumeric(length):
    temp = ''.join(random.choice('0123456789ABCDEF') for i in range(length=5))
    return temp

def random_date(start_date='today', end_date='+1y'):
    # start_date = datetime.date(year=2015, month=1, day=1)
    temp = fake.date_between(start_date=start_date, end_date=end_date)
    return temp

for num in range(100):
    fullname = fake.name().split()
    name = fullname[0]
    name = random.

    emp_no = random.randint(1000, 2000)
    location = random.choice(choice_list['location'])
    seat_no = random.randint(100,200)
    sl_no_1 = random.randint(100,200)
    model = random_alphanumeric(5)
    make = random_alphanumeric(5)
    tel_tvm = random_alphanumeric(5)
    test_pc = random_alphanumeric(5)
    processor = random.choice(choice_list['processor'])
    ram = random.choice(choice_list['ram'])
    hdd = random.choice(choice_list['hdd'])
    asset_no = random_alphanumeric()
    allocation_date = random_date()
    project_name = random.choice(choice_list['project_name'])
    won_no = random.randint(1000,2000)
    end_date = random_date(start_date=allocation_date, end_date='+1y')
    # Save in database
    row_data = Asset(emp_no = emp_no,
            location = location,
            seat_no = seat_no,
            sl_no_1 = sl_no_1,
            model = model,
            make = make,
            tel_tvm = tel_tvm,
            test_pc = test_pc,
            processor = processor,
            ram = ram,
            hdd = hdd,
            asset_no = asset_no,
            allocation_date = allocation_date,
            project_name = project_name,
            won_no = won_no,
            end_date = end_date )
    db.session.add(row_data)

db.session.commit()
