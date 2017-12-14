from django.db import models

from collections import Counter
import csv
import random


# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        unique_together = ['name', 'number']

    def __str__(self):
        return "PLAN {}: {}".format(self.number, self.name)

    @classmethod
    def _load_plans(cls, plan_file="data/plans.csv"):
        """
        Creates and Saves Plans to DB from CSV file
        DB is already loaded so you can ignore this.
        """
        with open(plan_file, "r") as f:
            plan_csv = csv.reader(f)
            for row in plan_csv:
                plan = cls(
                    name=row[1].strip(),
                    number=row[0].strip()
                )
                plan.save()

    @classmethod
    def find_plan(cls, input):
        """
        Implement method that takes an input string parses it and finds
        matching a Plan(s) and returns a Tuple of the Plan(s) and a
        Confidence Rating:
        4 - Exact Match (Plan Name/Plan Number both Match)
        3 - Probably Match (Plan Name or Plan Number Match)
        2 - Partial Match (Distance or other Algo Match)
        1 - Multiple Partial Matches (Distance or other Algo Match)
        0 - No Matches Found (Nothing even close)

        Examples:
        return (match, 4)
        return (match, 3)
        return (match, 2)
        return (matches, 1)
        return (None, 0)
        """
        return ("Test", random.randint(0, 4))

    @classmethod
    def test_find_plan(cls, inputs="data/inputs.csv"):
        """
        Tests how many matches we can find with current implementation.
        """
        confidence_levels = []
        with open(inputs, "r") as f:
            input_file = csv.reader(f)
            for row in input_file:
                match, confidence = cls.find_plan(row[0].strip())
                confidence_levels.append(confidence)
                if confidence == 0:
                    print("No Match for {}".format(row[0]))
                elif confidence == 1:
                    print("Multiple matches for {}".format(row[0]))
                else:
                    print("{} matched with {}".format(row[0], match))

        match_confidence = Counter(confidence_levels)
        print()
        print()
        print("Level 4 Matches: ", match_confidence[4])
        print("Level 3 Matches: ", match_confidence[3])
        print("Level 2 Matches: ", match_confidence[2])
        print("Level 1 Matches: ", match_confidence[1])
        print("No Match: ", match_confidence[0])
