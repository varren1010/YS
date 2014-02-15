print ("LST Maker 1.0 - Varren ")

addon = input("Enter a name for your files and user folder ")

lstline = ("/user/"+addon+"/"+addon+'.dat'+' '+"/user/"+addon+"/"+addon+'.dnm'+' '+"/user/"+addon+"/"+addon+'_coll'+'.srf'+" "+"/user/"+addon+"/"+addon+'_cock'+'.srf')
print (lstline)
ver = input("Is the information correct? ")
if ver == 'yes' or ver == 'Yes' or ver == 'y' or ver == 'Y':
    fo = open("air_lstmaker.lst", "wb")
    fo.write(bytes(lstline, 'UTF-8')) ;
  
else:
    print ("That line will not be added")

status = 'complete'

while status == 'complete':
    again = input("Would you like to add another line? ")
    if again == 'yes' or again == 'Yes' or again == 'Y' or again == 'y':
        addon2 = input("Enter another name for your files, user folder will stay the same ")
        lstline2 = (" \r\n/user/"+addon+"/"+addon2+'.dat'+' '+"/user/"+addon+"/"+addon2+'.dnm'+' '+"/user/"+addon+"/"+addon2+'_coll'+'.srf'+" "+"/user/"+addon+"/"+addon2+'_cock'+'.srf')
        print(lstline2)
        ver = input("Is the information correct? ")
        if ver == 'yes' or ver == 'Yes' or ver == 'y' or ver == 'Y':
            fo = open("air_lstmaker.lst", "ab")
            fo.write(bytes(lstline2, 'UTF-8')) ;
        else:
            print ("That line will not be added")
         
    elif again == 'no' or again == 'No' or again == 'n' or again == 'N':
        print("The script will now end")
        break

