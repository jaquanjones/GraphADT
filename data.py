adjacent_cities = {
    "Seattle": ["San Francisco", "Denver", "Chicago"],
    "San Francisco": ["Seattle", "Los Angeles", "Denver"],
    "Los Angeles": ["San Francisco", "Denver", "Kansas", "Dallas"],
    "Denver": ["Seattle", "San Francisco", "Los Angeles", "Kansas", "Chicago"],
    "Kansas": ["Los Angeles", "Denver", "Chicago", "New York", "Atlanta", "Dallas"],
    "Chicago": ["Seattle", "Denver", "Kansas", "Boston", "New York"],
    "Boston": ["Chicago", "New York"],
    "New York": ["Kansas", "Chicago", "Boston", "Atlanta"],
    "Atlanta": ["Kansas", "New York", "Miami", "Dallas", "Houston"],
    "Miami": ["Atlanta", "Houston"],
    "Dallas": ["Los Angeles", "Kansas", "Atlanta", "Houston"],
    "Houston": ["Atlanta", "Miami", "Dallas"],
}

cities = (
    "Seattle",
    "San Francisco",
    "Los Angeles",
    "Denver",
    "Kansas",
    "Chicago",
    "Boston",
    "New York",
    "Atlanta",
    "Miami",
    "Dallas",
    "Houston"
)

# to convert integer user input
index_val = {
    0: "Seattle",
    1: "San Francisco",
    2: "Los Angeles",
    3: "Denver",
    4: "Kansas",
    5: "Chicago",
    6: "Boston",
    7: "New York",
    8: "Atlanta",
    9: "Miami",
    10: "Dallas",
    11: "Houston",
}
