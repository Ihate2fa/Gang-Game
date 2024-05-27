import numpy as np

class World:
    def __init__(self):
        self.mafias = {}
        self.upcoming = {}
        self.time = 0

    def sim (self, time: int):
        for day in range(time + 1):
            self.time += 1
            # random situations

            if self.time in self.upcoming:
                for task in self.upcoming[time]:
                    # do task
                    ...
            
            """
            Mafia wise
            
            Chance of shootout with enemy gang - 5%
            Chance of RANDOM robbery - 5%
            Chance of RANDOM shootout - 5%
            Chance of RANDOM kidnapping - 5%

            Nothing - 80%
            """

            for mafia_n in self.mafias.keys():
                events = [1, 2, 3, 4, 5]
                weights = [0.05, 0.05, 0.05, 0.05, 0.8]

                event = np.random.choice(events, 5, p=weights)

                if event == 1:
                    possible_mafias = []
                    for emafia_n in self.mafias[mafia_n].keys():
                        if self.mafias[mafia_n].relations[emafia_n] < 0:
                            possible_mafias.append(emafia_n)
                elif event == 2:
                    self.mafias[mafia_n].rob_person()
                elif event == 3:
                    ...
                elif event == 4:
                    self.mafias[mafia_n].kidnap_middleclass()