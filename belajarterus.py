def capitalh(baris, kolom):
    if baris % 2 == 0:
        print ("dimensi tidak sesuai")
    elif kolom == 1:
        print ("dimensi tidak sesuai")
    else:
        for i in range(1, baris+1):
            if i == (baris+1)/2:
                print ("#" *kolom)
            else:
                print("#", end="")
                print(" "*(kolom-2),end="")
                print("#")
                
        
    
