"""
Andy Asher
01/22/2023
domain: social inequality
A little comrade to help radicalize your coworkers
"""


from dataclasses import dataclass, field

import datetime
from enum import Enum
import random
import statistics as stats


class industry(Enum):
    MANUFACTURING = 1
    ENTERTAINMENT = 2
    RETAIL = 3
    EDUCATION = 4

@dataclass
class PyBuddy:
    """PyBuddy data class for creating a study buddy."""

    # With a data class, we just name each field and provide the type.
    # Include a default value in case something is not provied.
    name: str = "Unknown"
    industry: industry = 1
    num_years: int = 4
    salary: float = 75
    is_available: bool = True
    skill_list: list = field(default_factory=list)
    create_date = datetime.datetime.now()
    member: bool = False
    job_satisfaction: str = "Neither happy nor unhappy"
    coworker_sal_list: list = field(default_factory=list)



    def get_age_string(self):
        """Return a string with our age."""
        return str(datetime.datetime.now() - self.create_date)

    def get_availability_string(self):
        """Return a message based on availability."""
        if self.is_available:
            return "I'm available for tutoring."
        else:
            return "I'm already helping others learn Python."

    def get_skills_string(self):
        """Return a nicely formatted string of skills."""
        # use concise list comprehension syntax
        return "".join([str(f"  - {elem}\n") for elem in self.skill_list])

    def set_job_satisfaction(self):
        self.job_satisfaction = random.choice["Unhappy", "Happy", "Neither happy nor unhappy"]
        return "Job satisfaction is {self.job_satisfaction}"

    def show_recruitment_vuln(self):
    #this module assumes salary is the only reason people would want to unionize
        if self.member == False:
            if self.job_satisfaction == "Unhappy":
                return "would be very easy"
            elif self.job_satisfaction == "Neither happy nor unhappy":
                if self.salary < stats.mean(self.coworker_sal_list):
                    return "would be realistically possible"
                else:
                    return "may take some convincing"
            else:
                if self.salary < stats.mean(self.coworker_sal_list):
                    return "would be realistically possible"
                else:
                    return "may take some convincing"
            
        else:
            return "is already done. I a union member!"

    def to_string(self):
        """Return a custom string describing this instance"""
        return f"""
            I'm {self.name}.
            I'm a worker in the {self.industry} industry with {self.num_years} years of experience.
            I make {self.salary:.2f} thousand dollars a year.
            I've been alive for {self.get_age_string()}.
            I know:
            {self.get_skills_string()}
            """

    def display_welcome(self):
        """Display a welcome message from this instance."""
        print("Welcome, I'm a new PyBuddy.")
        self.set_job_satisfaction
        print(f"""
            {self.to_string()}
            To recruit me to the union 
            {self.show_recruitment_vuln()}
            You'll need curiousity, the ability to search the web, 
            and the tenacity and resourcefulness to solve all kinds of challenges.
            Let's get started!""")
        
#create a pybuddy
ivan = PyBuddy(
    #most defaults are fine for ivan
    name= "Ivan",
    industry= industry.EDUCATION ,
    num_years= 10,
    salary= 55,
    is_available= True,
    job_satisfaction= "Unhappy",
    skill_list=["Git", "GitHub", "Python", "Markdown", "VS Code"],
    coworker_sal_list= [40, 76, 85, 43, 69, 90, 72]
)
ivan.display_welcome()
