from fire_evacuation.agents.floor_object import FloorObject
from fire_evacuation.agents.smoke import Smoke


class Fire(FloorObject):
    """
    A fire agent

    Attributes:
        ...
    """

    def __init__(self, pos, model):
        super().__init__(
            pos,
            traversable=False,
            flammable=False,
            spreads_smoke=True,
            visibility=20,
            model=model,
        )
        self.smoke_radius = 1

    def step(self):
        neighborhood = self.model.grid.get_neighborhood(
            self.pos, moore=False, include_center=False, radius=self.smoke_radius
        )

        for neighbor_pos in neighborhood:
            contents = self.model.grid.get_cell_list_contents(neighbor_pos)

            if len(contents) > 0:
                has_smoke = False
                has_fire = False
                for agent in contents:
                    if isinstance(agent, Smoke):
                        has_smoke = True
                    elif isinstance(agent, Fire):
                        has_fire = True
                    if has_smoke and has_fire:
                        break

                if not has_fire:
                    for agent in contents:
                        if agent.flammable:
                            fire = Fire(neighbor_pos, self.model)
                            self.model.schedule.add(fire)
                            self.model.grid.place_agent(fire, neighbor_pos)
                            break

                if not has_smoke:
                    for agent in contents:
                        if agent.spreads_smoke:
                            smoke = Smoke(neighbor_pos, self.model)
                            self.model.schedule.add(smoke)
                            self.model.grid.place_agent(smoke, neighbor_pos)
                            break

    def get_position(self):
        return self.pos