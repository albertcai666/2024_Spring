# before: verint_silver_container -> ops-uvc-cur-verint-pii-delta
# now: verint_cdlsilver_container -> ops-uvc-cur-cdl-quality-pii-delta

# etl_created_date

lst = ["Contact Phone", "Survey Response Datetime", "Customer First Name", "Customer Last Name", "Contact ID", "Survey Program ", "Agent Name", "Amazon Agent Name", "Survey BU", "EDate", "First Owner Name", "Team Lead Name", "Callin Number", "Initiation Method", "Line of Business", "Customer Product", "Advisor Selling Code", "Case Status", "Contact Email"]

modified_list = list(map(lambda x: x.replace(" ", "_"), lst))
print(modified_list)
