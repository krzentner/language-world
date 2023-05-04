

"""
[eod] [code]from app.main import db
from datetime import datetime


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    path = db.Column(db.String(128))


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(128), nullable=False)
    log = db.relationship('Log', back_populates='model')

    def to_dict(self):
        return {
            'id': self.id,
            'path': self.path
        }

    def add_log(self, path):
        return Log(path=path, model=self)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    path = db.Column(db.String(128))
    model = db.relationship('Model', back_populates='log')
[eod] [code]import unittest
import pandas as pd
import numpy as np
import pytest

from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression

from ML_metrics import compute_metrics, MLMetrics
from ML_metrics import calculate_RMSE, calculate_R2



class TestMetrics(unittest.TestCase):
    """Test the functions in ML Metrics"""

    # @pytest.mark.skip
    # @pytest.mark.xfail
    def test_calculate_RMSE(self):
        df = pd.read_csv("Data/housing.csv")
        df['median_house_value'] = df['median_house_value'].apply(pd.to_numeric)
        X_train, X_test, y_train, y_test = train_test_split(
            df[['median_income']], df[['median_house_value']], test_size=0.2, random_state=0)

        model = LinearRegression().fit(X_train, y_train)
        y_pred = model.predict(X_test)

        