from sklearn import metrics
import pandas as pd

question_answers = [
	["DM-2011", "DM-6733", "DM-18674", "DM-9149", "DM-578", "DM-22893", "DM-951", "DM-31802", "DM-16323"],
	["Won't fix", "Done", "Done", "Done", "Done", "Done", "Done", "Invalid", "Invalid"]
]

user_answers = [
	["Won't fix", "Done", "Done", "Won't fix", "Done", "Invalid", "Won't fix", "Invalid", "Won't fix"],
	["Done", "Invalid", "Done", "Invalid", "Done", "Done", "Done", "Done", "Invalid"],
	["Done", "Invalid", "Done", "Won't fix", "Invalid", "Won't fix", "Won't fix", "Won't fix", "Invalid"],
	["Done", "Invalid", "Done", "Done", "Invalid", "Done", "Done", "Done", "Won't fix"],
	["Done", "Invalid", "Done", "Invalid", "Invalid", "Invalid", "Done", "Invalid", "Invalid"],
	["Done", "Invalid", "Won't fix", "Done", "Won't fix", "Done", "Won't fix", "Invalid", "Invalid"],
	["Done", "Won't fix", "Done", "Done", "Done", "Invalid", "Done", "Done", "Invalid"],
	["Invalid", "Won't fix", "Won't fix", "Invalid", "Invalid", "Won't fix", "Won't fix", "Won't fix", "Invalid"],
	["Won't fix", "Won't fix", "Done", "Done", "Done", "Won't fix", "Invalid", "Invalid", "Done"],
	["Done", "Invalid", "Done", "Invalid", "Won't fix", "Won't fix", "Done", "Done", "Invalid"]
]

y_true = question_answers[1] * 10
y_pred = [item for sublist in user_answers for item in sublist]

print (y_true)
report = metrics.classification_report(y_true, y_pred, output_dict=True)
print (report)
report_frame = pd.DataFrame(report).transpose()
result = report_frame.round(3)
# result= result.round({'support': 0})
print (result.to_latex())