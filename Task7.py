#String formatting


format_objects = {'task_no':7,
                    'learning_objects':'texts'}

text = """Hi, there!
    I'am learning how to format {learning_objects} through task {task_no}"""

print(text.format(**format_objects))

#or
task_no =7
learning_objects = 'texts'

text = f"""Hi, there!
    I'am learning how to format {learning_objects} through task {task_no}"""
print(text)
