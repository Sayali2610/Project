import pandas as pd
import numpy as np
from django.shortcuts import render


def dashboard(request):

    df = pd.read_csv("dataset/students.csv")

    average = np.mean(df["Marks"])
    highest = np.max(df["Marks"])
    lowest = np.min(df["Marks"])

    context = {
        "students": df.to_dict(orient="records"),
        "average": average,
        "highest": highest,
        "lowest": lowest,
    }

    return render(request, "dashboard.html", context)