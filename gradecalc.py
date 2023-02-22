import tkinter as tk
from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image
import string 
from string import punctuation as symbols 
from string import ascii_lowercase as alphabet
from string import ascii_uppercase as Alphabet

symbols = symbols.replace("-","")

window = Tk()
window.title("Grade Calculator")

canvas = tk.Canvas(window, width = 700, height = 600)
canvas.grid(columnspan = 60, rowspan = 20)

logo = ImageTk.PhotoImage(Image.open("logo.png"))
logo_label = Label(image = logo)
logo_label.grid(row =0 ,columnspan = 60, pady = (25,25))

total_final_points_e = Entry(window,
                      bg = "#e0dcdf",
                      fg = "black",
                      width = 5)
total_final_points_e.grid(row = 3, column = 20)

total_class_points_e = Entry(window,
                      bg = "#e0dcdf",
                      fg = "black",
                      width = 5)
total_class_points_e.grid(row = 2, column = 20)

final_points = (total_final_points_e.get())
total_class_points = (total_class_points_e.get())

def calc_final_worth(final_points, total_class_points):
    
    final_points = (total_final_points_e.get())
    total_class_points = (total_class_points_e.get())
    

    for i in symbols: 
        if i in str(final_points) or i in str(total_class_points):
            messagebox.showwarning("Error", "Please Enter Numeric Values Only") 
    for i in alphabet: 
        if i in str(final_points) or i in str(total_class_points):
            messagebox.showwarning("Error", "Please Enter Numeric Values Only") 
    for i in Alphabet: 
        if i in str(final_points) or i in str(total_class_points):
            messagebox.showwarning("Error", "Please Enter Numeric Values Only") 
    if len(final_points) == 0 or len(total_class_points) == 0: 
        messagebox.showwarning("Error", "Please Fill in All Fields")
    if float(final_points) < 0 or float(total_class_points) < 0:
        messagebox.showwarning("Error", "Values Must Be Positive")
    elif float(final_points) >= 0 and float(total_class_points) == 0:
        messagebox.showwarning("Error", "Total Class Points Cannot be 0")
    else:
        final_worth = round(((float(final_points) / float(total_class_points)) * 100),2) 
        outcome_final_worth_label.config(
            text = f"Your final is worth: {final_worth} % of your total course grade.")
                
grade_wanted_e = Entry(window,
                      bg = "#e0dcdf",
                      fg = "black",
                      width = 5)
grade_wanted_e.grid(row = 6, column = 20)

final_worth_e = Entry(window,
                      bg = "#e0dcdf",
                      fg = "black",
                      width = 5)
final_worth_e.grid(row = 7, column = 20)

current_grade_e = Entry(window,
                      bg = "#e0dcdf",
                      fg = "black",
                      width = 5)
current_grade_e.grid(row = 8, column = 20)

grade_wanted = (grade_wanted_e.get())
final_worth = (final_worth_e.get())
current_grade = (current_grade_e.get())

def grade_wanted(grade_wanted, final_worth, current_grade):
    
    try:
        grade_wanted = (grade_wanted_e.get())
        final_worth = (final_worth_e.get())
        current_grade = (current_grade_e.get())
        for i in symbols: 
            if i in str(grade_wanted) or i in str(final_worth) or i in str(current_grade): 
                messagebox.showwarning("Error", "Please Enter Numeric Values Only")  
        for i in alphabet: 
            if i in str(grade_wanted) or i in str(final_worth) or i in str(current_grade): 
                messagebox.showwarning("Error", "Please Enter Numeric Values Only")
        for i in Alphabet:
            if i in str(grade_wanted) or i in str(final_worth) or i in str(current_grade): 
                messagebox.showwarning("Error", "Please Enter Numeric Values Only")
        if len(grade_wanted) == 0 or len(final_worth) == 0 or len(current_grade) == 0: 
            messagebox.showwarning("Error", "Please Fill in All Fields")
        if float(grade_wanted) < 0 or float(final_worth) < 0 or float(current_grade) < 0:
            messagebox.showwarning("Error", "Values Must Be Positive")
            raise ValueError
        if final_worth == 0:
            messagebox.showwarning("Error", "Enter Final Exam Weight Greater Than Zero")
        else: 
            desired_grade = ((float(grade_wanted) - ((1 - (float(final_worth) / 100)) * float(current_grade)))
                             / (float(final_worth) / 100))
            desired_grade = round(desired_grade,2)
            outcome_desired_grade_label.config(
                text = f"You need {desired_grade} % to receive {grade_wanted} % in the course.")
    except ZeroDivisionError: 
        messagebox.showwarning("Error", "Enter Final Exam Weight Greater Than Zero")
        

grade_before_final_e = Entry(window,
                      bg = "#e0dcdf",
                      fg = "black",
                      width = 5)
grade_before_final_e.grid(row = 11, column = 20)
        
final_exam_grade_e = Entry(window,
                      bg = "#e0dcdf",
                      fg = "black",
                      width = 5)
final_exam_grade_e.grid(row = 12, column = 20)
        
final_worth_2_e = Entry(window,
                      bg = "#e0dcdf",
                      fg = "black",
                      width = 5)
final_worth_2_e.grid(row = 13, column = 20)        

grade_prior = (grade_before_final_e.get())
exam_score = (final_exam_grade_e.get())
final_weight = (final_worth_2_e.get())
        
def grade_after_final(grade_prior, exam_score, final_weight):
    
        grade_prior = (grade_before_final_e.get())
        exam_score = (final_exam_grade_e.get())
        final_weight = (final_worth_2_e.get())
        for i in symbols: 
            if i in str(grade_prior) or i in str(exam_score) or i in str(final_weight): 
                 messagebox.showwarning("Error", "Please Enter Numeric Values Only")
        for i in alphabet: 
            if i in str(grade_prior) or i in str(exam_score) or i in str(final_weight):
                 messagebox.showwarning("Error", "Please Enter Numeric Values Only")
        for i in Alphabet: 
            if i in str(grade_prior) or i in str(exam_score) or i in str(final_weight):
                 messagebox.showwarning("Error", "Please Enter Numeric Values Only") 
        if len(grade_prior) == 0 or len(exam_score) == 0 or len(final_weight) == 0: 
            messagebox.showwarning("Error", "Please Fill in All Fields")
        elif float(grade_prior) < 0 or float(final_weight) < 0 or float(exam_score) < 0:
            messagebox.showwarning("Error", "Values Must Be Positive")
        else:
            grade_after_final = round((float(exam_score) * (float(final_weight) / 100) +  
                                       (1 - (float(final_weight) / 100)) * float(grade_prior)),2)
            outcome_grade_after_label.config(
                text = f"Your final course grade is {grade_after_final} %.")

# Formula to determine how much final is worth Title 
formula_final_worth_l = Label(window,
                     text = "Final Exam Weight:",
                     font = ("Helvetica", 20))
formula_final_worth_l.grid(row = 1, column = 0, columnspan = 20)


# Total Points in Class 
total_class_points_l = Label(window,
                     text = "Total Points in Class:",
                     font = ("Helvetica", 15))
total_class_points_l.grid(row = 2, column = 0, columnspan = 20)

# Points of Final 
total_final_points_l = Label(window,
                     text = "Total Points on Final:",
                     font = ("Helvetica", 15))
total_final_points_l.grid(row = 3, column = 0, columnspan = 20)

outcome_final_worth_label = Label(window, text = " ")
outcome_final_worth_label.grid(row = 4, column = 10, pady = 20)


calculate_final_worth_b = Button(window, 
                                 text= "Calculate", 
                                 command = lambda: calc_final_worth(final_points,total_class_points,), 
                                 relief = "raised")
calculate_final_worth_b.grid(row = 3, column = 40)

# Formula to determine grade needed on final for desired grade title 
formula_final_needed_l = Label(window,
                     text = "Grade Needed on Final for Desired Course Grade:",
                     font = ("Helvetica", 20))
formula_final_needed_l.grid(row = 5, column = 0, columnspan = 20, padx = (25,0))

grade_wanted_l = Label(window,
                     text = "Desired Grade in Class:",
                     font = ("Helvetica", 15))
grade_wanted_l.grid(row = 6, column = 0, columnspan = 20)

final_worth_l = Label(window,
                     text = "Final Exam Weight:",
                     font = ("Helvetica", 15))
final_worth_l.grid(row = 7, column = 0, columnspan = 20)

current_grade_l = Label(window,
                     text = "Current Grade:",
                     font = ("Helvetica", 15))
current_grade_l.grid(row = 8, column = 0, columnspan = 20)

outcome_desired_grade_label = Label(window, text = " ")
outcome_desired_grade_label.grid(row = 9, column = 10, pady = 20)

calculate_desired_grade_b = Button(window, 
                                   text= "Calculate",
                                   command = lambda: grade_wanted(grade_wanted, final_worth, current_grade,), 
                                   relief = "raised")
calculate_desired_grade_b.grid(row = 8, column = 40)

# Formula for final grade in class after taking the final 

final_grade_l = Label(window,
                     text = "Course Grade After Final:",
                     font = ("Helvetica", 20))
final_grade_l.grid(row = 10, column = 0, columnspan = 20, padx = 10)

grade_before_final_l = Label(window,
                     text = "Grade Prior to Final:",
                     font = ("Helvetica", 15))
grade_before_final_l.grid(row = 11, column = 0, columnspan = 20)

final_exam_grade_l = Label(window,
                     text = "Grade Received on Final:",
                     font = ("Helvetica", 15))
final_exam_grade_l.grid(row = 12, column = 0, columnspan = 20)

final_worth_2_l = Label(window,
                     text = "Final Exam Weight:",
                     font = ("Helvetica", 15))
final_worth_2_l.grid(row = 13, column = 0, columnspan = 20)

calculate_final_grade_b = Button(window, 
                                 text= "Calculate", 
                                 command = lambda: grade_after_final(grade_prior, exam_score, final_weight),
                                 relief = "raised")
calculate_final_grade_b.grid(row = 13, column = 40)


outcome_grade_after_label = Label(window, text = " ")
outcome_grade_after_label.grid(row = 14, column = 10, pady = 20)

def clear_data():
    total_final_points_e.delete(0, END)
    total_class_points_e.delete(0, END)
    final_worth_2_e.delete(0, END)
    final_exam_grade_e.delete(0, END)
    grade_before_final_e.delete(0, END)
    final_worth_e.delete(0, END)
    grade_wanted_e.delete(0, END)
    current_grade_e.delete(0, END)
    outcome_grade_after_label.config(text = " ")
    outcome_desired_grade_label.config(text = " ")
    outcome_final_worth_label.config(text = " ")

clear_button = Button(window, text = "Clear", command = clear_data, relief = "raised")
clear_button.grid(row = 15, column = 15, pady = (0,25))

window.mainloop()

#logo made via logomakr.com/app