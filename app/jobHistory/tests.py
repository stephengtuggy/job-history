from django.test import TestCase
from .models import Employer, Position, JobTimePeriod

# Create your tests here.
class EmployerTestCase(TestCase):
    def setUp(self):
        pass

    def test_creating_an_employer(self):
        Employer.objects.create(short_name="Employer1", long_name="Employer 1")

    def test_creating_positions(self):
        Employer.objects.create(short_name="Employer2", long_name="Employer 2")
        emp = Employer.objects.get(short_name="Employer2")
        Position.objects.create(employer=emp, title="Position 1", supervisor_given_name="John", supervisor_surname="Doe", can_contact=True)
        Position.objects.create(employer=emp, title="Position 2", supervisor_given_name="Jane", supervisor_surname="Doe", can_contact=False)

    def test_creating_job_time_periods(self):
        Employer.objects.create(short_name="Employer3", long_name="Employer 3")
        emp = Employer.objects.get(short_name="Employer3")
        Position.objects.create(employer=emp, title="Position 3", supervisor_given_name="John", supervisor_surname="Doe", can_contact=True)
        Position.objects.create(employer=emp, title="Position 4", supervisor_given_name="Jane", supervisor_surname="Doe", can_contact=False)
        position3 = Position.objects.get(employer=emp, title="Position 3")
        position4 = Position.objects.get(employer=emp, title="Position 4")
        JobTimePeriod.objects.create(position=position3, start_year=2000, is_current_position=False, end_year=2005, starting_pay="$10.00/hour", ending_pay="$11.00/hour")
        JobTimePeriod.objects.create(position=position3, start_year=2005, is_current_position=False, end_year=2010, starting_pay="$12.00/hour", ending_pay="$13.00/hour")
        JobTimePeriod.objects.create(position=position3, start_year=2010, is_current_position=False, end_year=2015, starting_pay="$14.00/hour", ending_pay="$15.00/hour")
        JobTimePeriod.objects.create(position=position3, start_year=2015, is_current_position=True, starting_pay="$16.00/hour", ending_pay="$17.00/hour")


