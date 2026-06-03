import mysql.connector


def get_database_connection():

    connection = mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user='2yph7AKej7jSxjq.root',
        password='LNcHVPggDico6rAf',
        database='student_task_manager01',
        port = 4000
    )

    return connection