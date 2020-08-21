from django.test import TestCase
from django.db import IntegrityError
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

    def test_creating_duplicate_employers(self):
        Employer.objects.create(short_name="Employer4", long_name="Employer 4")
        with self.assertRaises(IntegrityError):
            Employer.objects.create(short_name="Employer4", long_name="Employer 4")

    def test_creating_duplicate_positions(self):
        Employer.objects.create(short_name="Employer5", long_name="Employer 5")
        emp = Employer.objects.get(short_name="Employer5")
        Position.objects.create(employer=emp, title="Position 5", supervisor_given_name="John", supervisor_surname="Doe", can_contact=True)
        with self.assertRaises(IntegrityError):
            Position.objects.create(employer=emp, title="Position 5", supervisor_given_name="Jane", supervisor_surname="Doe", can_contact=False)

    def test_creating_duplicate_job_time_periods_A(self):
        Employer.objects.create(short_name="Employer6", long_name="Employer 6")
        emp = Employer.objects.get(short_name="Employer6")
        Position.objects.create(employer=emp, title="Position 6", supervisor_given_name="Billy Joe", supervisor_surname="Jim Bob", can_contact=True)
        position = Position.objects.get(employer=emp, title="Position 6")
        JobTimePeriod.objects.create(position=position, start_year=2000, start_month=1, start_day=1, is_current_position=True, starting_pay="$10.00/hour", ending_pay="$17.00/hour")
        with self.assertRaises(IntegrityError):
            JobTimePeriod.objects.create(position=position, start_year=2000, start_month=1, start_day=1, is_current_position=True, starting_pay="$10.00/hour", ending_pay="$17.00/hour")

    def test_creating_duplicate_job_time_periods_B(self):
        Employer.objects.create(short_name="Employer7", long_name="Employer 7")
        emp = Employer.objects.get(short_name="Employer7")
        Position.objects.create(employer=emp, title="Position 7", supervisor_given_name="Billy Joe", supervisor_surname="Jim Bob", can_contact=True)
        position = Position.objects.get(employer=emp, title="Position 7")
        JobTimePeriod.objects.create(position=position, start_year=2000, start_month=1, start_day=1, is_current_position=False, end_year=2019, end_month=12, end_day=31, starting_pay="$10.00/hour", ending_pay="$17.00/hour")
        with self.assertRaises(IntegrityError):
            JobTimePeriod.objects.create(position=position, start_year=2000, start_month=1, start_day=1, is_current_position=False, end_year=2019, end_month=12, end_day=31, starting_pay="$10.00/hour", ending_pay="$17.00/hour")


