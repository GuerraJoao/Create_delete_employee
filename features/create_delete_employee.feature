Feature: Creating and deleting employee

  Scenario Outline: Create and delete employee
      Given we create an employee with id "<id>" and name "<name>"
      Given confirm the employee "<id>"
      When we delete employee "<id>"
      Then confirm employee "<id>" does not exist

   Examples: Employees
   | id   | name |
   | 3344 | Joao |

