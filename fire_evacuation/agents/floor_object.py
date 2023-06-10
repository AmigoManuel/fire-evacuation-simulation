from mesa import Agent
from mesa.space import Coordinate

from fire_evacuation.utils import get_random_id


class FloorObject(Agent):
    def __init__(
        self,
        pos: Coordinate,
        traversable: bool,
        flammable: bool,
        spreads_smoke: bool,
        visibility: int = 2,
        model=None,
    ):
        rand_id = get_random_id()
        super().__init__(rand_id, model)
        self.pos = pos
        self.traversable = traversable
        self.flammable = flammable
        self.spreads_smoke = spreads_smoke
        self.visibility = visibility

    def get_position(self):
        return self.pos