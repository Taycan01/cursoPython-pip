import matplotlib as plt

def generar_pie_chat():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()
    
#generar_pie_chat()

print("Esto funciona bien")