POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


class Note:
    """A note in the 12-tone chromatic scale.
    
    Attributes:
        position (int): the specific note position within the chromatic scale.
        perspective (str or None): "#" if we're viewing the note from a sharp
            perspective, "b" if we're viewing the note from a flat perspective,
            or None if we are not adopting a perspective.
    """
    def __init__(self, position, perspective=None):
        if isinstance(position, int):
            self.position = position
            self.perspective = perspective
        else:
            self.position = POSITIONS[position]
            if len(position) > 1 and perspective is None:
                self.perspective = position[1]
            else:
                self.perspective = perspective
    
    def __invert__(self):
        perspective = {
            "b": "#",
            "#": "b",
            None: None
        }[self.perspective]
        return Note(self.position, perspective=perspective)
    
    def __add__(self, value):
        position = (self.position + value) % 12
        return Note(position, perspective=self.perspective)
    
    def __sub__(self, value):
        return self + (-value)
    
    def __rshift__(self, other):
        return (self.position - other.position) % 12
    
    def __lshift__(self, other):
        return other >> self
    
    def __repr__(self):
        return f"Note({self.position}, {self.perspective!r})"
    
    def __str__(self):
        names = PITCHES[self.position]
        if len(names) == 1:
            return names[0]
        if self.perspective == "#":
            return names[0]
        elif self.perspective == "b":
            return names[1]
        else:
            return "/".join(names)
