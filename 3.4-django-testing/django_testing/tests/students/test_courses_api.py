import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import *
from django_testing import settings

@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def student_factory():
    def sfactory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return sfactory


@pytest.fixture()
def course_factory():
    def cfactory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return cfactory


@pytest.fixture()
def students(student_factory):
    students = student_factory(_quantity=10)
    students_list = []
    for i in students:
        students_list.append(i.id)
    return students_list


@pytest.mark.django_db
def test_create_course_baker(client, course_factory):
    courses = course_factory()
    response = client.get(f'/api/v1/courses/{courses.id}/')
    assert response.status_code == 200
    data = response.json()
    assert courses.id == data['id']


@pytest.mark.django_db
def test_create_course_list(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    for i, m in enumerate(data):
        assert m['id'] == courses[i].id


@pytest.mark.django_db
def test_create_course_filter_id(client, course_factory):
    courses = course_factory(_quantity=10)
    number = 0

    response = client.get(f'/api/v1/courses/?id={courses[number].id}')

    assert response.status_code == 200
    data = response.json()
    assert data[number]['id'] == courses[number].id


@pytest.mark.django_db
def test_create_course_filter_name(client, course_factory):
    courses = course_factory(_quantity=10)
    number = 0

    response = client.get(f'/api/v1/courses/?name={courses[number].name}')

    assert response.status_code == 200
    data = response.json()
    assert data[number]['name'] == courses[number].name


@pytest.mark.django_db
def test_create_course(client, students):
    count = Course.objects.count()

    response = client.post('/api/v1/courses/', data={'name': 'test', 'students': students})

    assert response.status_code == 201
    assert Course.objects.count() == count+1


@pytest.mark.django_db
def test_patch_course(client, course_factory, students):
    courses = course_factory(_quantity=10)
    json = {
        'name': 'test',
        'students': students
    }
    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data=json)

    assert response.status_code == 200
    response = client.get(f'/api/v1/courses/{courses[0].id}/')
    data = response.json()
    json['id'] = courses[0].id
    assert data == json


@pytest.mark.django_db
def test_delete_course(client, course_factory, students):
    courses = course_factory(_quantity=10)
    count = Course.objects.count()

    response = client.delete(f'/api/v1/courses/{courses[0].id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1


@pytest.mark.django_db
def test_max_student_on_course(client, student_factory):
