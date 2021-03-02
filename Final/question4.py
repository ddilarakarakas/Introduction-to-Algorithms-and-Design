from random import randint

class Job:
    def __init__(self, unit, jobName):
        self.unit = unit
        self.jobName = jobName

    
    def print_job_info(self):
        print("Job Name : " + self.jobName + ", Unit : " + str(self.unit))


class Person:
    def __init__(self, person_name, unit_time):
        self.person_name = person_name
        self.unit_time = unit_time
        self.hasJob = False
        self.job = None
        self.work_time = None
        self.jobs = []
    
    def set_job(self, job):
        if Job != None:
            self.hasJob = True
            self.job = job
            self.work_time = float(job.unit) / float(self.unit_time)
    
    def add_job(self, job):
        self.work_time = float(job.unit) / float(self.unit_time)
        self.jobs.append(self.work_time)

    def find_min_index(self):
        index = 0
        minValue = 999999
        findIndex = 0
        while index < len(self.jobs):
            if index not in self.signedIndex:
                if jobs[index]<minValue:
                    minValue = jobs[index]
                    findIndex = index
            index += 1
        return findIndex




    def print_person_info(self):
        if self.job==None:
            self.hasJob = False
            print("Name : " + self.person_name + ", Unit Time : " + 
                str(self.unit_time)  + ", Has Job : " + str(self.hasJob) + ", Job : " + str(self.job))
        else:
            self.hasJob = True
            print("Name : " + self.person_name + ", Unit Time : " + 
                str(self.unit_time)  + ", Has Job : " + str(self.hasJob) + ", Job Name: " + self.job.jobName + ", Job Unit : " + str(self.job.unit) + ", Work Time : " + str(self.work_time))

def fillPeopleJobs(people, jobs):
    i = 0
    while i < len(people):
        j = 0
        while j<len(jobs):
            people[i].add_job(jobs[j])
            j += 1
        i += 1

def findIndex(people, index):
    i = 0
    minValue = 999999
    returnIndex = 0
    while i<len(people):
        if people[i].hasJob == False:
            if people[i].jobs[index]<minValue:
                returnIndex = i
                minValue = people[i].jobs[index]
        i += 1
    return returnIndex

def assignment(people, jobs):
    fillPeopleJobs(people, jobs)
    i = 0
    while i < len(jobs):
        index = findIndex(people, i)
        people[index].set_job(jobs[i])
        i += 1
    

def test1():
    i = 0
    jobs = []
    persons = []
    while i < 10:
        temp_job_name = str(i)+"_job"
        temp_job = Job(randint(10,100), temp_job_name)
        jobs.append(temp_job)
        temp_person_name = str(i)+"_person"
        temp_person = Person(person_name=temp_person_name, unit_time=randint(1,5))
        persons.append(temp_person)
        i +=1
    i = 0
    while i<10:
        jobs[i].print_job_info()
        persons[i].print_person_info()
        print("\n")
        i += 1
    assignment(persons, jobs)
    i = 0
    while i<10:
        persons[i].print_person_info()
        i +=1



test1()
