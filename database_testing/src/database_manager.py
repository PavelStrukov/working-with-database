import mysql.connector


class DatabaseManager:
    """
    DatabaseManager organize the communication with database

        ...

        Attributes
        ----------
        _INSERT_REQUEST_STRING : str
            A string contains a template for insert query
        _SELECT_REQUEST_STRING : str
            A string contains a template for select query
        _UPDATE_REQUEST_STRING : str
            A string contains a template for update query
        _DELETE_REQUEST_STRING : int
            A string contains a template for delete query

        Methods
        -------
        close_connection()
            Closes connection to database

        generate_insert_request(student)
            Generates insert query to add student to a table

        generate_select_request(conditions=None)
            Generates select query to get one or more students from a table

        generate_update_request(update_info, conditions)
            Generates update query to change student's data in a table

        generate_delete_request(condition)
            Generates delete query to remove student from a table

        def send_request(request)
            Sends query to a database
        """

    _INSERT_REQUEST_STRING = "INSERT INTO students (id, name, login, password, group_id) VALUES ({}, {}, {}, {}, {});"
    _SELECT_REQUEST_STRING = "SELECT * FROM students"
    _UPDATE_REQUEST_STRING = "UPDATE students SET {} WHERE {}"
    _DELETE_REQUEST_STRING = "DELETE FROM students WHERE {} = {};"

    def __init__(self, user_data, host, port, database_name=None):

        """Allow to create DatabaseManager instance and create connection

            Parameters
            ----------
            user_data : list
                The login and password of user
            host : str
                The host where the database is located
            database_name : str
                Name of the database"""

        self._user_login = user_data[0]
        self._user_password = user_data[1]

        self._connection = mysql.connector.connect(user=self._user_login, password=self._user_password,
                                                   host=host, port=port)

        if database_name is not None:
            cursor = self._connection.cursor(buffered=True, dictionary=True)
            cursor.execute("CREATE DATABASE IF NOT EXISTS " + str(database_name))

            connection = mysql.connector.connect(user=self._user_login, password=self._user_password,
                                                 host=host, port=port, database=database_name)

            self._connection = connection

    def set_database(self, database):
        self._connection.cmd_init_db(database)

    def close_connection(self):
        self._connection.cursor().close()

    def generate_insert_request(self, student):

        """Generates insert request from the template with data from parameter

            Parameters
            ----------
            student : Student
                The student that should be inserted

            Returns
            -------
            str
                A string with generated SQL query"""

        student_data = [student.id, student.name, student.login, student.password, student.group_id]
        request = self._INSERT_REQUEST_STRING.format(*student_data)
        return request

    def generate_select_request(self, conditions=None):

        """Generates select request from the template with data from parameter
            If conditions is None, method returns the query for selecting all rows

            Parameters
            ----------
            conditions : str, optional (default is None)
                Conditions according to that the student should be selected

            Returns
            -------
            str
                A string with generated SQL query"""

        if conditions is None:
            return self._SELECT_REQUEST_STRING
        else:
            request = self._SELECT_REQUEST_STRING + "  WHERE {}={}"
            request = request.format(*conditions.split("="))
        return request

    def generate_update_request(self, update_info, conditions):

        """Generates update request from the template with data from parameter

            Parameters
            ----------
            update_info: str
                The sting contains fields and new information for them
            conditions : str
                Conditions according to that the student should be selected

            Returns
            -------
            str
                A string with generated SQL query"""

        request = self._UPDATE_REQUEST_STRING.format(*[update_info, conditions])
        return request

    def generate_delete_request(self, condition):

        """Generates delete request from the template with data from parameter

            Parameters
            ----------
            condition : str
                Conditions according to that the student should be deleted

            Returns
            -------
            str
                A string with generated SQL query"""

        request = self._DELETE_REQUEST_STRING.format(*condition.split("="))
        return request

    def send_request(self, request):

        """Organise sending the SQL query

            Parameters
            ----------
            request : str
                Query that should be sent

            Returns
            -------
            str or None
                A string with generated SQL query
                None when the response of execution is empty

            Raises
            ------
            ValueError
                If the SQL query has problems
            InterfaceError
                If the response after execution is empty"""

        cursor = self._connection.cursor(buffered=True, dictionary=True)
        response = cursor.execute(request)
        self._connection.commit()
        if "SELECT" in request or "SHOW" in request:
            response = cursor.fetchall()
        return response
