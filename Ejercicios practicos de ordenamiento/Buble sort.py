def ordenamiento_burbuja(arr):
    n = len(arr)-1
    #blucle para hacer un recorrido en en array
    for i in range(0,n):
        print(f'Recorrido #{i+1}')
        #comparar y realizar intercambio
        for j in range(0, n):
            print(f'Comparación:{arr[j]} > {arr[j + 1]}')
            if arr[j] > arr[j + 1]:
                print(f'Intercambio:{arr[j]}x{arr[j + 1]}')
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr = [15,5,10,20,25]
 
print("Array antes de ordenar:")
print(arr)
ordenamiento_burbuja(arr) 
print("\nArray después de ordenar usando bubble sort:")
print(arr)
