import json
import csv
from HTTP_HELPER.http_helper import HttpHelper
from util.utils import SortBy
from model.data_model import random_address_model_from_dict


def write_csv(result):
    try:
        with open('users.csv', 'a') as f:
            writer = csv.writer(f)
            with open('users.csv', 'r') as f:
                if f.readline().__contains__("ID") is False:
                    writer.writerow(
                        ['ID', 'FirstName', 'LastName', 'Username', 'Email', 'Avatar', 'Gender', 'DOB', 'ADDRESS'])
            for user in result:
                writer.writerow(
                    [user.id, user.first_name, user.last_name, user.username, user.email, user.avatar,
                     user.gender,
                     user.date_of_birth, user.address.street_address])
    except FileNotFoundError:
        print("File Not Found")


def main():
    user = HttpHelper.get_user_info(size=3)
    print(user)
    result = random_address_model_from_dict(json.loads(user))
    write_csv(result)


def sort_csv_and_save(sort_by: SortBy):
    try:
        with open("users.csv", "r") as read:
            user_detail = read.readlines()
            csv_reader = csv.reader(user_detail)
            next(csv_reader)
            if sort_by == SortBy.ID:
                sorted_list = sorted(csv_reader, key=lambda x: x[0])
            elif sort_by == SortBy.FIRST_NAME:
                sorted_list = sorted(csv_reader, key=lambda x: x[1])
            elif sort_by == SortBy.LAST_NAME:
                sorted_list = sorted(csv_reader, key=lambda x: x[2])
            elif sort_by == SortBy.USERNAME:
                sorted_list = sorted(csv_reader, key=lambda x: x[3])
            elif sort_by == SortBy.EMAIL:
                sorted_list = sorted(csv_reader, key=lambda x: x[4])
            elif sort_by == SortBy.ADDRESS:
                sorted_list = sorted(csv_reader, key=lambda x: x[8])
            with open("sorted_users.csv", "w") as write:
                writer = csv.writer(write)
                with open('sorted_users.csv', 'r') as f:
                    if f.readline().__contains__("ID") is False:
                        writer.writerow(
                            ['ID', 'FirstName', 'LastName', 'Username', 'Email', 'Avatar', 'Gender', 'DOB', 'ADDRESS'])
                        print(sorted_list)
                        writer.writerows(sorted_list)
    except FileNotFoundError:
        print("File Not Found")


def find_user_by_id(id):
    try:
        with open("users.csv", "r") as read:
            user_detail = read.readlines()
            csv_reader = csv.reader(user_detail)
            for row in csv_reader:
                if row[0] == id:
                    print(row)
                    print({"ID": row[0], "FirstName": row[1], "LastName": row[2], "Username": row[3], "Email": row[4],
                           "Avatar": row[5], "Gender": row[6], "DOB": row[7], "ADDRESS": row[8]})
    except FileNotFoundError:
        print("File Not Found")


if __name__ == '__main__':
    main()
    sort_csv_and_save(sort_by=SortBy.FIRST_NAME)
    find_user_by_id(id="1")
