n = int(input("enter number of semister "))
total_points_given = 0
total_points_yougot = 0

for i in range(1,n+1):
    crd = int(input('credits registerd for {} semister '.format(i) ))
    total_points_given += crd
    m = int(input('number of subjects ' )) 
    for j in range(1,m+1):
        op = int(input('enter the subject credit points for {} subject '.format(j) ))
        total_points_yougot += op
    
final = total_points_yougot/total_points_given
print(final)
