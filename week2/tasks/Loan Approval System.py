def check_loan_eligibility(age, income, credit_score, has_criminal_record):
    if age < 18:
        return "Rejected!"
    if income < 50000:
        return "Rejected!"
    if credit_score < 600:
        return "Rejected!"
    if has_criminal_record:
        return "Rejected!"
    
    return "Eligible for loan."
print(check_loan_eligibility(2, 5, 60, False))