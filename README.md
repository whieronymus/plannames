## Name Parsing Challenge

### Setup Instructions:
1. Fork and Clone
2. Create and activate Virtual Env
3. `pip install -r requirements.txt`

### Challenge:
In plans.models.Plan update the find_plan classmethod to return valid matches and a confidence level
of the match. (Described in Docstring)

### Testing:
In your terminal:
1. `python manage.py shell`
2. `from plans.models import Plan`
3. To test individual cases call the find_plan method and pass in any case from data/inputs.csv
..* Example: `Plan.find_plan("NEWTON/1462/A")`
4. Finally, test all Cases at once call the test_plan_find method
..* Example: `Plan.test_find_plan()`
