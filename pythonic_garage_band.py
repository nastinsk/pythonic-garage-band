# base class or parent class
class Musician:

    members = []

    def __init__(self, role, instrument):
        self.role = role
        self.instrument = instrument
        self.__class__.members.append(self)

    def __str__(self):

        # FIX_BUG!!!
        # for some reasons this format {} displays an error in my console, can't find why
        # return f'I am a {self.role}'
        return ("I am a " + self.role)

    def __repr__(self):
        # return f'This is {self.role}'
        return ("This is a " + self.role)

    def play_solo(self):
        # return f'{self.role} is playing solo on the {self.instrument}'
        return (self.role + "is playing solo on the "+ self.instrument)

    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    pass

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass

def read_file(file):
    """F() to take data from band.txt file"""
    with open(file, 'r') as f:
        template = (f.read())
        return template

band_data = read_file("band.txt")

class Band:

    all = []


    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        self.__class__.all.append(self)

# ============To DO
    # def play_solos(self):
    #     for el in self.members:
    #         el.play_solo()



    def __str__():
        return ("We are the " + self.name)

    def __repr__():
         return ("This is the " + self.name)

    @classmethod
    def to_list(cls):
        return cls.all

    @staticmethod
    def create_from_data(data):
        members = []
        parsed_data = data.split('\n')
        band_name = parsed_data[0]

        for el in parsed_data[1:len(parsed_data)-1]:

            musician_data = el.split(",")
            print(el)
            if musician_data[0] == "Bassist":
                members.append(Bassist(musician_data[0], musician_data[1]))

            if musician_data[0] == "Guitarist":
                members.append(Guitarist(musician_data[0], musician_data[1]))
            else:
                members.append(Drummer(musician_data[0], musician_data[1]))

            # FIX_BUG!!!
            # Can't figure out why I have extra member in the band all the time
            print(members)
            print(el)
        return band_name, members




Band(Band.create_from_data(band_data))
# Can't figure out why I have extra member in the band all the time
print(Band.all[0].name)


