from fire_evacuation.agents.human import Human

from mesa.space import Coordinate

class Security(Human):
    def __init__(
            self,
        pos: Coordinate,
        health: float,
        speed: float,
        vision: int,
        collaborates: bool,
        nervousness,
        experience,
        believes_alarm: bool,
        model,
        security: bool
    ):
        security = True
        super().__init__(
            pos,
            health,
            speed,
            vision,
            collaborates,
            nervousness,
            experience,
            believes_alarm,
            model,
            security
        )
