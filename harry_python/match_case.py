x=11

match x:
    case 0:
        print("x is zero")
    case 4 if x%2==0:
        print(f"x%2==0 and case is 4 and x is {x}")
    case _ if x<10:
        print("x is <10")
    case _:
        print(x)







def data_type_detector(colum_type):
     match colum_type:
         case "int":
              print("Process as numeric integer data. Apply scaling if needed.")
         case "float":
              print("Process as continuous numeric data. Check for outliers and normalize.")
         case "str":
             print("process as string ")
         case "bool":
             print("process as boolean ")
         case _ :
             print("Unkown data type")



data_type_detector("str")



# qno 
def ml_strategy(datset_size):
    match datset_size.lower():

        case "small":
            print("Use simple models and cross-validation.")
            print("Recommended: Logistic Regression, Decision tree")
        case "medium":
            print("Use feature engineering and ensemble methods.")
            print("Recommended: Random Forest , Gradient Boosting")
        case "large":
            print("use scalable and distributed learning.")
            print("Recommended :Deep learning or distributed Ml(Spark)")
        case _:
            print("Unkown dataset size. Please check input.")

ml_strategy("small")












# qno 
def imputation_strategy(column_type):

    match column_type.lower():

        case "numeric":
            print("Imputation: Use mean or median value.")

        case "categorical":
            print("Imputation: Use mode (most frequent category).")

        case "datetime":
            print("Imputation: Use forward fill or interpolation.")

        case _:
            print("Unknown column type. Manual review required.")


# qno 
def recommend_model(problem_type):

    match problem_type.lower():

        case "classification":
            print("Recommended Models: Logistic Regression, Random Forest, SVM")

        case "regression":
            print("Recommended Models: Linear Regression, Ridge, Decision Tree Regressor")

        case "clustering":
            print("Recommended Models: K-Means, DBSCAN, Hierarchical Clustering")

        case _:
            print("Unknown problem type. Please specify a valid ML task.")




def preprocessing_action(quality_status):

    match quality_status.lower():

        case "clean":
            print("Action: No action needed. Dataset is ready for analysis.")

        case "missing":
            print("Action: Impute missing values or remove rows/columns.")

        case "duplicate":
            print("Action: Remove duplicate records.")

        case "corrupted":
            print("Action: Investigate corrupted rows and correct or remove them.")

        case _:
            print("Action: Unknown quality status. Manual inspection required.")




def feature_scaling_decision(algorithm):

    match algorithm.lower():

        case "knn" | "svm" | "linear":
            print(f"Algorithm: {algorithm.upper()} → Scaling Required (normalize or standardize features)")

        case "tree":
            print(f"Algorithm: {algorithm.upper()} → Scaling Not Required (tree-based models are scale-invariant)")

        case _:
            print(f"Algorithm: {algorithm.upper()} → Unknown algorithm. Manual decision required.")


feature_scaling_decision('svm')






def marketing_label(spending_category):

    match spending_category.lower():

        case "low":
            print("Spending Category: LOW → Marketing Label: Budget Shopper")

        case "medium":
            print("Spending Category: MEDIUM → Marketing Label: Regular Customer")

        case "high":
            print("Spending Category: HIGH → Marketing Label: Premium Customer")

        case _:
            print("Spending Category: UNKNOWN → Marketing Label: Manual Review")








# qno 
def calculate_bonus(department,performence_score):
    match department.lower():
        case "sales" if performence_score>=85:
            print("departmen :sales >High Bonus ")
        case "sales" if performence_score>=60:
            print("department:sales > Medium Bonus")
        case "sales":
            print("Department: Sales > Low Bonus")
        case "engineering" if performence_score>=90:
            print("Departmen:Engineering > High Bonus")
        case "engineering" :
            print("Department:Engineering > Standered Bonus")
        case "hr":
            print("Department:HR > Fixed Bonus")
        case _:
            print("Unkown department. No bonus assigned")

calculate_bonus("sales",66)
calculate_bonus("engineering",89)






# qno 
def e_commerce_cal(delivery_type,order_amount):
    match delivery_type.lower():
        case "standered" if order_amount>=5000:
            print("Order Type:Standered > Amount:Free Shipping")
        case "standered" :
            print("Delivery Type:Standered >Amount:RS 200")
        case "express" if order_amount>=8000:
            print("Delivery Type:Express > Shipping Amount :RS 100")
        case "express":
            print("Delivery Type:Express > Shipping Amount:RS 400")
        case "same_day":
            print("Delivery Type:Same Day > Shipping Amount:RS 700")



e_commerce_cal("standered",500000)










# # API Response Handler using match-case

# # Inputs
# status_code = int(input("Enter status code: "))
# retry_count = int(input("Enter retry count: "))

# # Match-case for API response handling
# match status_code:
#     case 200:
#         print("Success ✅")

#     case 404:
#         print("Resource not found ❌")

#     case 500:
#         if retry_count < 3:
#             print("Retry request 🔄")
#         else:
#             print("Alert admin 🚨")

#     case _:  # Default case for unknown errors
#         print("Unknown error ❓")








    




# # qno 
# #Data Quality Status: A dataset record has a status value such as 'clean', 'missing', 'duplicate',
# # or 'invalid'. Use match-case to determine what action should be taken.
# status = input("Enter data status: ").lower()

# match status:

#     case "clean":
#         print("✅ Record accepted.")

#     case "missing":
#         print("⚠ Handle missing values (impute or drop).")

#     case "duplicate":
#         print("🗑 Remove duplicate record.")

#     case "invalid":
#         print("🚩 Send record for validation.")

#     case _:
#         print("Unknown status.")








dataset_status = [
    "clean",
    "missing",
    "duplicate",
    "invalid",
    "clean"
]

for status in dataset_status:

    match status:

        case "clean":
            action = "Keep"

        case "missing":
            action = "Impute"

        case "duplicate":
            action = "Remove"

        case "invalid":
            action = "Review"

        case _:
            action = "Unknown"

    print(status, "→", action)









# qno
algo_name="Linear_regression".lower()

match algo_name:
    case "linear_regression":
        print("Strategy: Scale features and fit  linear model.")
    case "decision_tree":
        print("Strategy: Build tree using features splits.")
    case "random_forest":
        print("Strategy: Train multiple trees and aggregate results.")
    case _:
        print("Invalid algorithim name:")








# qno 
file_format="csv"

match file_format:
    case 'csv':
        print("Load file using pandas.read_csv()")
    case 'xlsx':
        print("Load file using pandas.read_excel()")
    case 'json':
        print("Load file using pandas.read_json()")
    case 'parquet':
        print("Load file using pandas.read_parquet()")
    case _:
        print("Unsupported file format")



