import string 
from string import punctuation as symbols
from string import ascii_lowercase as alphabet
from string import ascii_uppercase as Alphabet

symbols = symbols.replace("-","") 


def calc_final_worth(final_points, total_class_points):

    if len(str(final_points)) == 0 or len(str(total_class_points)) == 0: 
        raise ValueError
    for i in symbols: 
        if i in str(final_points) or i in str(total_class_points): 
            raise ValueError
    for i in alphabet: 
        if i in str(final_points) or i in str(total_class_points): 
            raise ValueError
    for i in Alphabet: 
        if i in str(final_points) or i in str(total_class_points):
            raise ValueError   
    if float(final_points) < 0 or float(total_class_points) < 0:
        raise ValueError 
    if float(final_points) >= 0 and float(total_class_points) == 0:
        raise ZeroDivisionError 
    else:
        final_worth = round(((float(final_points) / float(total_class_points)) * 100),2) 
        return final_worth
    
   
def grade_wanted(grade_wanted, final_worth, current_grade):
    
    if len(str(grade_wanted)) == 0 or len(str(final_worth)) == 0 or len(str(current_grade)) == 0: 
        raise ValueError
    for i in symbols: 
        if i in str(grade_wanted) or i in str(final_worth) or i in str(current_grade): 
            raise ValueError 
    for i in alphabet: 
        if i in str(grade_wanted) or i in str(final_worth) or i in str(current_grade): 
            raise ValueError
    for i in Alphabet: 
        if i in str(grade_wanted) or i in str(final_worth) or i in str(current_grade): 
            raise ValueError
    if float(grade_wanted) < 0 or float(final_worth) < 0 or float(current_grade) < 0: 
        raise ValueError
    if (float(grade_wanted) - (1 - float(final_worth) / 100) * float(current_grade)) >= 0 and (float(final_worth) / 100) == 0: 
        raise ZeroDivisionError
    if final_worth == 0: 
        raise ZeroDivisionError
    else: 
        desired_grade = ((float(grade_wanted) - ((1 - (float(final_worth) / 100)) * float(current_grade)))
                            / (float(final_worth) / 100))
        desired_grade = round(desired_grade,2)
        return desired_grade 


def grade_after_final(grade_prior, exam_score, final_weight):
    
    if len(str(grade_prior)) == 0 or len(str(exam_score)) == 0 or len(str(final_weight)) == 0:
        raise ValueError
    for i in symbols: 
        if i in str(grade_prior) or i in str(exam_score) or i in str(final_weight):  
            raise ValueError
    for i in alphabet: 
        if i in str(grade_prior) or i in str(exam_score) or i in str(final_weight):  
            raise ValueError
    for i in Alphabet: 
        if i in str(grade_prior) or i in str(exam_score) or i in str(final_weight):  
            raise ValueError
    if float(grade_prior) < 0 or float(final_weight) < 0 or float(exam_score) < 0:
        raise ValueError 
    else: 
        grade_after_final = round((float(exam_score) * (float(final_weight) / 100) +  
                                   (1 - (float(final_weight) / 100)) * float(grade_prior)),2)
        return grade_after_final


