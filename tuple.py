days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
print(days[2])
print(len(days))
person = {"name" : "John Doe", "age":30, "location": "Nairobi", "email" :"johndoe@mail.com"}
print(person["age"])


taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
print(type(taskList))
tasklist_tuple=taskList[2][2]
print(tasklist_tuple["currency"])
print(taskList[2][1])
print(len(taskList))

taskList_987=taskList[3]
print(taskList_987)
taskList_987=str(taskList_987)
task=taskList_987[::-1]
print(task)
reversed_item=int(task)
taskList[3]=reversed_item
print (taskList)

task_tuple=list(taskList[4])
print(task_tuple)
task_tuple[1]="Jane"