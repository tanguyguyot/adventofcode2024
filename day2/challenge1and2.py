def is_ascending(report, idx):
    if report[idx] < report[idx+1]:
        return True
    return False

def value_condition(report, idx):
    if abs(report[idx] - report[idx+1]) > 3 or abs(report[idx] - report[idx+1]) == 0:
        return False
    return True

def is_report_safe(report: tuple):
    if report[0] == report[1]:
        return False
    else:
        ascending = is_ascending(report, 0)
    for idx in range(0, len(report)-1):
        # value condition
        if not value_condition(report, idx):
            return False
        # ascending/descending condition
        if ascending and not is_ascending(report, idx):
            return False
        elif not ascending and is_ascending(report, idx):
            return False
    return True

def get_safe_reports(reports: set):
    safe_reports = set()
    unsafe_reports = set()
    for report in reports:
        report_is_safe = is_report_safe(report)
        # everything went fine, no break, then safe report
        if report_is_safe:
            safe_reports.add(report)
        else:
            unsafe_reports.add(report)
    return len(safe_reports), safe_reports, len(unsafe_reports), unsafe_reports

# get result  
if __name__ == "__main__":
    # data preparation
    file = "day2/input.txt"
    raw_reports = open(file, encoding="utf-8").read().strip().split("\n")
    reports_list = []
    reports = set()
    for report in raw_reports:
        reports.add(tuple(map(int, report.split())))
        reports_list.append(list(map(int, report.split())))
        
    len_safe_reports, safe_reports, len_unsafe_reports, unsafe_reports = get_safe_reports(reports)
    
    print("Safe reports for star 1 : ", len_safe_reports)
    # 680
    
    # Part 2 : problem dampener
    # data preparation
    unsafe_reports_list = list(unsafe_reports)
    safe_count = 0
    
    for i in range(len(unsafe_reports_list)):
        for idx in range(len(unsafe_reports_list[i])):
            report_copy = list(unsafe_reports_list[i])
            del report_copy[idx]
            report_is_safe = is_report_safe(report_copy)
            if report_is_safe:
                safe_count += 1
                break

    print("Additional safe reports : ", safe_count)
    # 30
    print("Total safe reports, for 2nd star : ", len_safe_reports + safe_count)
    # 710
    