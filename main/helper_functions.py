from datetime import date


def valid_adult(dob):
    today = str(date.today())
    student_dob_year = int(dob[:4])
    student_dob_month = int(dob[5:7])
    student_dob_date = int(dob[8:])
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_date = int(today[8:])
    is_valid = False
    if (today_year - 18 > student_dob_year) or (
        (today_year - 18 == student_dob_year)
        and (
            (today_month > student_dob_month)
            or ((today_month == student_dob_month) and (today_date >= student_dob_date))
        )
    ):
        is_valid = True
    return is_valid
