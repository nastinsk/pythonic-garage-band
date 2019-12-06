# base class or parent class
class Musician:

    members = []

    def __init__(self, role, instrument):
        self.role = role
        self.instrument = instrument
        self.__class__.members.append(self)

    def __str__(self):
        return f'I am a {self.role}'

    def __repr__(self):
        return f'This is {self.role}'

    def play_solo(self):
        return f'{self.role} is playing solo on the {self.instrument}'

    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    pass

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass

guitarist = Guitarist('Guitarist', 'guitar')
bassist = Bassist('Bassist','bass')
drummer = Drummer('Drummer', 'drums')
drummer2 = Drummer('Drummer', 'drums')



class Band:

    all = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.__class__.alt.append(self)


    # def play_solos():


    # def __str__():

    # def __repr__():

    @classmethod
    def to_list(cls):
        return all

    # @staticmethod
    # def create_from_data()

band = Band('kazaks', Musician.members)
print(Band.name)

