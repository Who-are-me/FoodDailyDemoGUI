import src.FoodDaily.src.interface_ai as ai
import time
import asyncio
import pandas as pd

from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from os.path import expanduser
from PySide6 import QtWidgets
from PIL import Image
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Slot

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from src.ui_form import Ui_Widget


class Widget(QWidget):
    # FIXME make async
    async def async_constructor(self):
        self.ai_model = ai.get_ai_model()
        self.ai_processor = ai.get_ai_processor()


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.le_options.setPlaceholderText("Enter names of classes separated by ,")

        self.ui.pb_load_image.clicked.connect(self.slot_load_image)
        self.ui.pb_start.clicked.connect(self.slot_start_ai)

        asyncio.run(self.async_constructor())


    def get_classes_with_calories(self, name='data_csv/calories.csv'):
        df_classes = pd.read_csv(name)
        classes = dict()
        classes_calories = dict()

        food_category = df_classes['FoodCategory'].unique().tolist()

        for category in food_category:
            classes[category] = df_classes.loc[df_classes['FoodCategory'] == category, 'FoodItem'].tolist()
            classes_calories[category] = df_classes.loc[df_classes['FoodCategory'] == category, 'Cals_per100grams'].tolist()

        return classes, classes_calories


    # FIXME make async
    async def async_ai(self, classes: list = None):
        st = time.time()
        lprobs = ai.ai_calculate(
                    self.classes if classes == None else classes,
                    self.image,
                    self.ai_processor,
                    self.ai_model)
        answer = self.classes[lprobs.index(max(lprobs))] if classes == None else classes[lprobs.index(max(lprobs))]

        self.ui.lb_time.setText(f"TIME: {time.time() - st}")
        self.ui.lb_answer.setText(f"ANSWER: {answer}")
        self.ui.lb_percent.setText(f"PERCENT: {max(lprobs)}")


    def work_ai_by_multilevel(self, is_category = False, classes: list = None, classes_calories: list = None):
        st = time.time()
        lprobs = ai.ai_calculate(
            self.classes if classes == None else classes,
            self.image,
            self.ai_processor,
            self.ai_model)
        answer = self.classes[lprobs.index(max(lprobs))] if classes == None else classes[lprobs.index(max(lprobs))]

        if is_category:
            self.ui.lb_food_category.setText(f"FOOD CATEGORY: {answer}")
            return answer, lprobs.index(max(lprobs))
        else:
            self.ui.lb_time.setText(f"TIME: {time.time() - st}")
            self.ui.lb_answer.setText(f"ANSWER: {answer}")
            self.ui.lb_percent.setText(f"PERCENT: {max(lprobs)}")
            self.ui.lb_food_item.setText(f"FOOD ITEM: {answer}")
            self.ui.lb_calories.setText(f"CALORIES BY 100g: {classes_calories[lprobs.index(max(lprobs))]}")

            if self.ui.cb_show_info.isChecked():
                dlg = QMessageBox()
                dlg.setWindowTitle("Info massage")
                dlg.setText(f"Classes:\n{classes}\nPercents:\n{lprobs}.")
                dlg.exec()


    @Slot()
    def slot_start_ai(self):
        if self.ui.cb_use_calories_classes.isChecked():
            dict_classes, dict_classes_calories = self.get_classes_with_calories('src/resource/calories.csv')
            answer, ind_answer = self.work_ai_by_multilevel(classes=list(dict_classes.keys()), is_category=True)
            self.work_ai_by_multilevel(classes=dict_classes[answer], classes_calories=dict_classes_calories[answer])
        else:
            self.classes = self.ui.le_options.text().split(',')

            if len(self.classes) <= 1:
                self.classes = ai.get_classes('src/FoodDaily/data_csv/names_of_food.csv')
                self.classes = [cl.replace('_', ' ') for cl in self.classes]

            asyncio.run(self.async_ai())

    @Slot()
    def slot_load_image(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(dir=f"{expanduser('~')}/Downloads", filter="Image Files (*.png *.jpg *.jpeg)")
        self.ui.lb_file_name.setText(f"FILE NAME: {fname[0]}")
        self.image = Image.open(fname[0])
        w, h = self.image.size
        self.image = self.image.resize((int(w/2), int(h/2)))
        # set image to label
        pixmap = QPixmap(fname[0])
        pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.ui.lb_image.setPixmap(pixmap)

