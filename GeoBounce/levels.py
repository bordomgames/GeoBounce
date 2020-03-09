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
        "sprite_type": "rectangle",
        "coords": [600, 380],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
    },
    {
        "type": "obstacle",
        "sprite_type": "rectangle",
        "coords": [780, 380],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
    },
    {
        "type": "obstacle",
        "sprite_type": "rectangle",
        "coords": [900, 580],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
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
        "sprite_type": "rectangle",
        "coords": [2000, 580],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
    },
    {
        "type": "obstacle",
        "sprite_type": "rectangle",
        "coords": [2150, 580],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
    },
    {
        "type": "obstacle",
        "sprite_type": "rectangle",
        "coords": [2300, 595],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
    },
    {
        "type": "obstacle",
        "sprite_type": "rectangle",
        "coords": [2450, 580],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
    },
    {
        "type": "obstacle",
        "sprite_type": "rectangle",
        "coords": [2600, 580],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
    },
    {
        "type": "obstacle",
        "sprite_type": "rectangle",
        "coords": [2750, 550],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
    },
    {
        "type": "obstacle",
        "sprite_type": "rectangle",
        "coords": [2900, 580],
        "dimensions": [20, 20],
        "fill": "red",
        "outline": "red",
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
        "sprite_type": "rectangle",
        "coords": [800, 580],
        "dimensions": [150, 20],
        "fill": "red",
        "outline": "red",
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
        "dimensions": [400, 20],
        "fill": "black",
        "outline": "black",
    },
]
