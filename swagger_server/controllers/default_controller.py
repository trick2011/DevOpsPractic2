import connexion
import six

import swagger_server.service.student_service as student_service
from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def add_student(body):  # noqa: E501
    """Add a new student

     # noqa: E501

    :param body: Student object that needs to be added
    :type body: dict | bytes

    :rtype: str
    """

    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return student_service.add_student(body)


def delete_student(student_id):  # noqa: E501
    """delete_student

     # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int

    :rtype: Student
    """
    res = student_service.delete_student(student_id)
    if res:
        return res
    return 'Not Found', 404


def get_student_by_id(student_id, subject=None):  # noqa: E501
    """Find student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int
    :param subject: The subject name
    :type subject: str

    :rtype: Student
    """
    res = student_service.get_student_by_id(student_id, subject=subject)
    if res:
        return res
    return 'Not Found', 404


def get_student_by_last_name(last_name=None):  # noqa: E501
    """Find student by Last Name

    Returns a single student # noqa: E501

    :param last_name: Last Name of student to return
    :type last_name: str

    :rtype: Student
    """
    res = student_service.get_student_by_last_name(last_name)
    if res:
        return res
    return 'Not Found', 404
