# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(744, 484)
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_file_name = QLabel(Widget)
        self.lb_file_name.setObjectName(u"lb_file_name")
        self.lb_file_name.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.lb_file_name, 14, 1, 1, 8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_start = QPushButton(Widget)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.pb_start, 1, 3, 1, 1)

        self.cb_use_calories_classes = QCheckBox(Widget)
        self.cb_use_calories_classes.setObjectName(u"cb_use_calories_classes")

        self.gridLayout.addWidget(self.cb_use_calories_classes, 1, 1, 1, 1)

        self.pb_load_image = QPushButton(Widget)
        self.pb_load_image.setObjectName(u"pb_load_image")
        self.pb_load_image.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.pb_load_image, 1, 2, 1, 1)

        self.cb_show_info = QCheckBox(Widget)
        self.cb_show_info.setObjectName(u"cb_show_info")

        self.gridLayout.addWidget(self.cb_show_info, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 17, 1, 1, 7)

        self.le_options = QLineEdit(Widget)
        self.le_options.setObjectName(u"le_options")

        self.gridLayout_2.addWidget(self.le_options, 16, 1, 1, 7)

        self.lb_image = QLabel(Widget)
        self.lb_image.setObjectName(u"lb_image")
        self.lb_image.setMinimumSize(QSize(400, 300))
        self.lb_image.setMaximumSize(QSize(400, 300))
        self.lb_image.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.lb_image, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_time = QLabel(Widget)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_time)

        self.lb_percent = QLabel(Widget)
        self.lb_percent.setObjectName(u"lb_percent")
        self.lb_percent.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_percent)

        self.lb_food_category = QLabel(Widget)
        self.lb_food_category.setObjectName(u"lb_food_category")
        self.lb_food_category.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_food_category)

        self.lb_food_item = QLabel(Widget)
        self.lb_food_item.setObjectName(u"lb_food_item")
        self.lb_food_item.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_food_item)

        self.lb_calories = QLabel(Widget)
        self.lb_calories.setObjectName(u"lb_calories")
        self.lb_calories.setMinimumSize(QSize(200, 0))
        self.lb_calories.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_calories)

        self.lb_answer = QLabel(Widget)
        self.lb_answer.setObjectName(u"lb_answer")
        self.lb_answer.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lb_answer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 5, 1, 3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.lb_file_name.setText(QCoreApplication.translate("Widget", u"FILE NAME:", None))
        self.pb_start.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.cb_use_calories_classes.setText(QCoreApplication.translate("Widget", u"Use Calories Classes", None))
        self.pb_load_image.setText(QCoreApplication.translate("Widget", u"Load image", None))
        self.cb_show_info.setText(QCoreApplication.translate("Widget", u"Show Details Info (only cal.)", None))
        self.lb_image.setText(QCoreApplication.translate("Widget", u"Not load image", None))
        self.lb_time.setText(QCoreApplication.translate("Widget", u"TIME:", None))
        self.lb_percent.setText(QCoreApplication.translate("Widget", u"PERSENT:", None))
        self.lb_food_category.setText(QCoreApplication.translate("Widget", u"FOOD CATEGORY:", None))
        self.lb_food_item.setText(QCoreApplication.translate("Widget", u"FOOD ITEM:", None))
        self.lb_calories.setText(QCoreApplication.translate("Widget", u"CALORIES BY 100g:", None))
        self.lb_answer.setText(QCoreApplication.translate("Widget", u"ANSWER:", None))
    # retranslateUi

