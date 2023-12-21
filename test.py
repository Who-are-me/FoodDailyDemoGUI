# This Python file uses the following encoding: utf-8
# import ai_model as ai
# import time
import pandas as pd
# from PIL import Image


def get_classes_with_calories(name='csv_data/calories.csv'):
    df_classes = pd.read_csv(name)
    names = dict()

    food_category = df_classes['FoodCategory'].unique().tolist()

    for category in food_category:
        names[category] = df_classes.loc[df_classes['FoodCategory'] == category, 'FoodItem'].tolist()

    return names


if __name__ == "__main__":
    # classes = ai.get_classes()
    # classes = [cl.replace('_', ' ') for cl in classes]

    # st = time.time()
    # lprobs = ai.work_ai(classes, Image.open('/Users/vasil.storchak/Downloads/apple_pie.jpg'), ai.get_ai_processor(), ai.get_ai_model())
    # answer = classes[lprobs.index(max(lprobs))]

    # print(f"TIME: {time.time() - st}")
    # print(f"ANSWER: {answer}")
    # print(f"PERCENT: {max(lprobs)}")

    print(get_classes_with_calories())
    pass
