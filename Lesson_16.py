class Manager:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

class Developer:
    def __init__(self, name, salary, programming_language):
        self.name = name
        self.salary = salary
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)  # Ініціалізація Manager
        Developer.__init__(self, name, salary, programming_language)  # Ініціалізація Developer
        self.team_size = team_size  # Додатковий атрибут для TeamLead






# НАПИСАННЯ ТЕСТУ
import unittest
from Hillel_sckool.homework_16.Lesson_16 import Manager, Developer, TeamLead


class TestEmployeeClasses(unittest.TestCase):

    def test_manager_creation(self):
        manager = Manager("Alice", 7000, "HR")
        self.assertEqual(manager.name, "Alice")
        self.assertEqual(manager.salary, 7000)
        self.assertEqual(manager.department, "HR")

    def test_developer_creation(self):
        developer = Developer("Misha", 15000, "Python")
        self.assertEqual(developer.name, "Misha")
        self.assertEqual(developer.salary, 15000)
        self.assertEqual(developer.programming_language, "Python")

    def test_tealead_creation(self):
        teamlead = TeamLead("Dima", 3000, "IT", "Java", 10)
        self.assertEqual(teamlead.name, "Dima")  # Замінили на правильне ім'я
        self.assertEqual(teamlead.salary, 3000)
        self.assertEqual(teamlead.department, "IT")
        self.assertEqual(teamlead.programming_language, "Java")
        self.assertEqual(teamlead.team_size, 10)

if __name__ == "__main__":
    unittest.main()