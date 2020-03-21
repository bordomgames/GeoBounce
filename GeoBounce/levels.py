from os import path


def image_path(image):
    return f"{path.dirname(__file__)}/images/{image}"


level1 = [
    {
        "type": "player",
        "sprite_type": "image",
        "image": image_path("player.png"),
        "coords": [390, 380],
        "dimensions": [20, 20],
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [0, 400],
        "dimensions": [800, 200],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [600, 380],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [780, 380],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [900, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1200, 580],
        "dimensions": [100, 20],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "rectangle",
        "coords": [1220, 560],
        "dimensions": [10, 10],
        "fill": "yellow",
        "outline": "yellow",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1300, 560],
        "dimensions": [100, 40],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "rectangle",
        "coords": [1320, 540],
        "dimensions": [10, 10],
        "fill": "yellow",
        "outline": "yellow",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1400, 540],
        "dimensions": [100, 60],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "rectangle",
        "coords": [1420, 520],
        "dimensions": [10, 10],
        "fill": "yellow",
        "outline": "yellow",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1500, 560],
        "dimensions": [100, 40],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "rectangle",
        "coords": [1520, 540],
        "dimensions": [10, 10],
        "fill": "yellow",
        "outline": "yellow",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1600, 580],
        "dimensions": [100, 20],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [2000, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [2150, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [2300, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [2450, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [2600, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [2750, 530],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike_under.png"),
        "coords": [2750, 550],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [2900, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "goal",
        "sprite_type": "rectangle",
        "coords": [3100, 0],
        "dimensions": [800, 600],
        "fill": "white",
        "outline": "white",
    },
]

level2 = [
    {
        "type": "player",
        "sprite_type": "image",
        "image": image_path("player.png"),
        "coords": [390, 380],
        "dimensions": [20, 20],
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [0, 400],
        "dimensions": [800, 200],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [805, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [825, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [845, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [865, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [885, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [905, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [925, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [945, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [950, 400],
        "dimensions": [50, 200],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1000, 350],
        "dimensions": [20, 250],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1020, 300],
        "dimensions": [20, 300],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1200, 540],
        "dimensions": [620, 20],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1800, 550],
        "dimensions": [20, 50],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1200, 480],
        "dimensions": [620, 20],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1640, 460],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1700, 460],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1760, 460],
        "dimensions": [20, 20],
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [1200, 420],
        "dimensions": [620, 20],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1400, 400],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1500, 400],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1600, 400],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1700, 400],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1800, 400],
        "dimensions": [20, 20],
    },
    {
        "type": "reward",
        "sprite_type": "rectangle",
        "coords": [1950, 520],
        "dimensions": [10, 10],
        "fill": "yellow",
        "outline": "yellow",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [2120, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "reward",
        "sprite_type": "rectangle",
        "coords": [2120, 520],
        "dimensions": [10, 10],
        "fill": "yellow",
        "outline": "yellow",
    },
    {
        "type": "goal",
        "sprite_type": "rectangle",
        "coords": [2300, 0],
        "dimensions": [800, 600],
        "fill": "white",
        "outline": "white",
    },
]


level3 = [
    {
        "type": "player",
        "sprite_type": "image",
        "image": image_path("player.png"),
        "coords": [390, 580],
        "dimensions": [20, 20],
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [580, 580],
        "dimensions": [80, 20],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [660, 560],
        "dimensions": [80, 40],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [740, 540],
        "dimensions": [80, 60],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [820, 520],
        "dimensions": [80, 80],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [900, 500],
        "dimensions": [80, 100],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": [980, 480],
        "dimensions": [80, 120],
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1080, 480],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike_under.png"),
        "coords": [1080, 500],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike.png"),
        "coords": [1100, 480],
        "dimensions": [20, 20],
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": image_path("spike_under.png"),
        "coords": [1100, 500],
        "dimensions": [20, 20],
    },
]


LEVELS = [{"Level 1": level1, "Level 2": level2, "Level 3": level3}]
