import abc
from pydantic import BaseModel, ConfigDict
from maze import Maze, Position
from typing import List, Any


class BaseSolver(BaseModel, abc.ABC):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    maze: Maze
    trace: List[Position] = [Position (0,0)]
    position: Position = Position (0, 0)


    @abc.abstractmethod
    def next_step(self) -> Position:
        pass

    @abc.abstractmethod
    def solve(self) -> List[Position]:
        pass

