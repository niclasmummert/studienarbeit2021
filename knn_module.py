import numpy as np
import pandas as pd
import sklearn
from skl2onnx.shape_calculators import NearestNeighbours
from sklearn import preprocessing
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

knn_joblib_file = "knn_model_v1.pkl"
user_joblib_file = "user_model_v1.pkl"


def data_to_int(str_prev_suspensiontype, str_surfacetype):
    if (str_prev_suspensiontype == "Normal"):
        int_prev_suspensiontype = 1
    elif (str_prev_suspensiontype == "Sport"):
        int_prev_suspensiontype = 2
    elif (str_prev_suspensiontype == "Sportplus"):
        int_prev_suspensiontype = 3
    else:
        int_prev_suspensiontype = 0
    
    if (str_surfacetype == "stonepath"):
        int_surfacetype = 2
    elif (str_surfacetype == "dirtroad"):
        int_surfacetype = 1
    else:
        int_surfacetype = 0

    return int_prev_suspensiontype, int_surfacetype

def output_to_str(output):
    if (output == 1):
        ret = "Normal"
    elif (output == 2):
        ret = "Sport"
    elif (output == 3):
        ret = "Sportplus"
    else:
        ret = "Comfort"
    return ret

def knn_prediction(str_prev_suspensiontype, str_surfacetype, img_iterator=0):
    if (img_iterator <= 14):
        print("Using knn_model")
        # Load from file
        knn_model = joblib.load(knn_joblib_file)
        int_prev_suspensiontype, int_surfacetype = data_to_int(str_prev_suspensiontype, str_surfacetype)
        data = [(int_prev_suspensiontype, int_surfacetype)]
        output = knn_model.predict(data)
        ret = output_to_str(output)
        print("Analysed Output", ret)
    elif (img_iterator == 15):
        print("Creating user_model")
        filename = "user_df.csv"
        df = pd.read_csv(filename)
        le = preprocessing.LabelEncoder()
        prev_susp = le.fit_transform(list(df["prev_suspensiontype"]))
        surf = le.fit_transform(list(df["surfacetype"]))
        susp = le.fit_transform(list(df["suspensiontype"]))
        X = list(zip(prev_susp, surf))
        y = list(susp)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
        user_model = KNeighborsClassifier(n_neighbors=4)
        user_model.fit(X_train, y_train)
        joblib.dump(user_model, user_joblib_file)
        int_prev_suspensiontype, int_surfacetype = data_to_int(str_prev_suspensiontype, str_surfacetype)
        data = [(int_prev_suspensiontype, int_surfacetype)]
        output = user_model.predict(data)
        ret = output_to_str(output)
        print("Analysed Output", ret)
    else:
        print("Using user_model")
        user_model = joblib.load(user_joblib_file)
        int_prev_suspensiontype, int_surfacetype = data_to_int(str_prev_suspensiontype, str_surfacetype)
        data = [(int_prev_suspensiontype, int_surfacetype)]
        output = user_model.predict(data)
        ret = output_to_str(output)
        print("Analysed Output", ret)
    
    return ret

# def main():
#     str_prev_suspensiontype = "Normal"
#     str_surfacetype = "stonepath"
#     img_iterator = 12
#     out = knn_prediction(str_prev_suspensiontype, str_surfacetype, img_iterator)
#     out_string = "Current Surfacetyp: " + str_surfacetype + ", Previous Suspensiontype: " + str_prev_suspensiontype + ", is leeding to the Suspensiontype: " + out
#     print(out_string)

# if __name__ == "__main__":
#     main()
