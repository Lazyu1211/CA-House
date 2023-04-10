import pandas as pd

PATH = "/Users/junyuwu/CA House Analysis /components/housing.csv"
df = pd.read_csv(PATH)
ave_rooms = df["total_rooms"]/df["households"]
df["ave_rooms"] = ave_rooms
ave_bedrooms = df['total_bedrooms']/df['households']
ave_people = df['population']/df['households']
Rooms = df["total_rooms"] / df["households"]
df["Rooms"] = Rooms

def get_data():
    return df

def get_data1():
    to_drop = df[df["median_house_value"]>500000].index
    df.drop(to_drop,inplace=True)
    return df

def get_ocean():
    byoce = df.groupby("ocean_proximity")[["median_house_value"]].mean()
    byoce.reset_index(inplace=True)
    return byoce
