import pandas as pd
import  numpy as np
from django.shortcuts import render

#Home page
def home(request):
    return render(request,"home.html")

#Employee List page
def employees(request):
    df = pd.read_csv("dataset/employees.csv")

    context = {
        "employees":df.to_dict(orient="records")
    }
    return render(request,"employees.html",context)

#Analytics page
def analytics(request):
    df = pd.read_csv("dataset/employees.csv")

    average_salary = np.mean(df["Salary"])
    highest_salary = np.max(df["Salary"])
    lowest_salary = np.min(df["Salary"])
    total_employees = len(df)

    context = {
        "average_salary":average_salary,
        "highest_salary":highest_salary,
        "lowest_salary":lowest_salary,
        "total_employees":total_employees,
    }
    return  render(request,"analytics.html",context)

#Search Page
import pandas as pd
from django.shortcuts import render

def search(request):
    df = pd.read_csv("dataset/employees.csv")

    query = request.GET.get("q")

    result = None

    if query:
        result = df[
            (df["EmployeeID"].astype(str).str.contains(query, case=False)) |
            (df["Name"].str.contains(query, case=False))
        ]

    context = {
        "query": query,
        "result": result.to_dict(orient="records") if result is not None else []
    }

    return render(request, "search.html", context)

#About Page
def about(request):
    return render(request,"about.html")