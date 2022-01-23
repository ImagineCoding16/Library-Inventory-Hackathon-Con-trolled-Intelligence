#Fiction
Fiction= {"001":"The Book Theif by Markus Zusak.", 
          "002": "The Hate You Give by Angie Thomas", 
          "003": "Hunger Games by Suzzane Collins", 
          "004": "The House on Mango Street by Sandra Cisneros", 
          "005": "The Curious Incident of the Dog in the Night-time by Mark Haddon", 
          "006": "A Wrinkle in Time by Madeleine L'Engle.",
          "007": "Educated by Tara Westover.", 
          "008": "To Kill a Mockingbird by Harper Lee", 
          "009": "I Am Malala: The Girl Who Stood Up for Education and Was Shot by the Taliban by Malala Yousafzai", 
          "010": "Anne Frank: The Diary of a Young Girl by Anne Frank"}

#Sci-fi
Sci_fi={"011":"The Infinity Courts by Akemi Dawn Bowman", 
        "012": "Fahrenheit 451 by Ray Bradbury", 
        "013": "Last Star Burning by Caitlin Sangster", 
        "014": "Fate of Flames by Sarah Raughley", 
        "015": "Life as We Knew It by Susan Beth Pfeffer", 
        "016": "The Left Hand of Darkness by Ursula K. Le Guin",
        "017": "The Martian by Andy Weir", 
        "018": "Foundation by Isaac Asimov", 
        "019": "Brave New World by Aldous Huxley", 
        "020": "Sky Without Stars by Jessica Brody and Joanne Rendell."}

# Horror
Horror={"021": "The Cheerleaders. by Kara Thomas",
        "022": "House of Salt and Sorrows. by Erin A.",
        "023": "The Babysitters Coven. by Kate M",
        "024": "A Wicked Magic. by Sasha Laurens",
        "025": "Harrow Lake. by Kat Ellis",
        "026": "Carrie. by Stephen King",
        "027": "The Dark Descent of Elizabeth Frankenstein. by Kiersten White",
        "028": "Amity by Micol Ostow",
        "029": "Bleeding Violet by Dia Reeves.",
        "030": "Dream Fall by Amy Plum."}

#Thriller
Thriller={"031": "Charm and Strange by Stephanie Kuehn",
          "032": "The Arsonist by Stephanie Oakes",
          "033": "My Own Worst Frenemy by Kimberly Reid.",
          "034": "A Spy in the House by Y.S. Lee",
          "035": "Overturned by Lamar Giles.",
          "036": "Follow Me Down by Tanya Byrne.",
          "037": "Out of the Easy by Ruta Sepetys",
          "038": "Luckiest Girl Alive by Jessica Knoll.",
          "039": "The Silent Companions by Laura Purcell.",
          "040": "Charm and Strange by Stephanie Kuehn"}

# Fantasy
Fantasy= {"041": "A Wizard of Earthsea by Ursula K",
          "042": "The Blue Sword by Robin McKinley.",
          "043": "Howl's Moving Castle by Diana Wynne Jones.",
          "044": "Sabriel by Garth Nix",
          "045": "Graceling by Kristin Cashore",
          "046": "harry potter- cursed child by j.k. rowling",
          "047": "The Reader by Traci Chee",
          "048": "The Hobbit. by J.R.R. Tolkien",
          "049": "Rebel of the Sands by Alwyn Hamilton",
          "050": "Seraphina by Rachel Hartman"}

Issued= []

# Main
print(" WELCOME TO THE LIBRARY!!!")
print()

cont= ""

while cont!="exit":
  print("What would you like to do?")
  print("1. Manage Inventory")
  print("2. Issue or Return a book")
  print("Enter the number")
  action= input()
  print()

  # Manage Inventory
  if action== "1":
    print("Would you like to \n 1. View the books available in the libraby \n 2. Remove a book \n 3. Add a book")
    action1= input()
    
    # View the Books
    if action1== "1":
      print()
      print("Please choose a genre from the list ")
      print(" 1. Fiction \n 2. Sci-fi \n 3. Horror \n 4. Thriller \n 5. Fantasy \n 6. View All the Books Available in the library")
      genre= input("Please enter a number \n")
      print()

      # Fiction Genre
      if genre== "1":
        print("The books in Fiction are: ")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Fiction:
          print(i,"     ~       ", Fiction[i])
          print("____________________________________________________________________")

      # Sci-fi Genre
      elif genre== "2":
        print("The books in Sci-fi are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Sci_fi:
          print(i,"      ~      ", Sci_fi[i])
          print("____________________________________________________________________")
    # Horror Genre
      elif genre== "3":
        print("The books in Horror are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Horror:
          print(i, "      ~       ", Horror[i])
          print("____________________________________________________________________")

      #Thriller Genre
      elif genre== "4":
        print("The books in Thriller are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Thriller:
          print(i,"       ~       ", Thriller[i])
          print("____________________________________________________________________")
      #Fantasy Genre
      elif genre== "5":
        print("The books in Fantasy are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Fantasy:
          print(i,"       ~       ", Fantasy[i])
          print("____________________________________________________________________")

      #View all the Books
      elif genre== "6":
        print("____________________________________________________________________")
        print("The books in the library are:")
        print("____________________________________________________________________")
        
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")

        for i in Fiction:
          print(i,"     ~       ", Fiction[i])
          print("____________________________________________________________________")

        for s in Sci_fi:
          print(s,"      ~      ", Sci_fi[s])
          print("____________________________________________________________________")

        for h in Horror:
          print(h, "      ~       ", Horror[h])
          print("____________________________________________________________________")

        for t in Thriller:
          print(t,"       ~       ", Thriller[t])
          print("____________________________________________________________________")

        for f in Fantasy:
          print(f,"     ~       ", Fantasy[f])
          print("____________________________________________________________________")
      else:
        print("Not found. Please try again!")

  #Remove a book
    elif action1== "2":
      print()
      print("From which genre would you like to remove a book?")
      print(" 1. Fiction \n 2. Sic-fi \n 3. Horror \n 4. Thriller \n 5. Fantasy")
      print("Enter the number")
      remove= input()

      #Fiction book remove
      if remove== "1":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Fiction:
          print(i,"     ~       ", Fiction[i])
          print("____________________________________________________________________")

        print()
        print("Which book do you want to remove? (Enter the reference number.)")
        num= input()
        print()
        print("The books now present in this genre are:")
        Fiction.pop(num)
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Fiction:
          print(i,"     ~       ", Fiction[i])
          print("____________________________________________________________________")
      
      #Sci_fi book remove
      elif remove=="2":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Sci_fi:
          print(i,"     ~       ", Sci_fi[i])
          print("____________________________________________________________________")

        print()
        print("Which book do you want to remove? (Enter the reference number.)")
        num= input()
        print()
        print("The books now present in this genre are:")
        Sci_fi.pop(num)
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Sci_fi:
          print(i,"     ~       ", Sci_fi[i])
          print("____________________________________________________________________")
      
      #Horror Book Remove
      elif remove== "3":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Horror:
          print(i,"     ~       ", Horror[i])
          print("____________________________________________________________________")

        print()
        print("Which book do you want to remove? (Enter the reference number.)")
        num= input()
        print()
        print("The books now present in this genre are:")
        Horror.pop(num)
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Horror:
          print(i,"     ~       ", Horror[i])
          print("____________________________________________________________________")

      #Thriller book remove
      elif remove== "4":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Thriller:
          print(i,"     ~       ", Thriller[i])
          print("____________________________________________________________________")

        print()
        print("Which book do you want to remove? (Enter the reference number.)")
        num= input()
        print()
        print("The books now present in this genre are:")
        Thriller.pop(num)
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Thriller:
          print(i,"     ~       ", Thriller[i])
          print("____________________________________________________________________")
      
      #Fantasy Book Remove
      elif remove=="5":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Fantasy:
          print(i,"     ~       ", Fantasy[i])
          print("____________________________________________________________________")

        print()
        print("Which book do you want to remove? (Enter the reference number.)")
        num= input()
        print()
        print("The books now present in this genre are:")
        Horror.pop(num)
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Fantasy:
          print(i,"     ~       ", Fantasy[i])
          print("____________________________________________________________________")

      else:
        print()
        print("Not found. Please try again!")

  #Adding a book
    elif action1=="3":
      print("In which genre would you like to add a book?")
      print()
      print(" 1. Fiction \n 2. Sic-fi \n 3. Horror \n 4. Thriller \n 5. Fantasy")
      print("Enter the number")
      add= input()
      
      #Fiction book add
      if add=="1":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Fiction:
          print(i,"     ~       ", Fiction[i])
          print("____________________________________________________________________")

        print()
        print("Which book would you like to add to this list? (Enter the book and author")
        added= input()
        Fiction["051"]= added
        print("The books now present in this genre are:")
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Fiction:
          print(i,"     ~       ", Fiction[i])
          print("____________________________________________________________________")

      #Sci-fi Add Book
      elif add=="2":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Sci_fi:
          print(i,"     ~       ", Sci_fi[i])
          print("____________________________________________________________________")

        print()
        print("Which book would you like to add to this list? (Enter the book and author")
        added= input()
        Sci_fi["051"]= added
        print("The books now present in this genre are:")
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Sci_fi:
          print(i,"     ~       ", Sci_fi[i])
          print("____________________________________________________________________")
      
      #Horror add book
      elif add=="3":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Horror:
          print(i,"     ~       ", Horror[i])
          print("____________________________________________________________________")

        print()
        print("Which book would you like to add to this list? (Enter the book and author")
        added= input()
        Horror["051"]= added
        print("The books now present in this genre are:")
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Horror:
          print(i,"     ~       ", Horror[i])
          print("____________________________________________________________________")
        
    # Thriller add book
      elif add=="4":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Thriller:
          print(i,"     ~       ", Thriller[i])
          print("____________________________________________________________________")

        print()
        print("Which book would you like to add to this list? (Enter the book and author")
        added= input()
        Thriller["051"]= added
        print("The books now present in this genre are:")
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Thriller:
          print(i,"     ~       ", Thriller[i])
          print("____________________________________________________________________")

    # Fantasy add Book
      elif add=="5":
        print("____________________________________________________________________")
        print("Reference number |","  Book and Author")
        for i in Fantasy:
          print(i,"     ~       ", Fantasy[i])
          print("____________________________________________________________________")

        print()
        print("Which book would you like to add to this list? (Enter the book and author")
        added= input()
        Fantasy["051"]= added
        print("The books now present in this genre are:")
        print("____________________________________________________________________")
        print()
        print("Reference number |","  Book and Author")
        for i in Fantasy:
          print(i,"     ~       ", Fantasy[i])
          print("____________________________________________________________________")
    else:
      print("Not Found! Please try again!")

  # Issue or return a book
  elif action=="2":
    print("Do you want to")
    print(" 1. Issue a book \n 2. Return a book \n 3. Report a lost book\nPlease enter a number:")
    function= input()
    
    #Issue
    if function== "1":
      print("From which genre do you want to issue a book from?")
      print(" 1. Fiction \n 2. Sci-fi \n 3. Horror \n 4. Thriller \n 5. Fantasy")
      print("Enter the number")
      issue= input()
      # Fiction Genre
      if issue== "1":
        print("The books in Fiction are: ")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Fiction:
          print(i,"     ~       ", Fiction[i])
          print("____________________________________________________________________")
        print("Please enter the reference number to issue the book.")
        refer= input() 
        if refer in Fiction:
          Fiction.pop(refer)
          print("The record has been saved! Thank you!!")
          Issued.append(refer)
        else:
          print("Not found! Try Again!")

      # Sci-fi Genre
      elif genre== "2":
        print("The books in Sci-fi are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Sci_fi:
          print(i,"      ~      ", Sci_fi[i])
          print("____________________________________________________________________")

        print("Please enter the reference number to issue the book.")
        refer= input() 
        if refer in Sci_fi:
          Sci_fi.pop(refer)
          print("The record has been saved! Thank you!!")
          Issued.append(refer)
        else:
          print("Not found! Try Again!")


    # Horror Genre
      elif genre== "3":
        print("The books in Horror are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Horror:
          print(i, "      ~       ", Horror[i])
          print("____________________________________________________________________")
        print("Please enter the reference number to issue the book.")
        refer= input() 
        if refer in Horror:
          Horror.pop(refer)
          print("The record has been saved! Thank you!!")
          Issued.append(refer)
        else:
          print("Not found! Try Again!")


      #Thriller Genre
      elif genre== "4":
        print("The books in Thriller are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Thriller:
          print(i,"       ~       ", Thriller[i])
          print("____________________________________________________________________")
        print("Please enter the reference number to issue the book.")
        refer= input() 
        if refer in Thriller:
          Thriller.pop(refer)
          print("The record has been saved! Thank you!!")
          Issued.append(refer)
        else:
          print("Not found! Try Again!")


      #Fantasy Genre
      elif genre== "5":
        print("The books in Fantasy are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Fantasy:
          print(i,"       ~       ", Fantasy[i])
          print("____________________________________________________________________")
        print("Please enter the reference number to issue the book.")
        refer= input() 
        if refer in Fantasy:
          Fantasy.pop(refer)
          print("The record has been saved! Thank you!!")
          Issued.append(refer)
        else:
          print("Not found! Try Again!")

    #Returning a book
    elif function== "2":
      print("Which genre do you want to return a book to?")
      print(" 1. Fiction \n 2. Sic-fi \n 3. Horror \n 4. Thriller \n 5. Fantasy")
      print("Enter the number")
      ret= input()
      if ret== "1":
        print("The books in Fiction are: ")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Fiction:
          print(i,"     ~       ", Fiction[i])
          print("____________________________________________________________________")

        print("Enter the reference number: ")
        refno= input()
        print("Enter the Book Name: ")
        bookn= input()
        if refno in Issued:
          print("Your book has been returned! Thank you!")
          Fiction.update({refno: bookn})
          Issued.remove(refno)
        else:
          print("The book doesn't belong here!!")

      # Sci-fi Genre
      elif ret== "2":
        print("The books in Sci-fi are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Sci_fi:
          print(i,"      ~      ", Sci_fi[i])
          print("____________________________________________________________________")
        

        print("Enter the reference number: ")
        refno= input()
        print("Enter the Book Name: ")
        bookn= input()
        if refno in Issued:
          print("Your book has been returned! Thank you!")
          Sci_fi.update({refno: bookn})
          Issued.remove(refno)
        else:
          print("The book doesn't belong here!!")

    # Horror Genre
      elif ret== "3":
        print("The books in Horror are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Horror:
          print(i, "      ~       ", Horror[i])
          print("____________________________________________________________________")
        
        print("Enter the reference number: ")
        refno= input()
        print("Enter the Book Name: ")
        bookn= input()
        if refno in Issued:
          print("Your book has been returned! Thank you!")
          Horror.update({refno: bookn})
          Issued.remove(refno)
        else:
          print("The book doesn't belong here!!")

      #Thriller Genre
      elif ret== "4":
        print("The books in Thriller are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Thriller:
          print(i,"       ~       ", Thriller[i])
          print("____________________________________________________________________")

        print("Enter the reference number: ")
        refno= input()
        print("Enter the Book Name: ")
        bookn= input()
        if refno in Issued:
          print("Your book has been returned! Thank you!")
          Thriller.update({refno: bookn})
          Issued.remove(refno)
        else:
          print("The book doesn't belong here!!")

      #Fantasy Genre
      elif ret== "5":
        print("The books in Fantasy are:")
        print("____________________________________________________________________")
        print("Reference number |","   Book and Author")
        print("____________________________________________________________________")
        for i in Fantasy:
          print(i,"       ~       ", Fantasy[i])
          print("____________________________________________________________________")

        print("Enter the reference number: ")
        refno= input()
        print("Enter the Book Name: ")
        bookn= input()
        if refno in Issued:
          print("Your book has been returned! Thank you!")
          Fantasy.update({refno: bookn})
          Issued.remove(refno)
        else:
          print("The book doesn't belong here!!")

        

    # Lost the book
    elif function== "3":
      print()
      print("Please pay a fine of ₹200/- for the lost book!")
    
    else:
      print("Not found. Please try agian!!")

  else:
    print("Not found!! Please try again!")
  
  print()
  
  cont= input("Do you want to continue (If yes press the 'Enter' key. If no, type 'exit')\n").lower()

# End of the code.