class AuthData:
    login_invalid_password={"email":"admin1@gmail.com","password":"invalid_password"}
    login_invalid_email={"email":"invalid@gmail.com","password":"$Student3"}
    login_validation={"email":"student1@gmail.com","password":"$Student1"}
    login_student_workflow1={"email":"student2@gmail.com","password":"$Student2"}
    login_student_workflow2={"email":"student3@gmail.com","password":"$Student3"}
    login_admin_workflow={"password":"$AnAdmin3","email":"admin3@gmail.com"}
    login_missing_email={"password":"$Student3"}
    login_missing_password={"email":"student3@gmail.com"}
    new_student = {
        "name": "studentQ",
        "age": 19,
        "gender": "male",
        "email": "student17@gmail.com",
        "password": "$Student17",
        "cgpa": 8.7
    }

    new_student_signup = {
        "name": "studentR",
        "age": 19,
        "gender": "male",
        "email": "student18@gmail.com",
        "password": "$Student18",
        "cgpa": 8.7
    }

    duplicate_email = {
        "name": "studentU",
        "age": 20,
        "gender": "female",
        "email": "student7@gmail.com",
        "password": "$Student17",
        "cgpa": 9.5
    }

    invalid_email = {
        "name": "studentV",
        "age": 20,
        "gender": "female",
        "email": "student22gmail.com",
        "password": "$Student17",
        "cgpa": 9.5
    }

    invalid_name = {
        "name": "student_W",
        "age": 20,
        "gender": "female",
        "email": "student23@gmail.com",
        "password": "$Student17",
        "cgpa": 9.5
    }

    missing_email = {
        "name": "studentX",
        "age": 20,
        "gender": "female",
        "password": "$Student17",
        "cgpa": 9.5
    }

    missing_password = {
        "name": "studentY",
        "age": 20,
        "gender": "female",
        "email": "student25@gmail.com",
        "cgpa": 9.5
    }
    tokens = {
        "invalid_token": "invalid_token",
        "malformed_token": "malformed_token",
        "expired_token": "expired_token"
    }