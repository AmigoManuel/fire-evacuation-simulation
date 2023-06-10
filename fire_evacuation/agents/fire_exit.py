from fire_evacuation.agents.floor_object import FloorObject


class FireExit(FloorObject):
    def __init__(self, pos, model):
        super().__init__(
            pos, traversable=True, flammable=False, spreads_smoke=False, visibility=6, model=model
        )