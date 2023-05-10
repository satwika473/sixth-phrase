import math

C = 50
H = 30

def calculateQ(D):
    return int(math.sqrt((2 * C * D) / H))

def calculateQList(DList):
    QList = []
    for D in DList:
        Q = calculateQ(int(D))
        QList.append(Q)
    return QList

# Prompt the user to enter a comma-separated sequence of D values
DList = input("Enter a comma-separated sequence of D values: ").split(",")

# Calculate the corresponding Q values
QList = calculateQList(DList)

# Print the Q values
print(",".join(str(Q) for Q in QList))
