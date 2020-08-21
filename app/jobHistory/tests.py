from django.test import TestCase
from .models import Employer, Position, JobTimePeriod

# Create your tests here.
class EmployerTestCase(TestCase):
    def setUp(self):
        pass

    def test_creating_an_employer(self):
        Employer.objects.create(short_name="Employer1", long_name="Employer 1")

    # def test_creating_positions(self):
    #     Employer.objects.create(short_name="Employer2", long_name="Employer 2")
    #     empID = Employer.objects.get(short_name="Employer2").pk
    #     Position.objects.create(employer=empID, title="Position 1", supervisor_given_name="John", supervisor_surname="Doe", can_contact=True)
    #     Position.objects.create(employer=empID, title="Position 2", supervisor_given_name="Jane", supervisor_surname="Doe", can_contact=False)

    # def test_creating_job_time_periods(self):
    #     Employer.objects.create(short_name="Employer3", long_name="Employer 3")
    #     empID = Employer.objects.get(short_name="Employer3").pk
    #     Position.objects.create(employer=empID, title="Position 3", supervisor_given_name="John", supervisor_surname="Doe", can_contact=True)
    #     Position.objects.create(employer=empID, title="Position 4", supervisor_given_name="Jane", supervisor_surname="Doe", can_contact=False)
    #     position3ID = Position.objects.get()


