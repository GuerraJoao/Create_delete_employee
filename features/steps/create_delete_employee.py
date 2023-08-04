from behave import *
from utils import *


@given('we create an employee with id "{employee_id}" and name "{employee_name}"')
def step_impl(context, employee_id, employee_name):
    response = create_employee(employee_id, employee_name)
    validate_response(response, 'add')


@given('confirm the employee "{employee_id}"')
def step_impl(context, employee_id):
    response = fetch_employee(employee_id)
    response = validate_response(response, 'fetch')
    assert response.parsed_text['data'] is not None


@when('we delete employee "{employee_id}"')
def step_impl(context, employee_id):
    response = delete_employee(employee_id)
    validate_response(response, 'delete')


@then('confirm employee "{employee_id}" does not exist')
def step_impl(context, employee_id):
    response = fetch_employee(employee_id)
    response = validate_response(response, 'fetch')
    assert response.parsed_text['data'] is None
