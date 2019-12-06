# base class or parent class
class Musician:

    members = []

    def __init__(self, role, instrument):
        self.role = role
        self.instrument = instrument
        self.__class__.members.append(self)

    # def __str__(self):
    #     return f'I am a {self.role}'

    # def __repr__(self):
    #     return f'This is {self.role}'

    # def play_solo(self):
    #     return f'{self.role} is playing solo on the {self.instrument}'

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


#     # def play_solos():


#     # def __str__():

#     # def __repr__():

#     @classmethod
#     def to_list(cls):
#         return all

    @staticmethod
    def create_from_data(data):
        members = []
        parsed_data = data.split('\n')
        band_name = parsed_data[0]

        for i in range(1, len(parsed_data)-1):
            print("new member")
            musician_data = parsed_data[i].split(",")
            if musician_data[0] == "Guitarist":
                members.append(Guitarist(musician_data[0], musician_data[1]))

            if musician_data[0] == "Bassist":
                members.append(Bassist(musician_data[0], musician_data[1]))
            else:
                members.append(Drummer(musician_data[0], musician_data[1]))

        return members



Band.create_from_data(band_data)
print(Band.all)

