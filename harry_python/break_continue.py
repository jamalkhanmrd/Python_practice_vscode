#  Sensor Failure Detection
# A smart hospital collects temperature readings every minute from an ICU sensor. If the sensor
# sends a value equal to None or -999, it means the sensor failed. Task: Loop through the readings
# list. • Skip invalid readings using continue. • Stop processing completely using break if 3 failures
# # occur consecutively. • Count valid readings and calculate their average

# ICU temperature readings
readings = [None, 37.0, None, 36.8, -999,
            37.2, None, -999, None, 38.0, 36.9]

valid_count = 0
total_temp = 0
failure_streak = 0 
invalid_counts=0  # consecutive failures counter

for temp in readings:

    # Check sensor failure
    if temp is None or temp == -999:
        print("Sensor failure detected")

        failure_streak += 1
        invalid_counts+=1
        # Stop if 3 consecutive failures
        if failure_streak == 3:
            print("⚠️ Sensor stopped after 3 consecutive failures")
            break

        continue   # skip invalid reading

    # Valid reading
    failure_streak = 0   # reset streak
    valid_count += 1
    total_temp += temp

# Calculate average
if valid_count > 0:
    average = total_temp / valid_count
    print("Invalid readings:",invalid_counts)
    print("\nValid readings:", valid_count)
    print("Average temperature:", round(average, 2),"\n")
else:
    print("No valid readings found.")











# 2. Log File Error Scanner
# You are given system log entries stored in a list. Each entry contains INFO, WARNING, or ERROR.
# Task: • Loop through logs. • Skip INFO messages using continue. • Print WARNING and ERROR
# messages. • Stop scanning once a CRITICAL ERROR appears.



logs = [
    "INFO: System started",
    "INFO: User login",
    "WARNING: High memory usage",
    "ERROR: Disk almost full",
    "INFO: Background job running",
    "CRITICAL ERROR: Database crashed",
    "ERROR: This should not be scanned"
]
for value in logs:

    if "CRITICAL ERROR" in value:
        print("CRITICAL ERROR Detected: Stopping scanning:")
        print(value)
        break

    if "INFO" in value:
        continue

    if "WARNING" in value or "ERROR" in value:
        print("WARNING and ERROR message detected:")
        print(value)








# . Dataset Cleaning Pipeline
# A dataset column contains mixed values: numbers, None, and negative placeholders (-1). Negative
# placeholders should be ignored. Task: • Use continue to skip invalid values. • Stop the loop if a
# value greater than 10,000 appears (possible corruption). • Store cleaned values in a new list.
dataset=[567,88,9,56,-1,9854,875,None,9987,557,36,547,4757,None,-1,None,121000,125,6498,5263]
clean_dataset=[]
# using foor loop for iterating 
for values in dataset:
    if values ==None or values==-1:         # negitive placeholder
        continue
    if values > 10000:
        print("Data corruption detected:",values)
        break
   
    
    clean_dataset.append(values)
    
print("Cleaned dataset :",clean_dataset)





# 4. Fraud Transaction Monitor
# A bank monitors transactions sequentially. Task: • Ignore transactions below 10 using continue. •
# Flag transactions above 5000. • Stop monitoring immediately if three flagged transactions appear
# consecutively

# Transaction dataset
transactions = [5, 20, 6000, 700, 8000, 50, 9000, 30]
flagged_count=0
for amount in transactions:
    if amount < 10:
        continue
    if amount>5000:
        print("Suspicious transactions detected:",amount)
        flagged_count+=1
        if flagged_count==3:
             print("Three suspicious taransaction appear consecutively!. Stopping transaction")
             break
    else:
        flagged_count=0
   
   

# Transaction dataset
transactions = [5, 20, 6000, 7000, 8000, 50, 9000, 30]

flagged_count = 0

for amount in transactions:

    # Ignore small transactions first
    if amount < 10:
        continue

    # Check suspicious transaction
    if amount > 5000:
        print("⚠️ Suspicious transaction detected:", amount)
        flagged_count += 1
    else:
        # Reset because frauds must be consecutive
        flagged_count = 0

    # Stop after 3 consecutive frauds
    if flagged_count == 3:
        print("🚨 Three suspicious transactions consecutively! Stopping monitoring.")
        break

   
# 6. Survey Data Validator
# Survey responses contain answers from 1–5 and sometimes invalid text. Task: • Skip invalid
# responses using continue. • Count only valid answers. • Stop processing once 100 valid responses
# are collected.
responses = [5, 3, "bad", 2, 7, 4, "N/A", 1, 5, 3]
valid_count=0
valid_answers=[]
for response in responses:
    if  not isinstance(response,int):
        continue
    if response<1 or response>5:
        continue
    valid_answers.append(response)
    valid_count+=1
    if valid_count==100:
        print("100 valid response collected:")
        break

print("Valid answers:",valid_answers)
print("Total number of valid counts:",valid_count)













# Streaming dataset
stream_data = [10, 20, 20, 30, 40, 30, 50, "STOP", 60]

processed_values = set()   # stores unique values

for value in stream_data:

    # Stop signal
    if value == "STOP":
        print("🛑 Shutdown signal received. Stopping processor.")
        break

    # Skip duplicates
    if value in processed_values:
        continue

    # Process unique value
    print("Processing value:", value)
    processed_values.add(value)


# Streaming dataset
stream_data = [10, 20, 20, 30, 40, 30, 50, "STOP", 60]
unique_data=set()
for values in stream_data:
    if values =="STOP":
        print("Shutdown signal appear:")
        break
    if values in unique_data:
        continue
    print("Processed value:",values)
    unique_data.add(values)










# 8. File Batch Processor
# Files are processed in sequence. Task: • Skip files with size 0. • Print processed file names. • Stop
# processing when a corrupted file is detected.

    # File batch processing
files = [
    {"name": "file1.txt", "size": 1024},
    {"name": "file2.txt", "size": 0},
    {"name": "file3.txt", "size": 2048},
    {"name": "file4.txt", "size": -1},  # corrupted
    {"name": "file5.txt", "size": 512}
]
for file in files:
    if file["size"]==0:
        continue
    if file["size"]<0:
       print(f"🚨 Corrupted file detected: {file['name']}. Stopping processing!")
       break
    print("Processing file:",file["name"])

















    dataset = [
    {"id": 1, "age": 25, "salary": 50000},
    {"id": 2, "age": None, "salary": 60000},
    {"id": 3, "age": 30, "salary": None},
    {"id": 4, "age": None, "salary": None},
    {"id": 5, "age": 28, "salary": 52000}
]

threshold = 3  # stop if total missing values exceed 3

missing_count=0
for row in dataset:
    if not None in row.values():
        continue
    for key,value in row.items():
        if value is None:
            row[key]=0
            missing_count+=1
    print("imputed row :",row)
    if missing_count>threshold:
        print("Missing value threshold exceeded.Stopped imputation!")
        break







# # qno 
# 10. Experiment Trial Analyzer
# Scientific experiment trials produce results sequentially. Task: • Skip trials marked 'invalid'. • Record
# successful trials. • Stop experiment when success rate exceeds 90%.


trials = [
    "failure",
    "failure",
    "invalid",
    "success",
    "failure",
    "failure",
    "invalid",
    "success",
    "failure"
] 
successful_record=[]
total_valid=0
success_count=0
for trail in trials:
    if trail=="invalid":
        continue
    total_valid+=1
    if trail=="success":
        success_count+=1
        successful_record.append(trail)
    succes_rate=(success_count/total_valid)*100
    print("Current success Rate:",succes_rate,"%")
    if succes_rate>90:
        print("Experiment stopped: Success Rate Exceeded 90% ")
        break
print("\nSuccessful Trials Recorded:",successful_record)

























trials = [
    "success",
    "failure",
    "invalid",
    "success",
    "success",
    "success",
    "invalid",
    "failure",
    "success"
]

total_valid = 0
successful_trials = 0
recorded_success = []

for trial in trials:

    # Skip invalid trials
    if trial == "invalid":
        continue

    # Count valid trials
    total_valid += 1

    # Record successful trials
    if trial == "success":
        successful_trials += 1
        recorded_success.append(trial)

    # Calculate success rate
    success_rate = (successful_trials / total_valid) * 100

    print("Current Success Rate:", success_rate, "%")

    # Stop experiment if success rate exceeds 90%
    if success_rate > 90:
        print("Experiment stopped: Success rate exceeded 90%")
        break

print("\nSuccessful Trials Recorded:", recorded_success)










# 1. Recommendation System Filter
# User interaction logs contain bot-generated entries. Task: • Skip bot interactions. • Process only
# real users. • Stop loop once 1000 valid interactions are processed.



logs = [
    {"user": "Ali", "type": "real"},
    {"user": "Bot_1", "type": "bot"},
    {"user": "Sara", "type": "real"},
    {"user": "Bot_2", "type": "bot"},
    {"user": "Ahmed", "type": "real"}
]

valid_interactions = 0
processed_users = []

for log in logs:

    # Skip bot interactions
    if log["type"] == "bot":
        continue

    # Process real users
    valid_interactions += 1
    processed_users.append(log["user"])

    print("Processed:", log["user"])

    # Stop after 1000 valid interactions
    if valid_interactions == 1000:
        print("Reached 1000 valid interactions")
        break

print("\nTotal Valid Interactions:", valid_interactions)
print("Users Processed:", processed_users)




