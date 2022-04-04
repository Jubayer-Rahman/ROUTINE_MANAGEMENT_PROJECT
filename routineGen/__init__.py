def geneticAlgorithm():
    from .models import Room, Instructor, MeetingTime, Course
    import random as rnd

    POPULATION_SIZE = 9
    NUMB_OF_ELITE_SCHEDULES = 1
    TOURNAMENT_SELECTION_SIZE = 3
    MUTATION_RATE = 0.2

    class Data:
        def __init__(self):
            self._rooms = Room.objects.all()
            self._meetingTimes = MeetingTime.objects.all()
            self._instructors = Instructor.objects.all()
            self._courses = Course.objects.all()

            self._numberOfClasses = 0
            self._coursesWcredit = []

            for i in range(len(self._courses)):
                last_digit_of_code = int(self._courses[i].code[len(self._courses[i].code)-1])
                lab_course_credit = 0
                if last_digit_of_code % 2 == 0:
                    lab_course_credit = int(self._courses[i].credit * 2)
                else:
                    lab_course_credit = int(self._courses[i].credit)
                for j in range(lab_course_credit):
                    self._coursesWcredit.append(self._courses[i])
                    self._numberOfClasses += 1

        def get_rooms(self): return self._rooms
        def get_instructors(self): return self._instructors
        def get_courses(self): return self._courses
        def get_meetingTimes(self): return self._meetingTimes
        def get_numberOfClasses(self): return self._numberOfClasses
        def get_coursesWcredit(self): return self._coursesWcredit

    class Class:
        def __init__(self, id, course):
            self._id = id
            self._course = course
            self._meetingTime = None
            self._room = None
        def get_id(self): return self._id
        def get_course(self): return self._course
        def get_meetingTime(self): return self._meetingTime
        def get_room(self): return self._room

        def set_meetingTime(self,meetingTime): self._meetingTime = meetingTime
        def set_room(self,room): self._room = room

        def __str__(self):
            return str(self._course.code) + '</td><td>' + str(self._room.number) + '</td><td>' + str(self._course.instructor_id) + '</td><td>' + str(self._meetingTime.meeting_id)

    class Schedule:
        def __init__(self):
            self._data = data
            self._classes = []
            self._numbOfConflicts = 0
            self._fitness = -1
            self._classNumb = 0
            self._isFitnessChanged = True

        def get_classes(self):
            self._isFitnessChanged = True
            return self._classes

        def get_numbOfConflicts(self): return self._numbOfConflicts

        def get_fitness(self):
            if(self._isFitnessChanged == True):
                self._fitness = self.calculate_fitness()
                self._isFitnessChanged = False
            return self._fitness

        def initialize(self):
            courses = self._data.get_coursesWcredit()
            for i in range(len(courses)):
                newClass = Class(self._classNumb, courses[i])
                newClass.set_meetingTime(self._data.get_meetingTimes()[rnd.randrange(0, len(self._data.get_meetingTimes()))])
                newClass.set_room(self._data.get_rooms()[rnd.randrange(0, len(self._data.get_rooms()))])
                self._classes.append(newClass)
                self._classNumb += 1
            return self
        def calculate_fitness(self):
            self._numbOfConflicts = 0
            classes = self.get_classes()
            for i in range(len(classes)):
                if(classes[i].get_room().seating_capacity < classes[i].get_course().numb_of_students):
                    self._numbOfConflicts += 1
                for j in range(len(classes)):
                    if(j>=i):
                        if(classes[i].get_id() != classes[j].get_id()):
                            if(classes[i].get_meetingTime().meeting_id == classes[j].get_meetingTime().meeting_id):
                                if (classes[i].get_room().number == classes[j].get_room().number): self._numbOfConflicts += 1
                                if (classes[i].get_course().instructor == classes[j].get_course().instructor): self._numbOfConflicts += 1
                            elif (classes[i].get_course().code == classes[j].get_course().code and classes[i].get_meetingTime().meeting_day == classes[j].get_meetingTime().meeting_day): self._numbOfConflicts +=1
            return 1 / (1.0*self._numbOfConflicts + 1)
        def __str__(self):
            returnValue = ""
            for i in range(len(self._classes)-1):
                returnValue += str(self._classes[i]) + ","
            returnValue += str(self._classes[len(self._classes)-1])

    class Population:
        def __init__(self, size):
            self._size = size
            self._data = data
            self._schedules = []
            for i in range(size):
                self._schedules.append(Schedule().initialize())
        def get_schedules(self): return self._schedules

    class GeneticAlgorithm:
        def evolve(self, population):
            return self._mutate_population(self._crossover_population(population))

        def _crossover_population(self, pop):
            crossover_pop = Population(0)
            for i in range(NUMB_OF_ELITE_SCHEDULES):
                crossover_pop.get_schedules().append(pop.get_schedules()[i])
            i = NUMB_OF_ELITE_SCHEDULES
            while i < POPULATION_SIZE:
                schedule1 = self._select_tournament_population(pop).get_schedules()[0]
                schedule2 = self._select_tournament_population(pop).get_schedules()[0]
                crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
                i += 1
            return crossover_pop

        def _mutate_population(self, population):
            for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
                self._mutate_schedule(population.get_schedules()[i])
            return population

        def _crossover_schedule(self, schedule1, schedule2):
            crossoverSchedule = Schedule().initialize()
            for i in range(0, len(crossoverSchedule.get_classes())):
                if rnd.random() > 5.0:
                    crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
                else:
                    crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
            return crossoverSchedule

        def _mutate_schedule(self, mutateSchedule):
            schedule = Schedule().initialize()
            for i in range(len(mutateSchedule.get_classes())):
                if MUTATION_RATE > rnd.random():
                    mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
            return mutateSchedule

        def _select_tournament_population(self, pop):
            tournament_pop = Population(0)
            i = 0
            while i < TOURNAMENT_SELECTION_SIZE:
                tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
                i += 1
            tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
            return tournament_pop

    data = Data()
    population = Population(POPULATION_SIZE)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    while (population.get_schedules()[0].get_fitness() != 1.0):
        population = GeneticAlgorithm().evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    return population.get_schedules()[0].get_classes()
