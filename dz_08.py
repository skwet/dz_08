from datetime import datetime,timedelta
from collections import defaultdict

def year_change(text: str):
    bd = datetime.strptime(text, '%d, %m, %Y')
    return bd.replace(year=datetime.now().year).date()
def get_birthday_per_week(users):
    birthday_list = defaultdict(list)
    today = datetime(2023, 3, 20).date()
    start_per = today + timedelta(5)
    end_per =  start_per + timedelta(6)

    for user in users:
        if start_per <= year_change(user['birthday']) <= end_per:
            if year_change(user['birthday']).weekday() in (5,6):
                birthday_list['Monday'].append(user['name'])
            else:
                birthday_list[year_change(user['birthday']).strftime('%A')].append(user['name'])
    return birthday_list

if __name__ == '__main__':
    users = [{'name': 'John','birthday': '25, 3, 2000'},
             {'name': 'Tony','birthday': '26, 3, 2001'},
             {'name': 'Bohdan','birthday': '27, 3, 2002'},
             {'name': 'James','birthday': '28, 3, 2003'},
             {'name': 'Bob','birthday': '29, 3, 2004'},
             {'name': 'Bill','birthday': '30, 3, 2005'},
             {'name': 'Sarah','birthday': '31, 3, 2006'}
    ]
    check = get_birthday_per_week(users)
    print(check)    