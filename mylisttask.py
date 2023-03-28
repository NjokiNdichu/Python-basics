trainees = ["John", [2, ["James","Mary"]]]
print("Original list",trainees)

print(trainees[1][0])
print(trainees[1][1][0])

trainees.append(56)
print(trainees)

trainees_new=trainees[1][1]
trainees_new.insert(1, "Mike")
print(trainees)

trainees[1][0]="8"
print(trainees)

del trainees[0]
print(trainees)
trainees_del=trainees[0][1]
del trainees_del[2]
print (trainees)
print(len(trainees))



