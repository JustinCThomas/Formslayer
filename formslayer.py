# This only works with Python 2
# Make sure to run "pip install mechanize" beforehand (with Python 2, not Python 3)
# import requests
import mechanize
from datetime import datetime
from random import choice

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeSc3sQ9_a8ICZXwJSeS1g29fQrlCTf5LDGvFTREXH6B0MIJg/viewform'

br = mechanize.Browser()

br.set_handle_robots(False)

br.addheaders = [("User-agent", "Mozilla/5.0")]

specific_form = br.open(form_url)

br.select_form(nr=0)

br.set_all_readonly(False)

mappings = {
    "first_name": "entry.1671884016",
    "last_name": "entry.388598124",
    "month": "entry.598128291_month",
    "day": "entry.598128291_day",
    "year": "entry.598128291_year",
    "course": "entry.474587928",
    "proud_of": "entry.1042773410",
    "how_challenged": "entry.1430770718",
    "skills_new_content": "entry.1137064007",
    "build_today": "entry.500130670",
    "build_tomorrow": "entry.1395423839",
    "improve_experience": "entry.856919328",
    "class_content_today": "entry.1611087871",
    "explain1": "entry.327698884",
    "teach_performance_today": "entry.303626407",
    "explain2": "entry.350438882",
}

fname = raw_input("Please enter your first name: ")
lname = raw_input("Please enter your last name: ")


proud_of_today_responses = [
    "I contributed to class discussion today.",
    "I helped others out with their code.",
    "I made progress on my personal project."
]

how_challenged_today_responses = [
    "The project in the presentation took a long time to understand.",
    "My Python installation kept crashing.",
    "I am still confused about Data Frames.",
    "It was difficult to visualize the instructor's explanations.",
    "I could not type fast enough to keep up."
]

what_skills_learn_responses = [
    "I learned interesting things about Python today.",
    "I developed my Project Management skills.",
    "I learned about the Pandas module.",
    "I can now web scrape websites.",
    "I learned how to use an API."
]

what_build_today_responses = [
    "I didn't build anything today.",
    "We didn't build anything today.",
    "I built a cool Python program.",
    "I built a mini application."
]


what_build_tomorrow_responses = [
    "I'm not sure.",
    "More problems with functions.",
    "I will work on building classes tomorrow.",
    "I will work on my group project tomorrow.",
    "Tomorrow I will make more progress on my personal project."
]

how_improve_experience = [
    "Have snacks every day.",
    "Get more surge protectors.",
    "Get longer surge protectors.",
    "Make the code available online. I type very slowly."
]

satisfied_today_content_responses = [
    "The slides were very easy to follow.",
    "The presentation was very good today."
    "The presentation was good.",
    "The class content today was very helpful.",
    "I learned a lot from the presentation.",
    "I am satisfied with today's class content. It was useful.",
    "The slides were very useful today."
]

satisfied_today_teaching_responses = [
    "The teaching was quite insightful today.",
    "The explanations from the teacher helped me understand the lesson.",
    "The teaching was very good today.",
    "The teaching was good.",
    "I am satisfied with the instructor's performance."
]

br[mappings["first_name"]] = fname
br[mappings["last_name"]] = lname
br[mappings["month"]] = str(datetime.now().month)
br[mappings["day"]] = str(datetime.now().day)
br[mappings["year"]] = str(datetime.now().year)
br[mappings["course"]] = "Python 3"
br[mappings["proud_of"]] = choice(proud_of_today_responses)
br[mappings["how_challenged"]] = choice(how_challenged_today_responses)
br[mappings["skills_new_content"]] = choice(what_skills_learn_responses)
br[mappings["build_today"]] = choice(what_build_today_responses)
br[mappings["build_tomorrow"]] = choice(what_build_tomorrow_responses)
# It is not necessary to provide feedback for how to improve the student experience.
# It is optional
# br[mappings["improve_experience"]] = choice(how_improve_experience)
br[mappings["class_content_today"]] = "5"
br[mappings["explain1"]] = choice(satisfied_today_content_responses)
br[mappings["teach_performance_today"]] = "5"
br[mappings["explain2"]] = choice(satisfied_today_teaching_responses)
print(br)


submit_form = br.submit()
