# base class or parent class
class Musician:

    def __init__(self, role, instrument):
        self.role = role
        self.instrument = instrument

    def __str__(self):
        return f'I am a {self.role}'

    def __repr__(self):
        return f'This is {self.role}'

    def play_solo(self):
        return f'{self.role} is playing on the {self.instrument}'

    def get_instrument(self):
        return self.instrument



class Guitarist(Musician):
    pass

guitarist = Guitarist("Guitarist", "guitar")




# class Guitarist(Musician)
# class Guitarist(Musician)

#create musian class
# describe role, str,repr, play_solo(), get_instrument() - return string,
# create object instances that made with this class
#

