from fire_evacuation.agents.floor_object import FloorObject


class Sight(FloorObject):
    def __init__(self, pos, model):
        super().__init__(
            pos, traversable=True, flammable=False, spreads_smoke=True, visibility=-1, model=model
        )

    def get_position(self):
        return self.pos