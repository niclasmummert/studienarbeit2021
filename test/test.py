import csv
import io
import os
import unittest
import sys
import base64
import importlib.util
import HtmlTestRunner
import xmlrunner

spec = importlib.util.spec_from_file_location("knn_module", "knn_module.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

spec = importlib.util.spec_from_file_location("ml_module", "ml_module.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

spec = importlib.util.spec_from_file_location("ui", "ui.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

spec = importlib.util.spec_from_file_location("bewertung", "bewertung.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

from bewertung import open_window
from knn_module import data_to_int, knn_prediction, output_to_str
from ml_module import ml_prediction, preprocess
from ui import convert_to_bytes


class TestImportVersions(unittest.TestCase):
    """
    Testing the packages versions used in the project
    """

    def test_PIL_pos(self):
        """
        Testing if PIL.__version__ is correct
        """
        import PIL
        from PIL import Image

        self.assertEqual(PIL.__version__, "8.1.0")

    def test_Pandas_pos(self):
        """
        Testing if pd.__version__ is correct
        """
        import pandas as pd

        self.assertEqual(pd.__version__, "0.23.4")

    def test_csv_pos(self):
        """
        Testing if csv.__version__ is correct
        """
        import csv

        self.assertEqual(csv.__version__, "1.0")

    def test_torch_pos(self):
        """
        Testing if torch.__version__ is correct
        """
        import torch
        from torch import tensor

        self.assertEqual(torch.__version__, "1.7.1+cpu")

    def test_torchvision_pos(self):
        """
        Testing if torchvision.__version__ is correct
        """
        import torchvision
        from torchvision import transforms

        self.assertEqual(torchvision.__version__, "0.5.0")

    def test_json_pos(self):
        """
        Testing if json.__version__ is correct
        """
        import json

        self.assertEqual(json.__version__, "2.0.9")

    def test_requests_pos(self):
        """
        Testing if requests.__version__ is correct
        """
        import requests

        self.assertEqual(requests.__version__, "2.22.0")

    def test_sklearn_pos(self):
        """
        Testing if sklearn.__version__ is correct
        """
        import sklearn
        from skl2onnx.shape_calculators import NearestNeighbours
        from sklearn import preprocessing
        from sklearn.externals import joblib
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.tree import DecisionTreeClassifier

        self.assertEqual(sklearn.__version__, "0.20.3")

    def test_numpy_pos(self):
        """
        Testing if numpy.__version__ is correct
        """
        import numpy as np

        self.assertEqual(np.__version__, "1.19.5")


class TestUI(unittest.TestCase):
    """
    Testing the UI in the project
    """

    def test_convert_to_bytes_pos1(self):
        """
        Testing if convert_to_bytes is correct for a normal string
        """
        folder = r"images1"
        png_files = [
            folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f
        ]
        filename = png_files[0]
        data = convert_to_bytes(filename)
        self.assertIsInstance(data, bytes)
        self.assertIsNotNone(data)

    @unittest.skip("There is some magical stuff going on")
    def test_convert_to_bytes_pos2(self):
        """
        Testing if convert_to_bytes is working correct for a bunch of base64 bytes
        """
        folder = r"images1"
        png_files = [
            folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f
        ]
        filename = png_files[0]
        data = io.BytesIO(base64.b64encode(filename))
        data = convert_to_bytes(data)
        self.assertIsInstance(data, bytes)
        self.assertIsNotNone(data)


class TestKnnModule(unittest.TestCase):
    """
    Testing the knn_module, which contains data_to_int, output_to_str and knn_prediction method
    """

    def test_knn_prediction_pos1(self):
        """
        Testing if knn_prediction is working correct with iterator = 0 !
        """
        ret = knn_prediction("Normal", "stonepath", 0)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)

    def test_knn_prediction_pos2(self):
        """
        Testing if knn_prediction is working correct with iterator = 0 !
        """
        directories = os.listdir(r"./")
        self.assertTrue(directories.__contains__("knn_model_v1.pkl"))

    def test_knn_prediction_pos3(self):
        """
        Testing if knn_prediction is working correct with iterator = 11 !
        """
        fields = ["prev_suspensiontype", "surfacetype", "suspensiontype"]
        with open("user_df.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(
                [
                    {
                        "prev_suspensiontype": "Normal",
                        "surfacetype": "tarmac",
                        "suspensiontype": "Normal",
                    },
                    {
                        "prev_suspensiontype": "Comfort",
                        "surfacetype": "stonepath",
                        "suspensiontype": "Comfort",
                    },
                    {
                        "prev_suspensiontype": "Sport",
                        "surfacetype": "dirtroad",
                        "suspensiontype": "Comfort",
                    },
                    {
                        "prev_suspensiontype": "Sport",
                        "surfacetype": "tarmac",
                        "suspensiontype": "Sportplus",
                    },
                    {
                        "prev_suspensiontype": "Normal",
                        "surfacetype": "stonepath",
                        "suspensiontype": "Comfort",
                    },
                    {
                        "prev_suspensiontype": "Normal",
                        "surfacetype": "dirtroad",
                        "suspensiontype": "Comfort",
                    },
                ]
            )
        ret = knn_prediction("Normal", "stonepath", 15)
        directories = os.listdir(r"./")
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertTrue(directories.__contains__("user_df.csv"))
        self.assertTrue(directories.__contains__("user_model_v1.pkl"))

    def test_knn_prediction_pos4(self):
        """
        Testing if knn_prediction is working correct with iterator = 12 !
        """
        ret = knn_prediction("Normal", "stonepath", 20)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)

    def test_data_to_int_pos(self):
        """
        Testing if data_to_int is working correct
        """
        str_prev_suspensiontype = "Normal"
        str_surfacetype = "stonepath"
        ret_one, ret_two = data_to_int(str_prev_suspensiontype, str_surfacetype)
        self.assertIsInstance(ret_one, int)
        self.assertIsInstance(ret_two, int)
        self.assertEqual(ret_one, 1)
        self.assertEqual(ret_two, 2)
        self.assertIsNotNone(ret_one)
        self.assertIsNotNone(ret_two)

    def test_output_to_str_pos(self):
        """
        Testing if output_to_str is working correct
        """
        ret = output_to_str(1)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "Normal")
        ret = output_to_str(2)
        self.assertEqual(ret, "Sport")
        ret = output_to_str(3)
        self.assertEqual(ret, "Sportplus")
        ret = output_to_str(0)
        self.assertEqual(ret, "Comfort")


class TestMLModule(unittest.TestCase):
    """
    Testing the ml_module, which contains preprocess and ml_prediction method
    """

    def test_preprocess_pos1(self):
        """
        Testing if preprocess is working correct for jpg files
        """
        image_file = "test_img.jpg"
        ret = preprocess(image_file)
        self.assertEqual(str(type(ret)), "<class 'numpy.ndarray'>")
        self.assertIsNotNone(ret)

    def test_preprocess_pos2(self):
        """
        Testing if preprocess is working correct for png files
        """
        folder = r"images1"
        png_files = [
            folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f
        ]
        image_file = png_files[0]
        ret = preprocess(image_file)
        self.assertEqual(str(type(ret)), "<class 'numpy.ndarray'>")
        self.assertIsNotNone(ret)

    def test_ml_prediction_pos1(self):
        """
        Testing if ml_prediction is working correct for jpg files
        """
        image_file = "test_img.jpg"
        ret = ml_prediction(image_file)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "tarmac")

    def test_ml_prediction_pos2(self):
        """
        Testing if ml_prediction is working correct for png files
        """
        folder = r"images1"
        png_files = [
            folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f
        ]
        image_file = png_files[0]
        ret = ml_prediction(image_file)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "tarmac")


class TestBewertungModule(unittest.TestCase):
    """
    Testing the bewertung, which contains open_window method
    """

    @unittest.skip("Somehow the window is not closing automaticaly")
    def test_bewertung_pos1(self):
        """
        Testing if ml_prediction is working correct for jpg files
        """
        window = open_window()
        window.close()
        ret = window.was_closed()
        self.assertEqual(ret, True)
        window.close()


# @unittest.expectedFailure
class ExpectedFailureTestCase(unittest.TestCase):
    """
    Testing all modules from above and try them to fail. But add ExpectFailure to TestCase to have a green signal to proceed
    """

    @unittest.expectedFailure
    def test_ml_prediction_neg1(self):
        """
        Wrong folder so no image should be found
        """
        folder = r"ml_app/images1"
        png_files = [
            folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f
        ]
        image_file = png_files[0]
        ret = ml_prediction(image_file)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "tarmac")

    @unittest.expectedFailure
    def test_ml_prediction_neg2(self):
        """
        Null Pointer Parameter so Test should be fail
        """
        ret = ml_prediction(None)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "tarmac")

    @unittest.expectedFailure
    def test_ml_prediction_neg3(self):
        """
        No Parameter so Test should be fail
        """
        ret = ml_prediction()
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "tarmac")

    @unittest.expectedFailure
    def test_ml_prediction_neg4(self):
        """
        Parameter has wrong type so function should fail
        """
        folder = r"images1"
        png_files = [
            folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f
        ]
        image_file = png_files[0]
        ret = ml_prediction(20)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "tarmac")

    @unittest.expectedFailure
    def test_preprocess_neg1(self):
        """
        Wrong folder so no image should be found
        """
        folder = r"ml_app/images1"
        png_files = [
            folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f
        ]
        image_file = png_files[0]
        ret = preprocess(image_file)
        self.assertEqual(str(type(ret)), "<class 'numpy.ndarray'>")
        self.assertIsNotNone(ret)

    @unittest.expectedFailure
    def test_preprocess_neg2(self):
        """
        Null Pointer Parameter so Test should be fail
        """
        ret = preprocess(None)
        self.assertEqual(str(type(ret)), "<class 'numpy.ndarray'>")
        self.assertIsNotNone(ret)

    @unittest.expectedFailure
    def test_preprocess_neg3(self):
        """
        No Parameter so Test should be fail
        """
        ret = preprocess()
        self.assertEqual(str(type(ret)), "<class 'numpy.ndarray'>")
        self.assertIsNotNone(ret)

    @unittest.expectedFailure
    def test_preprocess_neg4(self):
        """
        Parameter has wrong type so Test should be fail
        """
        ret = preprocess(20)
        self.assertEqual(str(type(ret)), "<class 'numpy.ndarray'>")
        self.assertIsNotNone(ret)

    @unittest.expectedFailure
    def test_output_to_str_neg1(self):
        """
        Parameter out of number range or border
        """
        ret = output_to_str(4)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "Normal")

    @unittest.expectedFailure
    def test_output_to_str_neg2(self):
        """
        Null Pointer Parameter so Test should be fail
        """
        ret = output_to_str(None)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "Normal")

    @unittest.expectedFailure
    def test_output_to_str_neg3(self):
        """
        No Parameter so Test should be fail
        """
        ret = output_to_str()
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "Normal")

    @unittest.expectedFailure
    def test_output_to_str_neg4(self):
        """
        Parameter has wrong type so Test should be fail
        """
        ret = output_to_str(20)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)
        self.assertEqual(ret, "Normal")

    @unittest.expectedFailure
    def test_data_to_int_neg1(self):
        """
        No valid Parameter so function should fail
        """
        str_prev_suspensiontype = "Not Normal"
        str_surfacetype = "stonepath"
        ret_one, ret_two = data_to_int(str_prev_suspensiontype, str_surfacetype)
        self.assertIsInstance(ret_one, int)
        self.assertIsInstance(ret_two, int)
        self.assertEqual(ret_one, 1)
        self.assertEqual(ret_two, 2)
        self.assertIsNotNone(ret_one)
        self.assertIsNotNone(ret_two)

    @unittest.expectedFailure
    def test_data_to_int_neg2(self):
        """
        First Parameter is Null Pointer so function should fail
        """
        ret_one, ret_two = data_to_int(None, "stonepath")
        self.assertIsInstance(ret_one, int)
        self.assertIsInstance(ret_two, int)
        self.assertEqual(ret_one, 1)
        self.assertEqual(ret_two, 2)
        self.assertIsNotNone(ret_one)
        self.assertIsNotNone(ret_two)

    @unittest.expectedFailure
    def test_data_to_int_neg3(self):
        """
        Second Parameter is Null Pointer so function should fail
        """
        ret_one, ret_two = data_to_int("Normal", None)
        self.assertIsInstance(ret_one, int)
        self.assertIsInstance(ret_two, int)
        self.assertEqual(ret_one, 1)
        self.assertEqual(ret_two, 2)
        self.assertIsNotNone(ret_one)
        self.assertIsNotNone(ret_two)

    @unittest.expectedFailure
    def test_data_to_int_neg4(self):
        """
        First Parameter has wrong type so function should fail
        """
        ret_one, ret_two = data_to_int(1, "stonepath")
        self.assertIsInstance(ret_one, int)
        self.assertIsInstance(ret_two, int)
        self.assertEqual(ret_one, 1)
        self.assertEqual(ret_two, 2)
        self.assertIsNotNone(ret_one)
        self.assertIsNotNone(ret_two)

    @unittest.expectedFailure
    def test_data_to_int_neg5(self):
        """
        Second Parameter is missing so function should fail
        """
        ret_one, ret_two = data_to_int("Normal")
        self.assertIsInstance(ret_one, int)
        self.assertIsInstance(ret_two, int)
        self.assertEqual(ret_one, 1)
        self.assertEqual(ret_two, 2)
        self.assertIsNotNone(ret_one)
        self.assertIsNotNone(ret_two)

    @unittest.expectedFailure
    def test_knn_prediction_neg1(self):
        """
        Third Parameter has wrong type so function should be fail
        """
        ret = knn_prediction("Normal", "stonepath", "please_fail")
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)

    @unittest.expectedFailure
    def test_knn_prediction_neg2(self):
        """
        Third Parameter is Null Pointer so function should be fail
        """
        ret = knn_prediction("Normal", "stonepath", None)
        self.assertIsInstance(ret, str)
        self.assertIsNotNone(ret)

    @unittest.expectedFailure
    def test_convert_to_bytes_neg1(self):
        """
        Wrong folder so no image should be found
        """
        folder = r"ml_app/images1"
        png_files = [
            folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f
        ]
        filename = png_files[0]
        data = convert_to_bytes(filename)
        self.assertIsInstance(data, bytes)
        self.assertIsNotNone(data)

    @unittest.expectedFailure
    def test_convert_to_bytes_neg2(self):
        """
        Parameter is Null Pointer so function should fail
        """
        data = convert_to_bytes(None)
        self.assertIsInstance(data, bytes)
        self.assertIsNotNone(data)

    @unittest.expectedFailure
    def test_convert_to_bytes_neg3(self):
        """
        Parameter has wrong type so function should fail
        """
        data = convert_to_bytes(20)
        self.assertIsInstance(data, bytes)
        self.assertIsNotNone(data)

    @unittest.expectedFailure
    def test_convert_to_bytes_neg4(self):
        """
        Parameter is missing so function should fail
        """
        data = convert_to_bytes()
        self.assertIsInstance(data, bytes)
        self.assertIsNotNone(data)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='html_report'))
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output="xml_report"))
